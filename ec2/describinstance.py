
import boto3
import datetime
import time

x = datetime.datetime.now()

print(type(x))
print(x)
'''
today_datetime = x.strftime("%Y-%m-%d %H:%M:%S")
print(today_datetime)
print(type(today_datetime))
'''

y = datetime.datetime.now().date()

#print(y.strftime("%C"))
print(y)




ec2_cons = boto3.client('ec2')

Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'instance-type', 'Values': ["t2.micro", "t3.micro"]}])


#Myec2=ec2_cons.describe_instances(Filters=[{'Name': 'description','Values': ["master"]}])



for pythonins in Myec2['Reservations']:
    for printout in pythonins['Instances']:
#        print(printout['InstanceId'])
#        print(printout['Tags'])
        print("my instance id is :{}\n the instance launch time is {}\n".format(printout['InstanceId'],printout['LaunchTime'].strftime("%y-%m-%d")))
        a = printout['LaunchTime'].date()
        '''
        b = printout['LaunchTime'].strftime("%Y-%m-%d %H:%M:%S")
        date_time_obj = datetime.datetime.strptime(b, "%Y-%m-%d %H:%M:%S")
        print(date_time_obj)
        print(type(date_time_obj))
        print(type(b))
        number_of_days = str(x - date_time_obj)
        print('testing')
        print(number_of_days)
        print(number_of_days.strip('days, 6:27:53.638260'))
        '''
        # print(a)
        # print(y)
        # print(type(a))
        # print(type(y))
        z = (y - a)
        #print(z.strftime("%d"))
        instance_created = str(z)
        # print(type(instance_created))
        str_list = instance_created.split(" ")
        print(str_list[0])
        # print(instance_created.strip('days, 0:00:00'))


        print("this instance is launched {}\n ago ".format(z)) 

        
        