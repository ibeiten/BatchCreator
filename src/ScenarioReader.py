"""
Open an input batch file, read in valid 'Call' statements, and produce a clean list of files names
"""

def read_scenario_lines(filename):
    with open(filename + ".bat") as f:
        scenario_lines = f.readlines()
    return(scenario_lines)

def keep_valid_lines(input_list):
    no_whitespace = [ x.lstrip() for x in input_list]
    output_list = [ ]
    for line in no_whitespace:
        if line.find("Call ") == 0:
            output_list.append(line)
    return(output_list)

def remove_extra_bits(input_list):
    no_call = [ x.strip("Call PrmFile ") for x in input_list]
    no_linebreak = [ x.strip("\n") for x in no_call]
    return (no_linebreak)

scenario = 'fruits'
initial_list = read_scenario_lines(scenario)
scenario_file_list = keep_valid_lines(initial_list)
clean_list = remove_extra_bits(scenario_file_list)
print(clean_list)
