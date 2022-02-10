

my_list=[1,2,3,4,5]

#print(my_list)


try:
    print(my_list[6])
except Exception as e:
    print("error because",e)
    print(e)