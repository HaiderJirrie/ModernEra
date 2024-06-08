import sys
import os

def get_valid_path():
    path = ''

    if len(sys.argv) < 2:
        print("Please provide a PE file")
        path = input().replace("\"", "")
    else:
        path = sys.argv[1]

    if not os.path.isfile(path):
        print("File not found")
        sys.exit()

    print("Target located")
    return path