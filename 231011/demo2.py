#Full scanning

import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-2', 
                          aws_access_key_id='', 
                          aws_secret_access_key='')
table = dynamodb.Table('Movies')

results = table.scan()
# print(type(results)) #dict
# print(results.keys()) 'Items', 'Count', 'ScannedCount', 'ResponseMetadata'
# print(results['Count']), results['ScannedCount']
items = results['Items']
for i in range(len(items)) :
    print(items[i])