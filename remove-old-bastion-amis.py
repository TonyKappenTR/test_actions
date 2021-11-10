"""
This script unregisters and deletes old bastion amis and their associated snapshots
"""
import boto3
# import datetime
import json
# import os
# datestring = '%Y-%m-%dT%H:%M:%S.%fZ'
# DELTA=datetime.timedelta(days=90)
# TODAY=datetime.datetime.today()
# DRY_RUN=True
# CR_LAMBDA_ARN = "arn:aws:lambda:us-east-1:460300312212:function:a205257-aws-dashboard-create-change-request"
# EMPLOYEE_ID="6112649"
# TR_ENTERPRISE_CICD_PROD="460300312212"
# TR_ENTERPRISE_CICD_NON_PROD="142227596713"
# ENV = os.environ.get('ENV')

#TEST invoking a lambda
lambda_client = boto3.client('lambda')
payload={
    "test":True
}
response = lambda_client.invoke(
    FunctionName='arn:aws:lambda:us-east-1:142227596713:function:a205257-testing',
    Payload=bytes(json.dumps(payload),'utf-8')
)
body = json.loads(response['Payload'].read().decode('utf-8'))
print(body)
client = boto3.client('ec2',region_name='us-east-1')
# def create_change_request():
#     account_number=""
#     if ENV == 'prod':
#         account_number=TR_ENTERPRISE_CICD_PROD
#     else:
#         account_number=TR_ENTERPRISE_CICD_NON_PROD
#     payload= {
#         "employee_id": "6112649",
#         "account_number": account_number,
#         "region": False,
#         "environment": ENV,
#         "zone": False
#     }
#     lambda_client = boto3.client('lambda')
#     response = lambda_client.invoke(
#         FunctionName=CR_LAMBDA_ARN,
#         InvocationType="RequestResponse",
#         Payload=bytes(json.dumps(payload))
#     )
#     body = json.loads(response['Payload'].read().decode('utf-8'))
#     if "errorType" not in body:
#         print(f"CREATED CHANGE REQUEST {body['cr_number']}")
#         return body['cr_number']
#     else:
#         print("FAILED TO CREATE CHANGE REQUEST")
# def close_change_request(cr):
#     payload= {
#         "cr_number": cr
#     }
#     lambda_client = boto3.client('lambda')
#     response = lambda_client.invoke(
#         FunctionName=CR_LAMBDA_ARN,
#         InvocationType="RequestResponse",
#         Payload=bytes(json.dumps(payload))
#     )
#     body = json.loads(response['Payload'].read().decode('utf-8'))
#     if "errorType" not in body:
#         print("CLOSED CHANGE REQUEST")
#     else:
#         print("FAILED TO CLOSE CHANGE REQUEST")
# def get_regions():
#     ami_regions = ''
#     if ENV == 'prod':
#         ami_regions = json.load(open('variables-prod.json','r'))['ami_regions']
#     else:
#         ami_regions = json.load(open('variables-dev.json','r'))['ami_regions']
#     regions = ami_regions.split(',')
#     return regions
# def describe_images(ec2):
#     args = {
#         "Filters":[
#             {
#                 "Name":"tag:tr:application-asset-insight-id",
#                 "Values":["205257"]
#             },
#         ],
#     }
#     s = []
#     while True:
#         r = ec2.describe_images(
#             **args
#         )
#         s += r['Images']
#         if 'NextToken' in r:
#             args['NextToken'] = r['NextToken']
#         else:
#             break
#     return s
# def get_associated_snapshots(image):
#     snaps=[]
#     for block in image['BlockDeviceMappings']:
#         snaps.append(block.get('SnapshotId'))
#     return snaps
# def delete_old_amis_and_snapshots(ec2):
#     images = describe_images(ec2)
#     for image in images:
#         creation_date = datetime.datetime.strptime(image['CreationDate'],datestring)
#         if 'tr-bastion' in image['Name'] and creation_date < TODAY - DELTA:
#             ec2.deregister_image(
#                 ImageId=image['ImageId'],
#                 DryRun=DRY_RUN
#             )
#             snapshots = get_associated_snapshots(image)
#             for snapshot in snapshots:
#                 ec2.delete_snapshot(
#                     SnapshotId=snapshot['SnapshotId'],
#                     DryRun=DRY_RUN
#                 )
# if __name__=='__main__':
#     cr = create_change_request()
#     regions = get_regions()
#     for region in regions:
#         ec2 = boto3.client('ec2',region=region)
#         delete_old_amis_and_snapshots(ec2)
#     close_change_request(cr)