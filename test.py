from distutils.log import debug
import boto3

myclient=boto3.client('ec2', region_name="ap-northeast-3")

def create_custom_vpc():
    response = myclient.create_vpc(
        CidrBlock='192.168.0.0/16',
        # AmazonProvidedIpv6CidrBlock=True,
        # Ipv6Pool='string',
        # Ipv6CidrBlock='string',
        # DryRun=True|False,
        InstanceTenancy='dedicated',
        TagSpecifications=[{
                                               'ResourceType':'vpc',
                                               'Tags': [{
                                                   'Key':'Name',
                                                   'Value':'Test_Vpc'
                                               }]
                                           }]
        # Ipv6CidrBlockNetworkBorderGroup='string'
    )
    print(response)
    vpc_id=response['Vpc']["VpcId"]
    print(vpc_id,"hello==>")
    return vpc_id

# y = create_custom_vpc()
# print(y)

def create_custom_subnet(y):  
    try:
        response = myclient.create_subnet(TagSpecifications=[
            {
                'ResourceType': 'subnet',
                'Tags': [{
                    'Key': 'Name',
                    'Value': 'Test_Subnet'
                }]
            },
        ],
        VpcId=y,
        CidrBlock='192.168.10.0/28'

        )
    except Exception as err:
        print(err)
# z= create_custom_subnet(y)

def create_ec2():
    myclient.run_instances(
            ImageId="ami-096d800410995ae84",
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
if __name__ == '__main__':
    
    y = create_custom_vpc()
    create_custom_subnet(y)
    create_ec2()