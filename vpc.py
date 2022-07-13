
import logging
import boto3
from botocore.exceptions import ClientError
import json



def create_custom_vpc():
    """
    Creates a custom VPC with the specified configuration.
    """
    try:
        AWS_REGION = 'ap-northeast-3'
        vpc_resource = boto3.resource("ec2", region_name=AWS_REGION)
        ip_cidr='192.168.0.0/16'
        response = vpc_resource.create_vpc(CidrBlock=ip_cidr,
                                           InstanceTenancy='default',
                                           TagSpecifications=[{
                                               'ResourceType':'vpc',
                                               'Tags': [{
                                                   'Key':'Name',
                                                   'Value':'Test_Vpc'
                                               }]
                                           }])
        print(response)
        print("VPC is created")
    except Exception as e:
        print(e)


if __name__ == '__main__':
    create_custom_vpc()