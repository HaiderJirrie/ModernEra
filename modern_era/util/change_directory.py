import os

def change_working_dir(path):
    target_dir = os.path.dirname(path)
    os.chdir(target_dir)