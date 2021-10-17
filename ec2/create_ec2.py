import boto3

ec2_cons = boto3.client('ec2')

#Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])


Myec2=ec2_cons.describe_instances()



for pythonins in Myec2['Reservations']:
    for printout in pythonins['Instances']:
#        print(printout['InstanceId'])
#        print(printout['Tags'])
        print("my instance id is :{}\n the instance launch time is {}\n".format(printout['InstanceId'],printout['LaunchTime']))
       








        

#{'Key': 'Name', 'Value': 'workernode'}]