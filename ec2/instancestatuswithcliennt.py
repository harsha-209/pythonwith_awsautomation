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
while True:
    instance_status = ec2_cons.describe_instances(Filters=[filter_custome])['Reservations'][0]['Instances']
    #print(instance_status[0]['State']['Name'])
    if instance_status[0]['State']['Name'] == "running":
        break
    time.sleep(10)
    print("just now you started the instance and it state {}\n".format(instance_status[0]['State']['Name']))
print("now instance status is up and {}\n".format(instance_status[0]['State']['Name']))
