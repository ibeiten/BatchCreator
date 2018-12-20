"""
Read in a list of files by an input file type in a folder and return a list of string file names.
Currently just reads local folder. Option to select folder will be added later.
"""

from pathlib import Path

def files_in_folder(file_extension):
# Returns current directory
    p = Path('.')
# Read in list of files in current directory that have file type file_extension
    a = list(p.glob('*' + file_extension))
    return (a)

# strip_extension isn't currently used but kept for now
def strip_extension(file_list,file_extension):
    file_list = [ str(x).strip(file_extension) for x in file_list]
    return file_list

def convert_glob_to_string(glob_list):
    string_list = [ str(x) for x in glob_list]
    return string_list

def list_of_files_in_subfolder(file_type):
    unstripped_list = files_in_folder(file_type)
    final_list = convert_glob_to_string(unstripped_list)
    return(final_list)