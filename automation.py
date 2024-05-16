import sys, os
    
def validatePath():
    if sys.argv.__len__() < 2 :
        print("please provide a target file")
        sys.exit()
        
    if not os.path.exists(sys.argv[1]) or not os.path.isfile:
        print("Target file not found")
        sys.exit()

def start():
    validatePath()
        
start()