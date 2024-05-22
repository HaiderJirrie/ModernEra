import sys, os, pefile

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

    #TO DO: create function that goes through the imports to determine which exploits are possible

def staticAnalysis():
    print("Analysing PE Imports")

    pe =  pefile.PE(target_path)
    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        if entry.dll.decode('utf-8').lower() == 'msvcrt.dll':
            print(f"{entry.dll.decode('utf-8')}:")
            for imp in entry.imports:
                print(f"\t{imp.name.decode('utf-8') if imp.name else str(imp.ordinal)}")  

# Call the functions
validatePath()
staticAnalysis()
