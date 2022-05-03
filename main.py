# yolo

import os
import platform

#               What os is in use
if platform.system() == "Linux":
    cl='clear'
if platform.system() == "Windows":
    cl='cls'
if platform.system() == "Darwin":
    cl='clear'

def clear():  
    os.system(cl)