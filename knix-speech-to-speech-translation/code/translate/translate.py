import json
import boto3

def handle(event, context):
    source_text = event['SourceText']
    target_language_code = event['TargetLanguage']['TargetLanguageCode']
    target_language_voice_id  = event['TargetLanguage']['VoiceId']
    access_key = event['AWSCredentials']['AccessKey']
    secret_key = event['AWSCredentials']['SecretKey']
    
    # create boto3 session
    translate_client = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name='us-east-1').client('translate')

    # call AWS Translate
    result = translate_client.translate_text(Text=source_text,
            SourceLanguageCode="en", TargetLanguageCode=target_language_code)

    # create return value JSON object
    return_json = {}
    return_json['SourceText'] = event['SourceText']
    return_json['TranslatedText'] = result.get('TranslatedText')
    return_json['TargetLanguageCode'] = target_language_code + "-" + target_language_code.upper()
    return_json['AWSCredentials'] = event['AWSCredentials']
    return_json['VoiceId'] = target_language_voice_id

    return return_json
