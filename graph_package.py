import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import itertools
from pathlib import Path
import os
import sys
import calendar
from data_main import silent_remove
from PyPDF2 import PdfFileReader, PdfFileMerger
import shutil
import glob
plt.style.use('ggplot')


def flip(items, ncol):
    return itertools.chain(*[items[i::ncol] for i in range(ncol)])

"""Make this take a lab name from PYQT since the dictionary is already there
    and add the Lab name to top of graph as well"""


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

    graph_folder = os.path.join(os.path.dirname(data_csv), 'Graphs')
    try:
        shutil.rmtree(graph_folder)
    except FileNotFoundError:
        pass
    os.makedirs(graph_folder)
    """Format date name from first entry to add to graph title"""
    month_digits = df['Date'][0]
    year = '20' + month_digits[-2:]
    if month_digits.startswith('0'):
        month_digits = month_digits[1]
    try:
        month_name = calendar.month_name[int(month_digits)]
    except IndexError:
        raise SystemExit("Index Error")
    month_folder_name = '{month_name} {year}'.format(
        month_name=month_name, year=year
    )
    grouped = df.groupby(['Component Name', 'Sample Name'])

    # list_of_drugs = sorted(list(set(df['Component Name'])))
    # print(grouped.get_group((list_of_drugs[0],)))
    for i in grouped.size().index:
        drug_name = i[0]
        QC = i[1]
        drug_group = grouped.get_group(i)
        y = drug_group['Calculated Concentration']
        x = drug_group['Date']
        x_range = len(x)
        x_values = np.arange(1, x_range+1)

        """Begin to calculate positive and negative standard deviations"""
        x_range_full_line = x_range + 2
        x_values_full_line = np.arange(x_range_full_line)
        y_mean = np.mean(y)
        y_mean_values = np.empty(x_range_full_line)
        y_mean_values.fill(y_mean)

        y_sd = np.std(y)
        y_1_pos_sd_values = np.empty(x_range_full_line)
        y_1_pos_sd_values.fill(y_mean + y_sd)

        y_2_pos_sd_values = np.empty(x_range_full_line)
        y_2_pos_sd_values.fill(y_mean + y_sd * 2)

        y_3_pos_sd_values = np.empty(x_range_full_line)
        y_3_pos_sd_values.fill(y_mean + y_sd * 3)

        y_1_neg_sd_values = np.empty(x_range_full_line)
        y_1_neg_sd_values.fill(y_mean - y_sd)

        y_2_neg_sd_values = np.empty(x_range_full_line)
        y_2_neg_sd_values.fill(y_mean - y_sd * 2)

        y_3_neg_sd_values = np.empty(x_range_full_line)
        y_3_neg_sd_values.fill(y_mean - y_sd * 3)

        plt.xlim(np.amin(x_values)-.5, np.amax(x_values)+.5)
        plt.ylim(y_mean - y_sd * 4, y_mean + y_sd * 4)
        plt.xticks(x_values, x, rotation='vertical')
        plt.title('{month_name} {QC} {drug_name}'.format(month_name=month_folder_name,
                                                         QC=QC, drug_name=drug_name[:-2]))

        """Begin to plot mean and sd values"""
        plt.plot(x_values_full_line, y_mean_values, 'gold', label='Mean')
        plt.plot(x_values_full_line, y_1_pos_sd_values, 'lime', label='1 SD')
        plt.plot(x_values_full_line, y_2_pos_sd_values, color='darkviolet', label='2 SD')
        plt.plot(x_values_full_line, y_3_pos_sd_values, 'darkred', label='3 SD')
        plt.plot(x_values_full_line, y_1_neg_sd_values, 'lime')
        plt.plot(x_values_full_line, y_2_neg_sd_values, color='darkviolet')
        plt.plot(x_values_full_line, y_3_neg_sd_values, 'darkred')

        if QC == 'Low QC':
            plt.plot(x_values, y, color='blue', marker='o')
        else:
            plt.plot(x_values, y, color='red', marker='o')
        plt.legend(ncol=6, fontsize=9,loc='upper center')
        graph_name = '{drug_name} {QC}.pdf'.format(drug_name=drug_name, QC=QC)
        graph_name = graph_name.replace('/', '-')
        plt.savefig(os.path.join(graph_folder, graph_name))
        plt.close()
    combinePDFs(graph_folder)
    delete_all_graphs(graph_folder)


def combinePDFs(path_to_graphs):
    path_to_graphs.encode('unicode_escape')
    try:
        pdf_files = [f for f in os.listdir(path_to_graphs) if f.endswith('pdf')]
        merger = PdfFileMerger()
        for filename in pdf_files:
            merger.append(PdfFileReader(os.path.join(path_to_graphs, filename), 'rb'))
        merger.write(os.path.join(path_to_graphs, 'Levey-Jennings Graphs.pdf'))
    except OSError as exception:
        raise exception.errno


def delete_all_graphs(path_to_graphs):
    list_of_files = glob.glob(os.path.join(path_to_graphs, '*.pdf'))
    for files in list_of_files:
        if files != os.path.join(path_to_graphs, 'Levey-Jennings Graphs.pdf'):
            os.remove(files)


make_graph(r'D:\Coding\Python\TestFiles\Results\ADV\June 2016\data.csv')