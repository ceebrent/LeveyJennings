import sys
from cx_Freeze import setup, Executable

includes = ['PyQt4.QtCore', 'sip']
include_files = ['CLMS_Logo_cropped.png']
exe = Executable("main.pyw", base = 'Win32GUI')

setup(
    name = 'Levey Program',
    version = '0',
    description = "Generate data and graph Levey jennings",
    options= {'build_exe': {'includes': includes, 'include_files': include_files}},
    executables = [exe]
)
