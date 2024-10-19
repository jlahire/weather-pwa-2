import json
from datetime import datetime, timedelta

def handler(event, context):
    return {
        'statusCode': 200,
        'body': json.dumps({'message': 'hello world'})
    }

#test
test_event = {'httpMethod': 'GET'}
result = handler(test_event, {})
assert result['statusCode'] == 200
assert json.loads(result['body'])['message'] == 'hello world'
print("it works!")