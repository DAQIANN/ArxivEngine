import os
import sys

if __name__ == "__main__":
    check = ""
    
    while True:
        check = input ("Enter keywords: ")
        cmd = "python3 searchStart.py " + check
        run = os.system(cmd)
        if check == 'stop':
            break