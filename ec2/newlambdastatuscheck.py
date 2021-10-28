import json
import boto3
import time

ec2_cons = boto3.client('ec2')
filter_custome = {'Name': 'tag:Name','Values': ['workernode',]}
response = ec2_cons.describe_instances(Filters=[filter_custome])
for each in response['Reservations']:
    for each_value in each['Instances']:
        print(each_value['InstanceId'])
        each_value['InstanceId']
##################### above instance is startin ######################################       
        start_instance = ec2_cons.start_instances(InstanceIds=[each_value['InstanceId']])
##########################################cchecking instance status untill up and running #################################################
ec2_resource = boto3.resource('ec2')
while True:
    instance = ec2_resource.Instance(each_value['InstanceId'])
    #print(instance.state['Name'])
    if instance.state['Name'] == "running":
        break
    time.sleep(5)
    print("please wait instance state is  {}\n".format(instance.state['Name']))
print("your wait-time is over now your instance  state is {}\n".format(instance.state['Name']))

  
      




