
new_file=open("harshad.txt",'w')
new_file.write("hi world harshad")
new_file.close()


append_file=open("harshad.txt",'a')
append_file.write("\n")
append_file.write("this is not harsha call he him as sai")
append_file.close()


read_file=open("harshad.txt",'r')
data=read_file.read()
read_file.close()


print(data)
newsplitlines = data.splitlines()
print(newsplitlines)
print(newsplitlines[0])
print(type(data))
print(type(newsplitlines))

