import os
import sys
file_name = input("please enter file name here ")

path_name = input("please enter path name here ")

#######################3 checking path exist or not################
if os.path.exists(path_name):
    print("yes path exists")
else:
    sys.exit()

############################# checking specific file exists in current path###############

if file_name in os.listdir(path_name):
    print("file exists")
    print(os.path.join(path_name,file_name))
else:
    print("sorry what you are searching for that file is not present in this path")
