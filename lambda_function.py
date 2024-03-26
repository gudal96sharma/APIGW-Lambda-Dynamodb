# lambda_function.py

import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('WeatherData')

def lambda_handler(event, context):
    # Check if id and Weather are in the request body
    if 'id' not in event['body'] or 'Weather' not in event['body']:
        return {
            'statusCode': 400,
            'body': json.dumps('Both "id" and "Weather" must be provided in the request body')
        }

    try:
        d = json.loads(event['body'])
    except KeyError:
        return {
            'statusCode': 400,
            'body': json.dumps('Invalid request body')
        }
    
    # Extract id and weather from the JSON
    id = str(d.get('id', ''))
    weather = str(d.get('Weather', ''))
    # Validate that both id and weather are present
    if not id or not weather:
        return {
            'statusCode': 400,
            'body': json.dumps('Missing id or Weather field in request')
        }

    if len(d) > 2:
        return {
            'statusCode': 400,
            'body': json.dumps('Other field is present in request')
        }
    # Put item into DynamoDB table
    try:
        response = table.put_item(
            Item= {
                'id': id,
                'Weather': weather
            }
        )
        return {
            'statusCode': 200,
            'body': json.dumps('Item added successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps('Error occurred: {}'.format(str(e)))
        }
