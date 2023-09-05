import boto3


aws_access_key = '56528769'
aws_secret_key = 't437743'
aws_region = 'US East (N. Virginia)'  

ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=aws_region)
instance_params = {
    'ImageId': 'ami-065681da47fb4e433', 
    'InstanceType': 't3.micro',           
    'KeyName': 'assignment',           
    'SecurityGroupIds': ['sg-0afaee8e1446b1bf1'], 
    'SubnetId': 'subnet-04d925ca4fbee6aa7',             
    'MinCount': 1,
    'MaxCount': 1
}

response = ec2.run_instances(**instance_params)

instance_id = response['Instances'][0]['i-01b7cfdb034e46024']

print(f"Launched EC2 instance with ID: {instance_id}")
