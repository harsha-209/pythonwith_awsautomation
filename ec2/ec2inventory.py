import boto3
import csv

ec2_cons = boto3.client('ec2')
count_number = 1
#response = ec2_cons.describe_instances()['Reservations'][0]['Instances']
#print(response[0]['ImageId'])
file_inventory = open("awsinventory.csv","w",newline='')
file_write = csv.writer(file_inventory)

file_write.writerow(["s.no","Instance_id","instance_type","launchtime","privateid","volumeid","instance_state"])

response = ec2_cons.describe_instances()
for each in response['Reservations']:
    for each_value in each['Instances']:
        #print(each_value['InstanceId'],each_value['InstanceType'],each_value['LaunchTime'].date(),each_value['PrivateIpAddress'])
        for each_volumeid in each_value['BlockDeviceMappings']:
            #print(each_volumeid['Ebs']['VolumeId'])
            print(count_number,each_value['InstanceId'],each_value['InstanceType'],each_value['LaunchTime'].date(),each_value['PrivateIpAddress'],each_volumeid['Ebs']['VolumeId'],each_value['State']['Name'])
            file_write.writerow([count_number,each_value['InstanceId'],each_value['InstanceType'],each_value['LaunchTime'].date(),each_value['PrivateIpAddress'],each_volumeid['Ebs']['VolumeId'],each_value['State']['Name']])
            count_number = count_number+1
file_inventory.close()