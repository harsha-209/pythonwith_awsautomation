import boto3
import datetime
import numpy as np

y = datetime.datetime.now().date()

print(y)

ec2_cons = boto3.client('ec2')

#Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])


Myec2=ec2_cons.describe_instances()



for pythonins in Myec2['Reservations']:
    for printout in pythonins['Instances']:
#        print(printout['InstanceId'])
#        print(printout['Tags'])
        print("my instance id is :{}\n the instance launch time is {}\n".format(printout['InstanceId'],printout['LaunchTime'].strftime("%y-%m-%d")))
        a = printout['LaunchTime'].date()
        insta_id = printout['InstanceId']
        print(a)
        print(y)
        print(type(a))
        print(type(y))
        z = (y - a)
      #  print(z.strftime("%d"))
        print(z)
        x = str(z)
        w = int(x[0])
        print(type(w))
        print(w)
        print("this instance is launched {}\n ago ".format(z))
        if w > 10:
            print("we are just starting the instances were, instance age is above 5 days")
            print("the current instance age {}\n".format(z))
            print(insta_id)
            responsed = ec2_cons.start_instances(InstanceIds=[insta_id])
            print(responsed)
 #stop_instances(instance_ids=[my_id])

                       