# Lahire Weather PWA v2.0

## Table of Contents

- [[Description]](#description)
- [[Code]](#code)
- [[API Reference]](#api)
- [[License]](#license)

## Description
This Progressive Web App(PWA) is a revamp of a extension of my final project for CEIS110 Intro to Programming. The project involved using noaa_sdk and matplotlib to create a simple Python program that takes zipcode, country, and start/end date as parameters to pull weather data from NOAA sensors. After completing that project I attempted to take it a step further by making a app version of it for my phone. Because I do not know or have the time to learn how to create iOS/Android apps I opted for creating a PWA knowing it can be 'added to the home screen' as a sudo app.

My first attempt at this project got really complicated and I made the mistake of making changes to code without really keeping track of changes or documenting in the code. I think the part that really messed up the first attempt was that I took bits and pieces of code from suggestions online and just threw them into my code to try and resolve build issues. 

For this attempt I spent about 8 hours reading/watching all the recources in [Documents](https://github.com/jlahire/weather-pwa-2/wiki/Documents) and [Web Resources](https://github.com/jlahire/weather-pwa-2/wiki/Web-Resources) The plan this time is to build the PWA according to the recomended set up. I will attempt to use python where I can but wont compromise the project for it.   

See the [Wiki](https://github.com/jlahire/weather-pwa-2/wiki) for the development process. I will make note all challenges and solutions found as well as all the people, documents and resources that helped me get this project started and running.

## Code

- Frontend:
  - [![HTML][HTML5]][HTML5-url]
  - [![CSS][CSS3]][CSS3-url]
  - [![JavaScript][JavaScript]][JavaScript-url]
  - [![Chart.js][Chartjs]][Chartjs-url]

- Backend:
  - [![Python][Python]][Python-url]
  - [![NOAA SDK][NOAA]][NOAA-url]

- Deployment:
  - [![Netlify][Netlify]][Netlify-url]
  - [![Netlify Functions][NetlifyFunctions]][NetlifyFunctions-url]

- Configuration:
  - [![JSON][JSON]][JSON-url]
  - [![TOML][TOML]][TOML-url]

- Documentation:
  - [![Markdown][Markdown]][Markdown-url]

[HTML5]: https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white
[HTML5-url]: https://developer.mozilla.org/en-US/docs/Web/HTML
[CSS3]: https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white
[CSS3-url]: https://developer.mozilla.org/en-US/docs/Web/CSS
[JavaScript]: https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black
[JavaScript-url]: https://developer.mozilla.org/en-US/docs/Web/JavaScript
[Chartjs]: https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chart.js&logoColor=white
[Chartjs-url]: https://www.chartjs.org/
[Python]: https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white
[Python-url]: https://www.python.org/
[NOAA]: https://img.shields.io/badge/NOAA_SDK-0077B5?style=for-the-badge&logo=noaa&logoColor=white
[NOAA-url]: https://github.com/paulokuong/noaa
[Netlify]: https://img.shields.io/badge/Netlify-00C7B7?style=for-the-badge&logo=netlify&logoColor=white
[Netlify-url]: https://www.netlify.com/
[NetlifyFunctions]: https://img.shields.io/badge/Netlify_Functions-00C7B7?style=for-the-badge&logo=netlify&logoColor=white
[NetlifyFunctions-url]: https://docs.netlify.com/functions/overview/
[JSON]: https://img.shields.io/badge/JSON-000000?style=for-the-badge&logo=json&logoColor=white
[JSON-url]: https://www.json.org/json-en.html
[TOML]: https://img.shields.io/badge/TOML-9C4121?style=for-the-badge&logo=toml&logoColor=white
[TOML-url]: https://toml.io/en/
[Markdown]: https://img.shields.io/badge/Markdown-000000?style=for-the-badge&logo=markdown&logoColor=white
[Markdown-url]: https://www.daringfireball.net/projects/markdown/



## API

Talks to NOAA sensors. It is really simple since this is just a personal project..

### How? 
[![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()

`/api/weather`

Takes 3 inputs (zipcode, country, period) and returns weather stuff from NOAA.

#### input
```javascript
// Basic fetch example
const response = await fetch(`/api/weather`, {
    method: 'POST',
    headers: {'Content-Type': 'application/json',},
    body: JSON.stringify({weatherStuff: {zipcode,country,period}})
});
```

#### return
[![Response Status](https://img.shields.io/badge/Type-JSON-blue)]()
```javascript
{resultsDiv.textContent = data.weatherData;
console.log('Temperature data:', data.temperatureData);
console.log('Humidity data:', data.humidityData);} 
```

#### errors
[![Error Handling](https://img.shields.io/badge/Status-Implemented-green)]()
- If you forget something: "Missing input"
- If period isn't a number: "Period must be integer"
- If something breaks: You'll get the specific error

Check out the [Wiki](https://github.com/jlahire/weather-pwa-2/wiki) if you want to see how I built and tested this.


## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)



[Work in Progress]: https://img.shields.io/badge/Status-Work%20in%20Progress-yellow
[Completed]: https://img.shields.io/badge/Status-Completed-green
