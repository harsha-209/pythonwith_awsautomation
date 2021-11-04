import boto3

ec2_con = boto3.client('ec2')

response = ec2_con.run_instances(
    BlockDeviceMappings=[
        {
            'DeviceName': '/dev/sdh',
         #   'VirtualName': 'string',
            'Ebs': {
                'DeleteOnTermination': True,
#                'Iops': 100,
                'VolumeSize': 8,
                'VolumeType': 'gp2',
                'Encrypted': False
            },
        },
    ],
    ImageId='ami-041db4a969fe3eb68',
    InstanceType='t2.micro',
#    InstanceType='t1.micro'|'t2.nano'|'t2.micro'|'trge'|'z1d.xlarge'|'z1d.2xlarge'|'z1d.3xlarge'|'z1d.6xlarge'|'z1d.12xlarge'|'z1d.metal'|'u-6tb1.56xlarge'|'u-6tb1.112xlarge'|'u-9tb1.112xlarge'|'u-12tb1.112xlarge'|'u-6tb1.metal'|'u-9tb1.metal'|'u-12tb1.metal'|'u-18tb1.metal'|'u-24tb1.metal'|'a1.medium'|'a1.large'|'a1.xlarge'|'a1.2xlarge'|'a1.4xlarge'|'a1.metal'|'m5dn.large'|'m5dn.',
    KeyName='ramcharan',
    MaxCount=1,
    MinCount=1,
    Monitoring={
        'Enabled': False
    },
#    SecurityGroupIds=[
#        'sg-4eb4442b',
#    ],
#    SecurityGroups=[
#        'sg-4eb4442b',
#    ],
#    SubnetId='subnet-b76364df',
#    UserData='string',
 #   IamInstanceProfile={
 #       'Arn': 'string',
 #       'Name': 'string'
 #   },
    NetworkInterfaces=[
        {
            'AssociatePublicIpAddress': True,
            'DeleteOnTermination': True,
            'Description': 'my instance',
            'DeviceIndex': 0,
            'Groups': [
                'sg-4eb4442b'
            ],
            'SubnetId':'subnet-b76364df'
        },
    ],
    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'harshad'
                },
            ]
        },
    ]
#    LaunchTemplate={
#        'LaunchTemplateName': 'pythoninstancetemplate'
#    }
)


print(response)
