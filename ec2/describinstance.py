
import boto3
import datetime


#x = datetime.datetime(2020, 5, 17)
#print(x)

y = datetime.datetime.now().date()

#print(y.strftime("%C"))
print(y)




ec2_cons = boto3.client('ec2')

Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])


#Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'description','Values': ["master"]}])



for pythonins in Myec2['Reservations']:
    for printout in pythonins['Instances']:
#        print(printout['InstanceId'])
#        print(printout['Tags'])
        print("my instance id is :{}\n the instance launch time is {}\n".format(printout['InstanceId'],printout['LaunchTime'].strftime("%y-%m-%d")))
        a = printout['LaunchTime'].date()
        print(a)
        print(y)
        print(type(a))
        print(type(y))
        z = (y - a)
        print(z)
        print("this instance is launched {}\n ago ".format(z)) 

        
        