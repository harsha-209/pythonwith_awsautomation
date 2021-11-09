import os
import sys

path_name = input("please enter path name here ")

file_extension = input("please required extension name here ")

if os.path.exists(path_name):
    print("path exists")
else:
    sys.exit()

for each_file in os.listdir(path_name):
    file = os.path.join(path_name,each_file)
    if file.endswith(file_extension):
        print(file)