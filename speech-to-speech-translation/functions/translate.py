import json
import boto3

translate = boto3.client('translate')

def lambda_handler(event, context):
    source_text = event['SourceText']
    target_language_code = event['TargetLanguage']['TargetLanguageCode']
    target_language_voice_id  = event['TargetLanguage']['VoiceId']
    
    # call AWS Translate
    result = translate.translate_text(Text=source_text,
            SourceLanguageCode="en", TargetLanguageCode=target_language_code)

    # Create return value JSON object
    return_json = {}
    return_json['SourceText'] = event['SourceText']
    return_json['TranslatedText'] = result.get('TranslatedText')
    return_json['TargetLanguageCode'] = target_language_code + "-" + target_language_code.upper()
    return_json['VoiceId'] = target_language_voice_id

    return return_json