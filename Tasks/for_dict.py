import os

my_dict = {'a':1,'b':2,'c':3}

print(my_dict['a'])
print(my_dict.get('a'))


for each_value in my_dict.values():
    print(each_value)

for eac_object in my_dict.keys():
    print(eac_object) 

for each_item in my_dict.items():
    print(each_item)