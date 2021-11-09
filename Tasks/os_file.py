import os


file_search = input("please enter here your required file to search it ")

print("you entered file name is {}".format(file_search))

#print(os.listdir())

current_path = os.getcwd()

if file_search in os.listdir():
    print("yes your required file is in current path")
    print("current path is {}".format(current_path))
