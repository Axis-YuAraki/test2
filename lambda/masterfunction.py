import json
import boto3

lambda_client = boto3.client('lambda')
s3 = boto3.resource('s3')
filepath = ''

Bucket_name = 'test-shikano'
ObJeCT_KEY_NAME = 'result.html'

def lambda_handler(event, context):

    event["number"] *= 5

    response = lambda_client.invoke(

        FunctionName='calculateprime',
        InvocationType='RequestResponse', 
        Payload=json.dumps(event)
        
    )
    result = json.load(response['Payload'])

    return {
        'statusCode': 200,
        'body': json.dumps({
            'Lambda': result,
        })
    }
