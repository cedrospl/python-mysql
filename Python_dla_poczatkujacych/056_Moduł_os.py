import os
import time

print("Currect directory is:", os.getcwd())

currentDir = os.getcwd()
filename = 'results.txt'
fullpath = os.path.join(currentDir, filename)
print("\nThe constructed file path is: ", fullpath)

relativePath = 'output.txt'
print("\nThe absolute path is: ", os.path.abspath(relativePath))

filepath = r'/home/oem/PycharmProjects/Git repo/Python_dla_poczatkujacych/results.txt'
print("\nThe file name part is: ", os.path.basename(filepath))
print("The directory part is: ", os.path.dirname(filepath))

print("\nIs file existing? ", os.path.exists(filepath))

if os.path.exists(filepath):
    print("\nLast modify date is: ", os.path.getmtime(filepath))
    print("Last modify date is: ", time.localtime(os.path.getmtime(filepath)))

    print("\nFile size is: ", os.path.getsize(filepath))

    print("\nIs it a file? ", os.path.isfile(filepath))
    print("\nIs it a dir? ", os.path.isdir(filepath))

    print("\nPath splitted: ", os.path.split(filepath))
    print("Only file name part: ", os.path.split(filepath) [1])

    print("\nPath splitted into drive: ", os.path.splitdrive(filepath))
    print("Only drive: ", os.path.splitdrive(filepath) [0])

# Moduł os - LAB

#import modułów os i time na górze pliku

dir = input("Please provide a directory path: ")

if not os.path.exists(dir):
    print("%s must be path to directory" % dir)
else:
    file = input("Please provide a filename: ")
    path = os.path.join(dir, file)

    if not os.path.isfile(path):
        print("%s must be a file!" % path)
    else:
        print("Some properties of the file will be displayed below")

        print("Last modification date of the file: ", time.localtime(os.path.getmtime(path)))
        print("Size of the file (in bytes): ", os.path.getsize(path))
        print("Current directory in which this file is: ", os.getcwd())
        print("Relative path to the file: ", os.path.relpath(path))

