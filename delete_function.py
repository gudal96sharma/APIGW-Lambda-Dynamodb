# delete_function.py

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WeatherData')

def lambda_handler(event, context):
    # Extract id from path parameters
    id = event['pathParameters']['id']

    # Delete item from DynamoDB table
    table.delete_item(Key={'id': id})

    return {
        'statusCode': 200,
        'body': json.dumps('Data successfully deleted from DynamoDB')
    }
