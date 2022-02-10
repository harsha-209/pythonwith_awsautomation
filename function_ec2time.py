import boto3
import datetime
import pytz

######## TypeError: can't subtract offset-naive and offset-aware datetimes###
####https://stackoverflow.com/questions/7065164/how-to-make-a-timezone-aware-datetime-object-in-python


today_date = datetime.datetime.now(pytz.UTC)
print(today_date)


ec2_cons = boto3.client('ec2')
response = ec2_cons.describe_instances()


def my_launchtime(instance_creationtime):
    x_dayof_instance = (today_date-instance_creationtime)
    print(x_dayof_instance)
    print("This is instance is created {} days ago".format(x_dayof_instance.days))










for each_instance in response['Reservations']:
    for each_inst in each_instance['Instances']:
        print(each_inst['InstanceId'],each_inst['LaunchTime'])
        instance_creationtime = each_inst['LaunchTime']
        my_launchtime(instance_creationtime)
'''        
        x_dayof_instance = (today_date-instance_creationtime)
        print(x_dayof_instance)
        print("This is instance is created {} days ago".format(x_dayof_instance.days))
'''