import boto3, dynamodbinfo
#delete table
table = dynamodbinfo.dynamodb.Table('Movies')
table.delete()