import boto3
import datetime

#x = datetime.datetime(2020, 5, 17)
#print(x)

y = datetime.datetime.now()

print(y.strftime("%C"))

ec2_cons = boto3.client('ec2')

#Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])


Myec2=ec2_cons.describe_instances()



for pythonins in Myec2['Reservations']:
    for printout in pythonins['Instances']:
#        print(printout['InstanceId'])
#        print(printout['Tags'])
        print("my instance id is :{}\n the instance launch time is {}\n".format(printout['Tags'],printout['LaunchTime']))
        a = print((printout['LaunchTime']))
        print(type(a))
        
       
