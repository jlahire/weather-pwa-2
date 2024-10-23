document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('weather-form');
    const resultsDiv = document.getElementById('weather-results');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const zipcode = document.getElementById('zipcode').value;
        const country = document.getElementById('country').value;
        const period = document.getElementById('period').value;
        
        try {
            const response = await fetch ('/api/weather?zipcode=${zipcode}&country=${country}&period=${period}');
            const data = await response.json();
            
            if (response.ok){resultsDiv.textContent = data.weatherData;}
            else { resultsDiv.textContent = 'Error: ${data.error}';}
        }
        catch (error){resultsDiv.textContent = 'Error: ${error.message}';}
    });
});

function createChart(temperatureData, humidityData){



}

console.log("test #4");