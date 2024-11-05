from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
from noaa_sdk import NOAA

app = Flask(__name__)
CORS(app)

@app.route('/weather', methods=['POST'])
def get_weather():
    try:
        data = request.json
        zipcode = data['zipcode']
        country = data['country']
        period = int(data['period'])
        
        endDate = datetime.now()
        startDate = endDate - timedelta(days=period)
        
        n = NOAA()
        obs = n.get_observations(
            zipcode,
            country,
            start=startDate.strftime('%Y-%m-%d'),
            end=endDate.strftime('%Y-%m-%d')
        )
        
        tempData = []
        humidityData = []
        descriptions = []
        
        for o in obs:
            if o['temperature']['value'] is not None:
                tempData.append(o['temperature']['value'])
            if o['relativeHumidity']['value'] is not None:
                humidityData.append(o['relativeHumidity']['value'])
            descriptions.append(f"{o['timestamp']}: {o['textDescription']}")
        
        weatherStuff = f"Weather for {zipcode}, {country}\n"
        weatherStuff += f"From {startDate.strftime('%Y-%m-%d')} to {endDate.strftime('%Y-%m-%d')}\n"
        weatherStuff += f"Latest conditions:\n{descriptions[-1] if descriptions else 'No data'}"
        
        return jsonify({
            'weatherData': weatherStuff,
            'temperatureData': tempData,
            'humidityData': humidityData
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)