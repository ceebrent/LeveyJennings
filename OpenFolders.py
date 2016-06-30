import re
import os
import shutil
import errno
from pathlib import Path
from home_directory import home_directory
import calendar
import glob


class LeveyJennings(object):
    def __init__(self, lab_name):
        self.homeDirectory = home_directory
        self.lab_name = lab_name

    # Creates and returns folder to store results into
        def results_folder(self):
            move_directory_up = Path(self.homeDirectory).parents[0]
            result_folder = 'Results\\'+self.lab_name
            lab_results = os.path.join(str(move_directory_up), result_folder)

            os.makedirs(lab_results, exist_ok=True)
            return lab_results
        self.lab_results = results_folder(self)

    # Walks through all files and directories in home folder with ending text and containing lab name
    def original_txt(self):
        lab_text_files = []
        for dirpath, dirnames, files in os.walk(self.homeDirectory):
            for filename in files:
                if filename.endswith('.txt') and self.lab_name in filename:
                    lab_text_files.append(os.path.join(dirpath, filename))
        return lab_text_files

    def make_unique_files(self, lab_text_files):
        # Copies all appropriate files into result folder and takes newest version of file
        new_result_path = os.path.join(self.lab_results, 'Temp_TXT')
        os.makedirs(new_result_path, exist_ok=True)

        for x in range(len(lab_text_files)):
            # Put original files into TXT folder, check for duplicates
            file_name = os.path.join(new_result_path, os.path.basename(lab_text_files[x]))
            silent_remove(file_name)
            shutil.copy2(lab_text_files[x], new_result_path)

            # Create new name in "Date Method Batch Lab format
            date = get_date(lab_text_files[x])
            old_file_name = file_name_regex(os.path.basename(lab_text_files[x]))
            unique_file_name = "{date} {old_file} {lab_name}.txt".format(date=date, old_file=old_file_name,
                                                                         lab_name=self.lab_name)

            unique_path = os.path.join(self.lab_results, os.path.basename(unique_file_name))
            silent_remove(unique_path)
            os.rename(file_name, unique_path)


def make_month_folders(result_path):
    list_of_files = glob.glob(result_path+'\\*.txt')
    for file in list_of_files:
        file_name = os.path.basename(file)
        month_digits = file_name[4:6]
        if month_digits.startswith('0'):
            month_digits = month_digits[1]
        try:
            month_name = calendar.month_name[int(month_digits)]
        except IndexError:
            raise SystemExit("Index Error")

        year = file_name[:4]
        month_folder_name = '{month_number} {month_name} {year}'.format(
            month_number=month_digits, month_name=month_name, year=year
        )
        month_folder = os.path.join(result_path, month_folder_name)
        os.makedirs(month_folder, exist_ok=True)
        # Move into months folders
        try:
            shutil.move(file, month_folder)
        # If file exists in month folder, delete it and add new
        except shutil.Error:
            os.remove(os.path.join(month_folder, os.path.basename(file)))
            shutil.move(file, month_folder)


# Gets date file was created from cell in original text file
def get_date(text_file):
    with open(text_file, 'r') as original_file:
        row = original_file.readlines()[1].split('\t')
        file_name = os.path.basename(row[2])[:8]
        return file_name


# Gets Unique portion of original file name to append to date file
def file_name_regex(base_name):
    base_name = base_name.strip()
    return re.findall('^[A-Z]+\s[A-Z]+-[0-9]+', base_name)[0]


def silent_remove(filename):
    try:
        os.remove(filename)
    except OSError as e:  # this would be "except OSError, e:" before Python 2.6
        if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
            raise  # re-raise exception if a different error occurred

"""Testing Purposes"""

path = 'D:/Coding/Python/TestFiles'

test = LeveyJennings('B3')

home = test.homeDirectory
home_to_data = test.original_txt()
unique_files = test.make_unique_files(home_to_data)
make_month_folders(test.lab_results)
