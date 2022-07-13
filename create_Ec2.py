import boto3
def create_instance():
    try:
        print("creating Ec2 Instance")
        ec2_client = boto3.client("ec2", region_name="ap-northeast-3")
        instances = ec2_client.run_instances(
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
                                    'Value':"MyEc211111"
                                },
                            ]
                        },
                    ],
        )
        # print(instances["Instances"][0]["InstanceId"])
    except Exception as err:
        print(err)

def describe_ec2():
    try:

        # print("Describing EC2 instances")
        # ec2_client=boto3.client("ec2", region_name="ap-northeast-3")
        # print(ec2_client.describe_instances())


        print("Describing EC2 instances")
        ec2_client=boto3.client("ec2", region_name="ap-northeast-3")
        reservation=ec2_client.describe_instances().get("Reservations")
        print(reservation)
        # for reservation in reservation:
        #     for instance in reservation['Instances']:
        #         print(instance.get("InstanceId"))

    except Exception as err:
        print(err)


# def stop_instance(instance_id):
#     ec2_client = boto3.client("ec2", region_name="ap-northeast-3")
#     response = ec2_client.stop_instances(InstanceIds=[instance_id])
#     print(response)

def terminate_instance(instance_id):
    ec2_client = boto3.client("ec2", region_name="ap-northeast-3")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    print(response)







create_instance()
describe_ec2()
# stop_instance("i-081d565a7f1b63c29")
# terminate_instance("i-00e7f0151fb3c520e")