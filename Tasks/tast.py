while  True:
    a = eval(input("please enter a number between 1 to 10 "))
    print("you entered a big value than 10 that is {}".format(a))
    if a < 10:
        print("you entered a small value than 10 thanks for your patience ")
        break
print("you entered a correct value small value{}".format(a))
print(a)
if a == 1:
    print("your value is one")
elif a == 2:
    print("your value is two")
elif a == 3:
    print("your value is three")