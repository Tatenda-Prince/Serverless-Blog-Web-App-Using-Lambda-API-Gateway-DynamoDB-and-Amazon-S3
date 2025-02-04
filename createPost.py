import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def lambda_handler(event, context):
    # Scan the table to get all posts
    response = table.scan()
    items = response['Items']

    return {
        'statusCode': 200,
        'body': json.dumps(items)
    }
