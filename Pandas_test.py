import pandas as pd
import numpy as np
import os
import datetime
import calendar
import csv

file_name = r'D:\Coding\Python\TestFiles\Results\B3\6 June 2016\20160624 PP BH-649 B3.txt'

in_text = list(csv.reader(open(file_name, 'rt'), delimiter='\t'))
out_csv_file = r'D:\Coding\Python\TestFiles\Results\B3\6 June 2016\test.csv'
print(in_text[0])

# if ('Low QC' or 'HIgh QC') in in_text[1000][3]:
#     print('found')
#     print(in_text[1000][3])
# else:
#     print('not found')

out_csv = csv.writer(open(out_csv_file, 'wt'))

original_filename = in_text[0][in_text[0].index('Original Filename')]
sample_name = in_text[0][in_text[0].index('Sample Name')]
component_name = in_text[0][in_text[0].index('Component Name')]
concentration = in_text[0][in_text[0].index('Calculated Concentration')]

print(sample_name)
# out_csv.writerow([test_var])
