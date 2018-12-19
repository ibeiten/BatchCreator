from pathlib import Path

def files_in_folder(file_extension):
# Returns current directory
    p = Path('.')
# Read in list of files in current directory that have file type file_extension
    a = list(p.glob('*' + file_extension))
    return (a)

def strip_extension(file_list,file_extension):
    file_list = [ str(x).strip(file_extension) for x in file_list]
    return file_list


file_type = '.txt'
unstripped_list = files_in_folder(file_type)
stripped_list = strip_extension(unstripped_list,file_type)
print(stripped_list)