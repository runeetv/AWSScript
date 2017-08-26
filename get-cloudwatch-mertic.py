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
