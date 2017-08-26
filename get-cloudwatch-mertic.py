#All sample code is provided for illustrative purposes only. These examples have not been thoroughly tested under all conditions. 
#The owner, therefore, cannot guarantee or imply reliability, serviceability, or function of these programs.

import boto3
import datetime

client = boto3.client('cloudwatch')

response = client.get_metric_statistics(
    Namespace='AWS/EC2',
    MetricName='CPUUtilization',
    Dimensions=[
        {
            'Name': 'InstanceId',
            'Value': 'i-02334'
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



print(response)
