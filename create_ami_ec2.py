import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'tag:Name','Values': ["master"]}

response = ec2_con.describe_instances(Filters=[specific_instacetags])
delete_instanceid = response['Reservations'][0]['Instances'][0]['InstanceId']

print(delete_instanceid)

###################### create ami for specific instance############################


create_ami = ec2_con.create_image(
    Description='this instance used for production',
    InstanceId=delete_instanceid,
    Name='my_newcustomeami'
)


print(create_ami)

