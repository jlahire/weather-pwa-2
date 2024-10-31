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
                console.log('Humidity data:', data.humidityData);} 
                else {resultsDiv.textContent = `Error: ${data.error || 'could not fetch weather data'}`;}
            } 
        catch (error) {resultsDiv.textContent = `Error: ${error.message}`;console.error('eather fetch error:', error);}
    });
});


console.log("test #2 api attempt");