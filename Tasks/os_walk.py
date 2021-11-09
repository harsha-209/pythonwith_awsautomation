import os

file_name = input("please enter your file name ")

path = os.walk("/home/minfy/")

for r,d,f in path:
    for each in f:
        if each == file_name:
            #print(each)
            print(os.path.join(r,each))