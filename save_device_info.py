
import boto3
import requests


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    l = boto3.client('lambda')



    l.update_function_code(
        FunctionName="check_device_info",
        S3Bucket="forevent",
        S3Key="save_device_info"
    )


    return ('test trigge!!dsadsdfsdfsdfsdfr')
