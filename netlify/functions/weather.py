import json
from datetime import datetime, timedelta

def handler(event, context):
    
    try:
        #ws stands for weather stuff
        ws = event.get('weatherStuff',{})
        zipcode = ws.get('zipcode')
        country = ws.get('country')
        period = ws.get('period')
        
        return {'statusCode': 200,'body': json.dumps({'message': f' {zipcode}, {country}, {period} test.'})}
        
    except Exception as e:
        
        return {'statusCode':500,'body': json.dumps({'error':str(e)})}
        

#test
test_event = {'weatherStuff': {'zipcode':'30350', 'country':'US', 'period':'14'}}
result = handler(test_event, {})
print(result)
assert result['statusCode'] == 200
#assert json.loads(result['body'])['message'] == 'hello world'
print("it works!")