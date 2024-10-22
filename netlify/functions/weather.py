import json
from datetime import datetime, timedelta
from noaa_sdk import NOAA
import asyncio

async def get_weather(zipcode, country, period):
    #timeframe
    endDate = datetime.now() #today
    startDate = endDate - timedelta(days=period)
    n = NOAA()
    obs = await asyncio.to_thread(n.get_observations(zipcode, country, start=startDate.strftime('%Y-%m-%d'), end=endDate.strftime('%Y-%m-%d')))
    
    temp = []
    humidity = []
    descriptions = []
    
    #throwing in 'is not None' and 'if -- else None' statements to prevent ValueErrors
    
    for o in obs:
        if o['temperature']['value'] is not None:
            temp.append(o['temperature']['value'])
        if o['relativeHumidity']['value'] is not None:
            humidity.append(o['relativeHumidity']['value'])
        descriptions.append(f"{o['timestamp']}: {o['textDescription']}")
    hTemp = max(temp) if temp else None
    lTemp = min (temp) if temp else None
    wText = f"Weather stats for zipcode: {zipcode}, in {country}.\n"
    wText += f"Timeframe: {startDate.strftime('%Y-%m-%d')} to {endDate.strftime('%Y-%m-%d')}.\n"
    wText += f"The highest temperature was: {hTemp:.2f}°C\n" if hTemp is not None else "The highest terperature was not recorded.\n"
    wText += f"The lowest temperature was: {lTemp:.2f}°C\n" if lTemp is not None else "The lowest terperature was not recorded.\n"
    #add more weather stuff here eventually
    wText += "Recent NOAA observations:\n"
    wText += "\n".join(descriptions[-5])
    
    return {'weatherData': wText, 'temperatureData': temp, 'humidityData': humidity}


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