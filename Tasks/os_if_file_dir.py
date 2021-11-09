import os
import sys

path_name = input("please enter required path ")

if os.path.exists(path_name):
    print(" yes path exists")
else:
    sys.exit()

#print(os.listdir(path_name))
for each_object in os.listdir(path_name):
    #print(each_object)
    if os.path.isfile(each_object):
        print("these below listed are files and file name is {}".format(each_object))
        #print(each_object)
    else:
        print("these are directorys and director name is {}".format(each_object))
        #print(each_object)