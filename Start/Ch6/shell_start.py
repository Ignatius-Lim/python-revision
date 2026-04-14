#
# Example file for working with filesystem shell methods
# LinkedIn Learning Python course by Joe Marini
#
import os
from os import path
import shutil
from zipfile import ZipFile

# make a duplicate of an existing file
if path.exists("newfile.txt"):
    # get the path to the file in the current directory
    src = path.realpath("newfile.txt")
        
    # # let's make a backup copy by appending "bak" to the name
    # dst = src + ".bak"

    # # now use the shell to make a copy of the file
    # shutil.copy(src, dst) # shutil.copy2() copies include the ori file metadata

    # # rename the original file
    # os.rename("textfile.txt", "newfile.txt")

    
    # now put things into a ZIP archive
    # root_dir, tail = path.split(src) # The 2 variables will store the 2 values from the tuple
    # shutil.make_archive("archive", "zip", root_dir)

    # more fine-grained control over ZIP files
    # Note: Below code will create a context manager that auto closes when it is done
    with ZipFile("testzip.zip", "w") as newzip: 
        newzip.write("newfile.txt")
        newzip.write("textfile.txt.bak")