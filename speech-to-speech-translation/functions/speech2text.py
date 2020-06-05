import json
import boto3
from botocore.vendored import requests
from botocore.vendored.requests.auth import HTTPBasicAuth

s3 = boto3.client('s3')

def lambda_handler(event, context):
    
    # get the S3 bucket name and object key that triggered the Step Function execution
    bucket_name = event['detail']['requestParameters']['bucketName']
    file_key = event['detail']['requestParameters']['key']
    
    # get the recording
    recording = s3.get_object(Bucket=bucket_name, Key=file_key)
    
    url = "https://stream-fra.watsonplatform.net/speech-to-text/api/v1/recognize"
    
    # send audio to IBM Watson Speech-to-Text service
    response = requests.post(url=url, data=recording['Body'].read(), auth=HTTPBasicAuth('apikey', [apikey value]))
    
    transcript = response.json()['results'][0]['alternatives'][0]['transcript']
    
    return_json = {}
    return_json['SourceText'] = transcript
    return_json['TargetLanguage'] = event['TargetLanguage']
    
    return return_json