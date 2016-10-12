# LeveyJennings
### Scope and Purpose
Creates LeveyJennings charts dynamically for multiple laboratories from raw HPLC-MS/MS txt data.
(PENDING REFACTOR)

### Packages
PyQt4, NumPy, Matplotlib, Pandas

### General Logic Overview
Multiple .txt files per lab per mass spec are generated and stored in generally accessable folders in the format of:
"Method Batch Lab Name Part-X"

In a specified "Data" subdirectory, all of the folders are recursively searched for any files containing relevant information to the lab and then formatted and appended to their corresponding month for which the samples were processed.

The .txt files are further reduced and post processed to only contain relevant columns used for identification and graphing.

From this point we use a graphing module to create pandas dataframes to do the heavy data analysis and then continue to graph these results using NumPy and matplotlib.

A PyQt4 GUI is used to wrap all of this in an easy to use interface for end users.

Compatible with pyinstaller to compile to a single executable file.

###Changing Lab Names
Lab names can be changed from within the lab_names.json file. Be sure to use appropriate formatting within the json file or the program will fail to read the json data and throw an error.

### Warning / Disclaimer
This program relies on a large amount of I/O from files and it will recursively delete files that are placed into the "Results" directory in order to ensure that all updates from the "Data" directory are current. The "home directory" is automatically set based on the location that the main.py is located, or where the executable is placed.
