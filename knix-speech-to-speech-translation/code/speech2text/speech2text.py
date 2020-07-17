import json
import requests
import base64
from requests.auth import HTTPBasicAuth

def handle(event, context):
    
    # get the recording
    recording = context.get("recording.mp3")
    recording = base64.b64decode(recording)
    
    url = "https://stream-fra.watsonplatform.net/speech-to-text/api/v1/recognize"
    
    # send audio to IBM Watson Speech-to-Text service
    response = requests.post(url=url, data=recording, auth=HTTPBasicAuth('apikey', [apikey value]))
    
    transcript = response.json()['results'][0]['alternatives'][0]['transcript']
    
    return_json = {}
    return_json['SourceText'] = transcript
    return_json['TargetLanguage'] = event['TargetLanguage']
    return_json['AWSCredentials'] = event['AWSCredentials']
    
    return return_json
