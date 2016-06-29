import re
import os
import shutil
import errno
from pathlib import Path
from home_directory import home_directory


class LeveyJennings(object):
    def __init__(self,lab_name):
        self.homeDirectory = home_directory
        self.lab_name = lab_name

    # Creates and returns folder to store results into
    def results_folder(self):
        move_directory_up = Path(self.homeDirectory).parents[0]
        result_folder = 'Results\\'+self.lab_name
        new_directory_path = os.path.join(str(move_directory_up), result_folder)

        os.makedirs(new_directory_path, exist_ok=True)
        return new_directory_path

    # Walks through all files and directories in home folder with ending text and containing lab name
    def original_txt(self):
        lab_text_files = []
        for dirpath, dirnames, files in os.walk(self.homeDirectory):
            for filename in files:
                if filename.endswith('.txt') and self.lab_name in filename:
                    lab_text_files.append(os.path.join(dirpath, filename))
        return lab_text_files

    def make_unique_files(self, result_path, lab_text_files):
        # Copies all appropriate files into result folder and takes newest version of file
        new_result_path = os.path.join(result_path, 'TXT')
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
            unique_path = os.path.join(result_path, os.path.basename(unique_file_name))
            silent_remove(unique_path)
            os.rename(file_name, unique_path)
            silent_remove(file_name)


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
save_results = test.results_folder()
home_to_data = test.original_txt()
unique_files = test.make_unique_files(save_results, home_to_data)
