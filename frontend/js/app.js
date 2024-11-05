document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('weather-form');
    const resultsDiv = document.getElementById('weather-results');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const zipcode = document.getElementById('zipcode').value;
        const country = document.getElementById('country').value;
        const period = document.getElementById('period').value;
      
        resultsDiv.textContent = `fetching weather data...`;
        try {
            const response = await fetch(`/api/weather`, {
                method: 'POST',
                headers: {'Content-Type': 'application/json',},
                body: JSON.stringify({weatherStuff: {zipcode,country,period}})
            });

            const data = await response.json();
            
            if (response.ok) {resultsDiv.textContent = data.weatherData;
                console.log('Temperature data:', data.temperatureData);
                console.log('Humidity data:', data.humidityData);
                createChart(data.temperatureData, data.humidityData);} 
                
                else {resultsDiv.textContent = `Error: ${data.error || 'could not fetch weather data'}`;}
            } 
        catch (error) {resultsDiv.textContent = `Error: ${error.message}`;console.error('eather fetch error:', error);}
    });
});

function createChart(temperatureData, humidityData){
    const weather = document.getElementById('weather-chart');
    
    if(window.myChart) { window.myChart.destroy();}
    
    window.myChart = new Chart(weather, {type: 'line',data: 
        {labels: temperatureData.map((_, i) => i + 1),datasets: 
            [
                {label: 'Temperature °F',
                data: temperatureData.map(temp => (temp * 9/5) + 32),
                borderColor: 'red'},
                {label: 'Humidity %',
                data: humidityData,
                borderColor: 'blue'}
            ]
        }
    });
}


console.log("test #6");
