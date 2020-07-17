import json
import base64
import boto3

def handle(event, context):

    source_text = event['SourceText']
    translated_text = event['TranslatedText']
    target_language_code = event['TargetLanguageCode']
    target_language_voice_id  = event['VoiceId']
    access_key = event['AWSCredentials']['AccessKey']
    secret_key = event['AWSCredentials']['SecretKey']

    polly_client = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='us-east-1').client('polly')
       
    response = polly_client.synthesize_speech(VoiceId=target_language_voice_id,
                    OutputFormat='mp3', LanguageCode=target_language_code,
                    Text = translated_text)
    
    context.put(target_language_code + '.mp3', base64.b64encode(response['AudioStream'].read()).decode("utf-8"))
    
    return_json = { 'Translation' : translated_text }
    return return_json
