document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('weather-form');
    const resultsDiv = document.getElementById('weather-results');

    form.addEventListener('submit', async (e) => {
        e.preventDefault();
        const zipcode = document.getElementById('zipcode').value;
        const country = document.getElementById('country').value;
        const period = document.getElementById('period').value;

        resultsDiv.textContent = `Submitted: ${zipcode}, ${country}, ${period}`;
    });
});


console.log("test #");