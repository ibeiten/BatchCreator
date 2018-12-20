"""
Use input values to create a new batch file
"""

from FileFinder import list_of_files_in_subfolder

file_type = '.txt'
a = list_of_files_in_subfolder(file_type)
print(a)