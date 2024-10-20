import json
from datetime import datetime, timedelta
from noaa_sdk import NOAA


def get_weather(zipcode, country, period):
    #timeframe
    endDate = datetime.now() #today
    startDate = endDate - timedelta(days=period)
    n = NOAA()
    obs = n.get_observations(zipcode, country, start=startDate.strftime('%Y-%m-%d'), end=endDate.strftime('%Y-%m-%d'))
    
    return list(obs)

def handler(event, context):
    
    try:
        #ws stands for weather stuff
        ws = event.get('weatherStuff',{})
        zipcode = ws.get('zipcode')
        country = ws.get('country')
        period = int(ws.get('period', 7))
        
        wData = get_weather(zipcode, country, period)
        
        return {'statusCode': 200,'body': json.dumps({'message': f' {zipcode}, {country}, {period} test.', 'dataLength' : len(wData)})}
        
    except Exception as e:
        
        return {'statusCode':500,'body': json.dumps({'error':str(e)})}
        

#test
test_event = {'weatherStuff': {'zipcode':'30350', 'country':'US', 'period':'7'}}
result = handler(test_event, {})
print(result)
assert result['statusCode'] == 200
assert json.loads(result['body'])['dataLength'] > 0
print('weather fetched successfully')