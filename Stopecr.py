import boto3

def stop_all_running_instances():
    ec2 = boto3.client("ec2")
    
    response = ec2.describe_instances()
    
    for reservation in response["Reservations"]:
        for instance in reservation["Instances"]:
            if instance["State"]["Name"] == "running":
                instance_id = instance["InstanceId"]
                print(f"Stopping {instance_id}")
                ec2.stop_instances(InstanceIds=[instance_id])

stop_all_running_instances()
