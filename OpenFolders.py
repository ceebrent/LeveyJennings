import glob
import os
import fnmatch
import tempfile
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

    def silent_remove(self, filename):
        try:
            os.remove(filename)
        except OSError as e:  # this would be "except OSError, e:" before Python 2.6
            if e.errno != errno.ENOENT:  # errno.ENOENT = no such file or directory
                raise  # re-raise exception if a different error occurred

    def data_folder(self, new_directory_path):
        lab_text_files = []
        for dirpath, dirnames, files in os.walk(self.homeDirectory):
            for filename in files:
                if filename.endswith('.txt') and self.lab_name in filename:
                    lab_text_files.append(os.path.join(dirpath, filename))

        for x in range(len(lab_text_files)):
            file_name = os.path.join(new_directory_path, os.path.basename(lab_text_files[x]))
            print(file_name)
            LeveyJennings.silent_remove(self, file_name)
            shutil.copy2(lab_text_files[x], new_directory_path)


"""Testing Purposes"""

# path = 'D:/Coding/Python/TestFiles'
#
# test = LeveyJennings('ADV')
#
# home = test.homeDirectory
# save_results = test.results_folder()
# home_to_data = test.data_folder(save_results)
