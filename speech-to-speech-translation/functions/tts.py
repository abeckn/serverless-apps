import json
import boto3

s3 = boto3.resource('s3')
polly_client = boto3.client('polly')

def lambda_handler(event, context):

    source_text = event['SourceText']
    translated_text = event['TranslatedText']
    target_language_code = event['TargetLanguageCode']
    target_language_voice_id  = event['VoiceId']
       
    response = polly_client.synthesize_speech(VoiceId=target_language_voice_id,
                    OutputFormat='mp3', LanguageCode=target_language_code,
                    Text = translated_text)

    object = s3.Object([bucket name], target_language_code + '.mp3')
    object.put(Body=response['AudioStream'].read())
   
    return_json = { 'Translation' : translated_text }
    return return_json