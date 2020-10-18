import json
import os
import boto3

def lambda_handler(event, context):
    for record in event['Records']:
        if 's3' in record:
            s3 = boto3.client('s3')
            print(record)
        else:
            raise Exception(
                'ERROR[{0}]: invalid input data. exit'.format(os.getpid()))
