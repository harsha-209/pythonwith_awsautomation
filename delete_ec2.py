import boto3

ec2_con = boto3.client('ec2')

specific_instacetags = {'Name': 'tag:Name','Values': ["harshad"]}

response = ec2_con.describe_instances(Filters=[specific_instacetags])
delete_instanceid = response['Reservations'][0]['Instances'][0]['InstanceId']


###########################3 terminate a instance ##################################

terminate_instance =  ec2_con.terminate_instances(
    InstanceIds=[
        delete_instanceid
    ]
)


print(terminate_instance)
