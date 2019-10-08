import cx_Freeze
import sys
import pandas
import tkinter
import win32print
import docx
import win32api
import os
import numpy
import tempfile

print("a")

os.environ['TCL_LIBRARY'] = r'C:\Users\Shantanu Shinde\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\Shantanu Shinde\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'

base = None

if sys.platform == 'win32':
    base = "Win32GUI"

print("a")
executables = [cx_Freeze.Executable("LC maker.py", base=base)]
print("a")

cx_Freeze.setup(
    name = "Lc maker",
    options = {"build_exe": {"packages":["numpy","tkinter","pandas","win32print","docx","win32api","tempfile"],
                             "include_files":["lc.py","mkmany.py","lc.docx","op.docx","tcl86t.dll", "tk86t.dll","dbaa.csv","lc - Copy.docx"]}},
    version = "0.01",
    description = "LC Maker",
    executables = executables
    )

print("ab")
