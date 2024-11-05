document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('weather-form');
    const resultsDiv = document.getElementById('weather-results');
    const chartCanvas = document.getElementById('weather-chart');
    let weatherChart = null;

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const formData = {
            zipcode: document.getElementById('zipcode').value,
            country: document.getElementById('country').value,
            period: document.getElementById('period').value
        };

        try {
            const response = await fetch('http://localhost:5000/weather', {
                method: 'POST',
                headers: {'Content-Type': 'application/json'},
                body: JSON.stringify(formData)
            });
            const data = await response.json();
            if (response.ok) {resultsDiv.textContent = data.weatherData;createChart(data.temperatureData, data.humidityData);} 
            else {resultsDiv.textContent = `Error: ${data.error}`;}
        } 
        catch (error) {resultsDiv.textContent = `Error: ${error.message}`;}
    });

    function createChart(tempData, humidData) {
        if (weatherChart) {weatherChart.destroy();}
        weatherChart = new Chart(chartCanvas, 
            {type: 'line',data: {labels: Array(tempData.length).fill(''),datasets: [
            {label: 'Temperature (°C)',data: tempData,borderColor: 'red',fill: false},
            {label: 'Humidity (%)',data: humidData,borderColor: 'blue',fill: false}]},
            options: {responsive: true}
        });
    }
});