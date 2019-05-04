import boto3

client = boto3.client('ec2')

resp = client.describe_instances(Filters=[{
    'Name': 'tag:Env',
    'Values': ['Prod']
}])

for reservation in resp['Reservations']:
    for instance in reservation['Instances']:
        print("InstanceId is {} ".format(instance['InstanceId']))
