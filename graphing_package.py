import pandas as pd
import numpy as np


class drugDF(object):
    def __init__(self, file):
        self.file = file

        def createDF(self):
            data = pd.read_csv(self.file, low_memory=False)
            df = pd.DataFrame(data)
            pd.set_option('display.float_format', lambda x: '%.2f' % x)
            return df

        self.df = createDF(self)

        def xValue(self):
            return self.df['Temp']

        def yValue(self):
            self.df.columns = pd.Series(self.df.columns).str.replace('/', '-')
            columnNames = list(self.df.columns[1:])
            return columnNames

        self.x = xValue(self)
        self.y = yValue(self)

    def makeQuadPlot(self, find_dir):
        x = self.x
        y = self.y
        os.makedirs(find_dir, exist_ok=True)
        for i in range(len(y)):
            coefs = poly.polyfit(x, self.df[y[i]], 2)
            x_new = np.linspace(x.min() + 1, x.max(), num=len(x * 10))
            ffit = poly.polyval(x_new, coefs)
            plt.plot(x_new, ffit)
            plt.scatter(x, self.df[y[i]], c='b', label='first')
            plt.xlabel('Temp (F)')
            plt.ylabel('Concentration (nG/mL)')
            plt.title(y[i])
            plt.savefig(find_dir + '\\' + y[i] + '.pdf')
            plt.clf()


def combinePDFs(saveLoc):
    saveLoc.encode('unicode_escape')
    try:
        pdf_files = [f for f in os.listdir(saveLoc) if f.endswith('pdf')]
        merger = PdfFileMerger()
        for filename in pdf_files:
            merger.append(PdfFileReader(os.path.join(saveLoc, filename), 'rb'))
        merger.write(os.path.join(saveLoc, 'CombinedGraphs.pdf'))
    except OSError as exception:
        raise exception.errno

# """Testing Purposes"""
openFile = 'D:\Coding\Python\TestFiles\Results\B3\July 2016\data'
saveLoc = 'D:\Coding\Python\TestFiles\Results\B3\July 2016'
