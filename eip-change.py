import boto3
import time

instance_id = 'i-2ec725f1'

def lambda_handler(event, context):
    
    client = boto3.client('ec2')
    client.start_instances(
        InstanceIds=[instance_id]
    )
    while True:
        try:
            time.sleep(3)
            response = client.describe_instances(
                InstanceIds=[
                    instance_id,
                ]
            )
            if response['Reservations'][0]['Instances'][0]['State']['Name'] == 'running':
                print 'Instance Started!'
                break
            else:
                print 'In Progress... Current Status: ',str(response['Reservations'][0]['Instances'][0]['State']['Name'])
        except Exception as e:
            print e
   client.associate_address(
        #InstanceId='i-3061339f',
        AllocationId='eipalloc-d17d8fb4',
        NetworkInterfaceId='eni-0a32f072',
        AllowReassociation=True
       )