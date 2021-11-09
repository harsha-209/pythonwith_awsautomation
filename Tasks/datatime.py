import os
import sys
import datetime

today_date = datetime.datetime.now()
print(today_date)


#file_name = input("please enter file name here ")

file_name = "append.py"

path_name = "/home/minfy/Desktop/pythonwith_awsautomation/Tasks"

for each_file in os.listdir(path_name):
    list_files = os.path.join(path_name,each_file)
    if os.path.isfile(list_files):
        print(list_files)
