#All sample code is provided for illustrative purposes only. These examples have not been thoroughly tested under all conditions. 
#The owner, therefore, cannot guarantee or imply reliability, serviceability, or function of these programs.

import boto3
import datetime
import sys

orig_stdout = sys.stdout
ec2 = boto3.resource('ec2')
client = boto3.client('cloudwatch')

instances = ec2.instances.filter(
    Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:    
    response = client.get_metric_statistics(
        Namespace='AWS/EC2',
        MetricName='CPUUtilization',
        Dimensions=[
            {
                'Name': 'InstanceId',
                'Value': instance.id
            },
        ],
        StartTime=datetime.datetime(2017, 8, 1),
        EndTime=datetime.datetime(2017, 8, 25),
        Period=3600,
        Statistics=[
            'Average'
        ],
        Unit='Percent'
    )
    f = open("C:\\temp\\" + instance.id + ".txt", 'w')
    sys.stdout = f
    print(response)
    #print("Done" + instance.id )

sys.stdout = orig_stdout
f.close()
