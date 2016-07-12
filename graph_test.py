import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv(r'D:\Coding\Python\TestFiles\Results\B3\June 2016\data.csv', encoding='utf-8-sig', low_memory=False)
df = pd.DataFrame(data)
pd.set_option('display.float_format', lambda x: '%.2f' % x)
pd.to_datetime(df['Date'], format='%m-%d-%y').dt.strftime('%m-%d-%y')

df.sort_values(['Component Name', 'Sample Name'], inplace=True)
df.drop_duplicates(['Component Name', 'Sample Name', 'Date'], inplace=True)
some_values = ['< 0']
df['Calculated Concentration'].fillna('< 0', inplace=True)
list_of_na = df.loc[df['Calculated Concentration'].isin(some_values)]
if list_of_na.empty:
    print('empty')
else:
    list_of_na.to_csv(r'D:\Coding\Python\TestFiles\Results\B3\June 2016\NA_values.csv')




# df['Calculated Concentration'] = df['Calculated Concentration'].astype(float)

grouped = df.groupby(['Component Name', 'Sample Name'])

list_of_drugs = sorted(list(set(df['Component Name'])))

# alprazolam = grouped.get_group(('Mephedrone 1', 'Low QC'))
#
# # for drugs in list_of_drugs:
# #     print(grouped.get_group((drugs, 'Low QC')))
# #     # print(grouped.get_group((drugs, 'HIgh QC')))
# print(alprazolam)
# date = alprazolam['Date']
#
# conc = alprazolam['Calculated Concentration'].get_values()
#
# print(conc)
