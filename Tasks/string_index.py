import os
import string

please_enterkey  = input("please enter a string ")

index = 0
#print(please_enterkey.index(please_enterkey))

for each_key in please_enterkey:
    print("{} ---->{}".format(each_key,index))
    index = index+1   