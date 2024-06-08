import os

def change_working_dir(target_path):
    target_dir = os.path.dirname(target_path)
    os.chdir(target_dir)