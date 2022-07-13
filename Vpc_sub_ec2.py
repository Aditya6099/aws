

# sub 192.168.10.0/28 and 192.168.10.2/28

import boto3
# from botocore.exceptions import ClientError

myclient=boto3.client('ec2', region_name="ap-northeast-3")

Ami="ami-096d800410995ae84"
Custom_Vpc="192.168.10.0/24"



vpc_id=myclient.create_vpc(CidrBlock=Custom_Vpc)['Vpc']['VpcId']




myclient.create_subnet(CidrBlock='192.168.10.0/28', VpcId=vpc_id)



myclient.run_instances(
            ImageId=Ami,
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            KeyName="Adi",
            TagSpecifications=
                    [
                        {
                            'ResourceType': 'instance',
                            'Tags': [
                                {
                                    'Key': 'Name',
                                    'Value':"Test_Ec2"
                                },
                            ]
                        },
                    ],
 )