def addtion(a,b):
    result=(a+b)
    return result  ############### if it none, output will none, so please take of it, you have to get output from donot return NOne

def inputs_addition():
    a=eval(input("please enter a value for a: "))
    b=eval(input("please enter b value for b: "))
    output=addtion(a,b)
    print("hi this is your output {}".format(output))

inputs_addition()