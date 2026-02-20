import boto3
from datetime import datetime

ec2 = boto3.client("ec2")

response = ec2.describe_instances()

for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        if instance["State"]["Name"] == "running":
            for volume in instance["BlockDeviceMappings"]:
                volume_id = volume["Ebs"]["VolumeId"]
                
                snapshot = ec2.create_snapshot(
                    VolumeId=volume_id,
                    Description=f"Backup-{datetime.now()}"
                )
                
                print(f"Snapshot created for {volume_id}")
