import pandas as pd
import numpy as np
import os

file_name = r'D:\Analyst Data\Projects\MPX5 Feb 2016\Data\20160624 NEW PP BH-649.wiff (sample 8)'

print(os.path.basename(file_name)[:8])

with open('D:\Coding\Python\TestFiles\Results\B3\PP BH-649 B3 PB.txt', 'r') as original_file:
        row = original_file.readlines()[1].split('\t')
        file_name = os.path.basename(row[2])[:8]
        print(file_name)
