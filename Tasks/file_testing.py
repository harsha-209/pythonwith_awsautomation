import os
import sys

#file_name = input("please enter file name ")
path_name = input("please enter path name ")

if os.path.exists(path_name):
    print("your path exists")
else:
    sys.exit()



for each_object in os.listdir(path_name):
    list_files = os.path.join(path_name,each_object)
    #print(os.path.isfile(list_files))
    if os.path.isfile(list_files):
        print(list_files)
    else:
        print("these are directorys{}".format(list_files))
