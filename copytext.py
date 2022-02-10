first_file=open("frist.txt",'w')

my_content = ['hi world','where are you']

#print(my_content)


for each in my_content:
    first_file.write(each+"\n")
first_file.close()

read_firstfile=open("frist.txt",'r')
read_data=read_firstfile.read()
read_firstfile.close()

print(read_data)

secondfile=open("second.txt",'w')
secondfile.write(read_data)
secondfile.close()

