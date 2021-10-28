import boto3

ec2_cons = boto3.client('ec2')
count_number = 1
#response = ec2_cons.describe_instances()['Reservations'][0]['Instances']
#print(response[0]['ImageId'])

response = ec2_cons.describe_instances()
for each in response['Reservations']:
    for each_value in each['Instances']:
        print(each_value['InstanceId'],each_value['InstanceType'],each_value['LaunchTime'].date(),each_value['PrivateIpAddress'])
        for each_volumeid in each_value['BlockDeviceMappings']:
            print(each_volumeid['Ebs']['VolumeId'])