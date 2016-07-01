import pandas as pd
import numpy as np
import os
import datetime
import calendar
import csv
import glob
from OpenFolders import silent_remove


def merge_txt_to_csv(path_to_directory):
    """ Takes list of files from directory, makes file new each time and sets designated header values"""
    list_of_files = glob.glob(os.path.join(path_to_directory, '*.txt'))
    out_csv_file = os.path.join(path_to_directory, 'data.csv')
    silent_remove(out_csv_file)
    out_csv = csv.writer(open(out_csv_file, 'a', newline=''))
    in_file = list(csv.reader(open(list_of_files[0], 'rt'), delimiter='\t'))

    original_filename = in_file[0][in_file[0].index('Original Filename')]
    sample_name = in_file[0][in_file[0].index('Sample Name')]
    component_name = in_file[0][in_file[0].index('Component Name')]
    concentration = in_file[0][in_file[0].index('Calculated Concentration')]
    headers = [component_name, sample_name, concentration, original_filename]
    out_csv.writerow(headers)
    # out_csv_opened = csv.writer(open(out_csv_file, 'a', newline=''))
    for files in list_of_files:
        for rows in in_file:
            if rows[in_file[0].index('Sample Name')] in ('Low QC', 'HIgh QC') and '1' in \
                    rows[in_file[0].index('Component Name')]:
                component_name = rows[in_file[0].index('Component Name')]
                sample_name = rows[in_file[0].index('Sample Name')]
                concentration = rows[in_file[0].index('Calculated Concentration')]
                date_name = (os.path.basename(rows[in_file[0].index('Original Filename')])[:8])
                date_formated = str(pd.to_datetime(date_name, format='%Y%m%d').date())
                original_filename = datetime.datetime.strptime(date_formated, '%Y-%m-%d').strftime('%m-%d-%y')
                values = [component_name, sample_name, concentration, original_filename]

                out_csv.writerow(values)

correct_path = os.path.normpath(r'D:\Coding\Python\TestFiles\Results\B3\6 June 2016')

merge_txt_to_csv(correct_path)