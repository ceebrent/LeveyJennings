import calendar
import csv
import datetime
import errno
import glob
import os
import re
import shutil
import sys
import pandas as pd


class LeveyJennings(object):
    def __init__(self, lab_name):

        self.homeDirectory = get_home()
        self.lab_name = lab_name

    # Creates and returns folder to store results into
        def results_folder(self):
            
            result_folder = os.path.join(self.homeDirectory, 'Results')
            os.makedirs(result_folder, exist_ok=True)
            
            lab_results = os.path.join(result_folder, self.lab_name)

            os.makedirs(lab_results, exist_ok=True)
            return lab_results
        self.lab_results = results_folder(self)

    # Walks through all files and directories in home folder with ending text and containing lab name
        def original_txt(self):
            lab_text_files = []
            for dirpath, dirnames, files in os.walk(os.path.join(self.homeDirectory, 'Data')):
                for filename in files:
                    if filename.endswith('.txt') and self.lab_name in filename:
                        lab_text_files.append(os.path.join(dirpath, filename))
            return sorted(lab_text_files)
        self.lab_text_files = original_txt(self)

    def make_unique_files(self):
        """Creates temp folder to store txt files in until they can be renamed by date and
        sorted according to month. This is designed to take the first txt file created if there are
        duplicate file names ie. "PP BH-502 B3 PA" and "PP BH-502 B3 PB".
        Note the PA is not always the first file created by the scientists while analyzing"""

        temp_result_path = os.path.join(self.lab_results, 'Temp_TXT')
        os.makedirs(temp_result_path, exist_ok=True)

        for x in range(len(self.lab_text_files)):
            # Put original files into TXT folder, check for duplicates
            temp_file_name = os.path.join(temp_result_path, os.path.basename(self.lab_text_files[x]))
            silent_remove(temp_file_name)
            shutil.copy2(self.lab_text_files[x], temp_result_path)

            # Create new name in "Date Method Batch Lab" format
            date = get_date(self.lab_text_files[x])
            old_file_name = file_name_regex(os.path.basename(self.lab_text_files[x]))
            if date and old_file_name:
                unique_file_name = "{date} {old_file} {lab_name}.txt".format(
                    date=date, old_file=old_file_name, lab_name=self.lab_name)

                unique_path = os.path.join(self.lab_results, os.path.basename(unique_file_name))
                # Checking for duplicate, keeping oldest file discarding new
                if os.path.isfile(unique_path):
                    os.remove(temp_file_name)
                else:
                    os.rename(temp_file_name, unique_path)

        shutil.rmtree(temp_result_path)


def make_month_folders(result_path):
    list_of_files = glob.glob(result_path+'\\*.txt')
    for file in list_of_files:
        file_name = os.path.basename(file)
        # Slice just the portion of file name where month designation resides
        month_digits = file_name[4:6]
        if month_digits.startswith('0') or month_digits.startswith('1'):
            if month_digits.startswith('0'):
                month_digits = month_digits[1]
            try:
                month_name = calendar.month_name[int(month_digits)]
            except IndexError:
                raise SystemExit("Index Error")

            year = file_name[:4]
            month_folder_name = '{month_name} {year}'.format(month_name=month_name, year=year)
            month_folder = os.path.join(result_path, month_folder_name)
            os.makedirs(month_folder, exist_ok=True)
            # Move into months folders
            try:
                shutil.move(file, month_folder)
            # If file exists in month folder, delete it and keep old
            except shutil.Error:
                os.remove(file)


# Gets date from 'Original Filename' field
#  that was created from last cell in original text file
def get_date(text_file):
    with open(text_file, 'r') as original_file:
        row = original_file.readlines()[-1].split('\t')
        file_name = os.path.basename(row[2])[:8]
        return file_name


# Gets Unique portion of original file name to append to date file
def file_name_regex(base_name):
    base_name = base_name.strip()
    unique_name = re.findall('^[A-Z]+\s*[A-Z]+-[0-9]+', base_name)
    if unique_name:
        return ' '.join(unique_name[0].split())


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred


def merge_txt_to_csv(path_to_directory):
    """ Takes list of files from directory, makes data file new each time and
    sets designated header values.
    On first run this will make a new data file and begin to append relevant fields from all other
    txt files in folder"""
    list_of_files = glob.glob(os.path.join(path_to_directory, '*.txt'))
    out_csv_file = os.path.join(path_to_directory, 'data.csv')
    silent_remove(out_csv_file)
    out_csv = csv.writer(open(out_csv_file, 'a', newline=''))
    # Open first file in list, take first row to obtain header values
    headers_in_file = next(csv.reader(open(list_of_files[0], 'rt'), delimiter='\t'))
    # Set all header values for fields
    sample_name = headers_in_file[headers_in_file.index('Sample Name')]
    component_name = headers_in_file[headers_in_file.index('Component Name')]
    concentration = headers_in_file[headers_in_file.index('Calculated Concentration')]
    headers = [component_name, sample_name, concentration, 'Date']
    out_csv.writerow(headers)

    for files in list_of_files:
        """ in_file uses a list because we need the very last date to copy for each entry
            otherwise using next() would be more memory efficient.  Tested using next()
            and reseting the iterator back to 0 with file.seek(0) to get the row data.
            Making list : 13.1s Max of 130 mb memory usage
            Using next(): 18.5s Max of 65 mb memory usage
            Would consider switching to next() in future if file size becomes an issue.
            Rough maximal file size currently: 27 mb"""
        in_file = list(csv.reader(open(files, 'rt'), delimiter='\t'))
        for rows in in_file:
            # Looking for only low and high QC data points. Taking only first transitions
            # which are indicated with a 1 at the end
            if rows[in_file[0].index('Sample Name')] in ('Low QC', 'HIgh QC') and \
                    rows[in_file[0].index('Component Name')].endswith('1'):
                # Setting values in same manner that header was set
                component_name = rows[in_file[0].index('Component Name')]
                sample_name = rows[in_file[0].index('Sample Name')]
                concentration = rows[in_file[0].index('Calculated Concentration')]
                date_name = (os.path.basename(in_file[1][in_file[0].index('Original Filename')])[:8])
                date_formatted = str(pd.to_datetime(date_name, format='%Y%m%d').date())
                date_final = datetime.datetime.strptime(date_formatted, '%Y-%m-%d').strftime('%m-%d-%y')
                values = [component_name, sample_name, concentration, date_final]
                out_csv.writerow(values)


def walk_months(results_directory):
    directories = next(os.walk(results_directory))[1]

    for subdirectories in directories:
        month_directory = os.path.join(results_directory, subdirectories)
        if os.listdir(month_directory) != []:
            merge_txt_to_csv(month_directory)


def get_home():
    if hasattr(sys, 'frozen'):
        return os.path.dirname(sys.executable)
    else:
        return os.path.dirname(sys.argv[0])


def generate_data(lab_value):
    lab = LeveyJennings(lab_value)
    lab.make_unique_files()
    make_month_folders(lab.lab_results)
    walk_months(lab.lab_results)


