import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
from pathlib import Path
import os
import sys
import matplotlib.ticker as ticker

def make_graph(data_csv):
    data = pd.read_csv(data_csv, encoding='utf-8-sig', low_memory=False)
    df = pd.DataFrame(data)
    # pd.set_option('display.float_format', lambda x: '%.2f' % x)
    # df['Date'] = pd.to_datetime(df['Date'])
    # , format='%m-%d-%y').dt.strftime('%m-%d-%y')

    df.sort_values(['Component Name', 'Sample Name'], inplace=True)
    df.drop_duplicates(['Component Name', 'Sample Name', 'Date'], inplace=True)
    some_values = ['< 0']
    df['Calculated Concentration'].fillna('< 0', inplace=True)
    list_of_na = df.loc[df['Calculated Concentration'].isin(some_values)]
    if list_of_na.empty:
        df['Calculated Concentration'] = df['Calculated Concentration'].astype(float)
    else:
        path_to_na = Path(data_csv).parents[0]
        na_out_csv = os.path.join(str(path_to_na), 'NA_values.csv')
        list_of_na.to_csv(na_out_csv)
        print('NA')
        sys.exit(0)

    grouped = df.groupby(['Component Name', 'Sample Name'])

    list_of_drugs = sorted(list(set(df['Component Name'])))

    for drugs in list_of_drugs:
        low_qc = grouped.get_group((drugs, 'Low QC'))
        x = low_qc['Date']
        x_range = len(x)
        x_values = np.arange(x_range)
        y = low_qc['Calculated Concentration']
        plt.xlim(np.amin(x_values)-1, np.amax(x_values)+1)
        plt.xticks(x_values, x, rotation='vertical')
        plt.plot(x_values, y, '-bo')
        plt.show()
        sys.exit(0)



make_graph(r'D:\Coding\Python\TestFiles\Results\ADV\June 2016\data.csv')