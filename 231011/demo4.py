import boto3, dynamodbinfo
#update item
table = dynamodbinfo.dynamodb.Table('Movies')
table.update_item(
    Key={
        'Code' : '20050112', 'Name' : 'Batman Begins'
    },
    UpdateExpression='SET Director = :val', 
    ExpressionAttributeValues = {
        ':val' : 'James Francis Cameron'
    }
)
