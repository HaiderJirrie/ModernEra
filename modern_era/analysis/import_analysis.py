from typing import List
from exploits.exploit import Exploit
import pefile

def print_result(functions_list: list, vulnerability_name):
    print(f"\tFound {len(functions_list)} vulnerable {vulnerability_name} functions \n\t({functions_list or "None"})")

def analyse_imports(path, exploits : List[Exploit]):
    print("Analysing PE Imports")

    pe = pefile.PE(path)
    target_entry = 'msvcrt.dll'

    for entry in pe.DIRECTORY_ENTRY_IMPORT:
        if entry.dll.decode('utf-8').lower() == target_entry:
            print(f"{entry.dll.decode('utf-8')}:")
            for imp in entry.imports:
                func_name = imp.name.decode('utf-8') if imp.name else str(imp.ordinal)
                for exploit in exploits:
                    if func_name in exploit.vulnerable_functions:
                        exploit.found_vulnerable_functions.append(func_name)
    
    for exploit in exploits:
        if len(exploit.found_vulnerable_functions) > 0:
            print_result(exploit.found_vulnerable_functions, exploit.name)