import boto3, dynamodbinfo
# delete item
table = dynamodbinfo.dynamodb.Table('Movies')
table.delete_item(
    Key={
        'Code' : '20050112',
        'Name' : 'Batman Begins'
    }
)