import json
import boto3
from uuid import uuid4

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('BlogPosts')

def lambda_handler(event, context):
    # Parse the request body
    body = json.loads(event['body'])
    post_id = str(uuid4())
    title = body['title']
    content = body['content']

    # Insert into DynamoDB
    table.put_item(Item={
        'PostID': post_id,
        'Title': title,
        'Content': content
    })

    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'Post created successfully!'})
    }
