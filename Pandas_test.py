import pandas as pd
import numpy as np
import os
import datetime
import calendar
import csv

file_name = r'D:\Coding\Python\TestFiles\Results\B3\6 June 2016\20160624 PP BH-649 B3.txt'

def merge_txt_to_csv(directory_list):
    in_text = list(csv.reader(open(file_name, 'rt'), delimiter='\t'))
    out_csv_file = r'D:\Coding\Python\TestFiles\Results\B3\6 June 2016\test.csv'
    print(in_text[0])

    original_filename = in_text[0][in_text[0].index('Original Filename')]
    sample_name = in_text[0][in_text[0].index('Sample Name')]
    component_name = in_text[0][in_text[0].index('Component Name')]
    concentration = in_text[0][in_text[0].index('Calculated Concentration')]

    headers = [original_filename, sample_name, component_name, concentration]
    print(in_text[0].index('Sample Name'))
    out_file_opened = csv.writer(open(out_csv_file, 'a', newline=''))
    out_file_opened.writerow(headers)
    
    for rows in in_text:
        if rows[in_text[0].index('Sample Name')] in ('Low QC', 'HIgh QC'):
            out_file_opened.writerow([rows[in_text[0].index('Sample Name')]])

        # elif 'HIgh QC' in rows[in_text[0].index('Sample Name')]:
        #     out_file_opened.writerow([rows[in_text[0].index('Sample Name')]])

