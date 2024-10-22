# Development Log

[![Last Updated](https://img.shields.io/badge/Last%20Updated-10--19--2024-brightgreen)]()
[![Project Status](https://img.shields.io/badge/Status-Still%20Building-red)]()
[![Total Hours Worked](https://img.shields.io/badge/Project%20Hours-28hrs-black)]()
- [Link to Current Log](#current-log)

## Table of Contents
- [Mentions](#mentions)
- [Overview](#overview)
- [Daily Logs](#daily-logs)
- [Challenges](#challenges)
- [Documents](#documents)
- [Web Resources](#web-resources)

See [README.md](README.md) for general project information.

## Mentions

- **add Gabe**

## Overview
The purpose of this development log is to keep track of progress and allow readers to see the entire development process and what has gone into this project.
```
File Structure:

WEATHER-PWA-2
├── frontend
│   ├── css
│   │   └── style.css
│   ├── js
│   │   └── app.js
│   ├── icon.2.png
│   ├── icon.png
│   ├── index.html
│   ├── manifest.json
│   └── sw.js
├── netlify
│   └── functions
│       └── weather.py
├── DEVLOG.md
├── netlify.toml
├── LICENSE.md
├── README.md
└── requirements.txt
```

## Daily Logs
[Back to Top](#table-of-contents)

### [10-15-2024] [![Day Status](https://img.shields.io/badge/Status-Completed-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-5%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
  1. Transfer files from weather-pwa 
  2. Allocate resources from weather-pwa README.md
  3. Use python to pull URL's from weather-pwa README.md and plug into templates in DEVLOG.md.
  4. Work on [Documents Read](#documents-read) and [Web Resources](#web-resources).
- **Progress made:** 
  1. Completed 1, 2, and 3. 
  2. Did a little of 4
- **Next steps:**
  1.  Finish 4 
  2. Delete all old file contents. 
  3. Start from scratch(kinda).
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:** 
      -  When I decided to scrap my previous project and go with a second attempt I don't think I fully planned on making this as professional and organized as I am now. I like that it is streamlined and that it's easier to navigate the README.md. In my last version of this project the README.md became more of a journal than it did a typical readme. I am excited having spent about 4-5 hours today working on getting everythin ready and organized.
    - **Challenges faced:** 
      1. I am not very well versed in .md or dev documentation in general.
    - **Solutions found:** 
      1. Spent about 1 hour today reading .md guides and then listend to a few different youtube videos that walked through documentation and organizing a devLog for tracking progress on a project.

### [10-16-2024] [![Day Status](https://img.shields.io/badge/Status-Completed-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-6%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
  1. Keep files/file names but delete contents.
  2. Create LICENSE.md
  3. Write README.md (keep it simple and professional)
  4. Drink coffee.
  5. Finish templates for DEVLOG.md
  6. Write manifest.json 
  7. Write sw.js (include path for app.js)
  8. Write index.html
  9. Check and make sure manifest.json is linked to index.html
  10. Create icon.png(192x192) and icon.2.png(512x512)
  11. Write style.css
  12. Cehck and make sure style.css is linked in index.html and sw.js
- **Progress made:** 
  1. Completed 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12
- **Next steps:**
  1. Write app.js and weather.py (try a new approach)
- **Comments:**
    - **Thoughts:**
      - **Initial impressions:** 
        - Now that I've gotten the core of my file structure more aligned to what I've been reading about I feel like I have a good starting point. I went ahead and added the path for app.js to my sw.js file even though I haven't written the app.js file yet. I find myself recognizing where to put code in these files now which is refreshgin and encouraging. I still have a lot of work to do. I will spend the rest of the day looking at the old app.js/weather.py files and consider some new approaches. In my previous attempt I was definitely too focused on python. This time around I will follow the already established format instead of recreating the wheel so to speak. Also instead of being super stylish and spending a lot of ttime trying to make the GUI look nice and trendy, I decided to go with a generic, bland, GUI look and color scheme.
      - **Challenges faced:** 
        1. I had a hard time creating the icons from scratch. 
        2. I revisited the files in the previous attempt to see how I structured them and realized that with all the changes I was constantly making after reading this article or that I really couldn't tell which parts were specific to PWA deployment on Netlify and which were suggestions that may or may not have applied. 
        3. In some of the web resources they mention including a LICENSE.md file to protect myself but I have no idea what license to use. 
        4. I am not sure what a professional readme should look like. 
      - **Solutions found:** 
        1. Ened up using a free online icon maker and uploaded my old icon.png to get my 192x192 and then found a very simple free opensource .jpg of a sun and cloud on google images and uploaded it to the same website to get a 512x512 icon. 
        3. I found that a simple MIT license will work for what I'm doing and was able to find a template on github. 
        4. I reread githubs documentaion on readme's and then googled a few examples of professional readme's before settling with the format I hvae now.

### [10-17-2024] [![Day Status](https://img.shields.io/badge/Status-Completed-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-5%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
    1. start weather.py 
    2. start requirements.txt
    3. start app.js 
    4. start netlify.toml
    5. update README.md 
    6. do i need a runtime.txt?
- **Progress made:**
  1. completed: 1, 2, 3, 4, 5, 7
- **Next steps:**
  1. Continue writing weather.py 
  2. continue writing app.js
  3. Figure out if I need a runtime.txt. 
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:** 
      - Excited. I'm finding myself doing more reading and learning than I am coding.. I would probably say there is a 1:4/hr ratio right now. I read for 45 minutes and then write code for 15 before having to read more to figure out the next part. I'm loving how much more professional this version of my project is becomming. 
    - **Challenges faced:** 
      1. After all the reading I've done I realize that I need to code this in such a way that it wont crash if there are multiple users. 
      2. I am following a similar format to my previous version of this file with the biggest differences being that I removed matplotlib after reading how it might be too resource intensive for my PWA.
      3. I don't know anything about chartjs
    - **Solutions found:** 
      1. asyncio solves my "multiple users" issue with my python file. Still need to read more about using it though
      2. Because I'm not using matplotlib I looked up some matplotlib alternatives for PWA on google. The first one I found that was described as "light weight" and didn't require an api to interface with python was chartjs. because I plan to include chartjs in my app.js file I plan to put a return response that throws everything my weather.py file processes out as a JSON response so app.js can grab it and turn it into a chart. But I still need to figure that part out so for now this is what I'll use for my weather.py file:
      ```
      import json
      from datetime import datetime, timedelta

      def handler(event, context):
          return {
              'statusCode': 200,
              'body': json.dumps({'message': 'hello world'})
          }
      #test
      test_event = {'httpMethod': 'GET'}
      result = handler(test_event, {})
      assert result['statusCode'] == 200
      assert json.loads(result['body'])['message'] == 'hello world'
      print("it works!")
      ```
      3. So I read through the [chartjs](#javascript) doc page to understand how to use it to render my weather graphs but I still don't understand how to use it yet. So I went back to my original app.js file and looked at the core parts of it and made this as a place holder until I have a better idea how to implement chartjs in my app.js file:
      ```
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
      ```
      4. I added the chartjs linnk to my sw.js file. And tomorrow I'll work on getting the weather.py file to dump zipcode country and period to the app.js file. 

### [10-18-2024] [![Day Status](https://img.shields.io/badge/Status-Completed-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-4%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
  1. Continue writing weather.py
  2. continue writing app.js
  3. Figure out if I need a runtime.txt. 
  4. Recheck paths in html/sw
  5. Clean up DEVLOG.md (Daily Log Template)
  6. publish github repo....(can't believe I haven't dont this yet...)
- **Progress made:**
  1. completed 4, 5. I spent most of my time reading [chartjs](#javascript),[netlify](#netlify-config-documentation), and planning what to do next with weather.py and app.js. 
- **Next steps:**
  1. Continue work on weather.py and app.js
  2. recheck if I need a runtime.txt file
  3. publish github repo
  4. write netlify.toml
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:** 
      This is turning into a massive project. I wish I had the knowledge of js and netlify to be able to get this project up and running. I'm realizing how in my previous attempt where I just copy & pasted ideas and work arounds that I stumbled upon in forums made this entire process more difficult for me. But, I have an idea how the weather.py and app.js files need to look like and from my last attempt I know that it is better if i understand what i'm coding and why. 
    - **Challenges faced:**
      1. Project scale
      2. Lack of actual language knowledge
      3. Time
    - **Solutions found:**
      1. The scale of this project seems to be continuing to grow. Again I spent the majority of my time reading to understand what I needed to do next. The most difficult part I think is making sure the python part is all compatible with python 3.8. 
      2. The continue problem I face right now is my lack of knowledge and experience. While I've done other projects that involve multiple languages I never really learned what I was coding but instaed wrote what I was instructed or advised to write. I'm not losing hope though. Each day I find myself understading just a little bit more than the day before.
      3. I can't do anything about the lack of time. I wish I could spend 10 hours a day 5 days a week working on this project but even the 20 hours I've put in over the past few days has taken a toll on my normal day-to-day. The light at the end of the tunnel here is my documentation. With how i'm documenting this development process it will be easier for me to pick up where I left off last. Still, I need to be more detail oriented with my progress and once I init my repo i'll begin using branches as I finish building weather.py and app.js. With this I will start doing 1-2 hours of work every other day so that I don't get burnt out working on this but also so I can have a better balance.

### [10-19-2024] [![Day Status](https://img.shields.io/badge/Status-Completed-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-3%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
  1. Continue work on weather.py and app.js
  2. recheck if I need a runtime.txt file
  3. publish github repo
  4. write netlify.toml
  5. clean up README.md and DEVLOG.md
- **Progress made:**
  1. completed 1-ish, 2, 3, 4-ish, 5
- **Next steps:**
  1. start get_weather function in weather.py
  2. start headers in weather.py
  3. implement asyncio in weather.py
  4. build a project timeline and plan to start working on app.js after i've finished weather.py
  5. add stuff to netlify.toml
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:**
      - Accomplished. So I do not know very much about json as most of my experience with it has been copy&paste/edit, but I had a successful local test today of my weather.py file using json. Here was my output:
      ```
      PS D:\Code Stuff\Python\Projects\PWA-Projects\weather-pwa-2\netlify\functions> python weather.py
      {'statusCode': 200, 'body': '{"message": " 30350, US, 14 test."}'}
      it works!
      ```
      - It felt good being able to put this together. I realize that my file doens't have the clean look like all the examples I've read about but I don't really understand how to space out my code like the examples. I think this is because I'm so used to writing in python. I will explore cleaning up the code later once I've got a better "handle" on the file. (that was a programmer joke..i think..)
    - **Challenges faced:**
      1. How do I avoid making the same mistake as before by changing a ton of code and not being able to go back.
      2. Writing a handler function.
    - **Solutions found:**
      1. Read up on git branches and how to merge. I will make a branch for each part of the project and as they work i'll merge with master branch. rinse&repeat. 
      2. I've built functions for projects before but outside of my first attempt I haven't actually written a handler function. This time i'm building it in parts and testing each part so I don't get confused.


### [10-20-2024] [![Day Status](https://img.shields.io/badge/Status-Completed-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-2%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
  1. start get_weather function in weather.py
  2. start headers in weather.py
  3. implement asyncio in weather.py
  4. build a project timeline and plan to start working on app.js after i've finished weather.py
  5. add stuff to netlify.toml
  6. create api branch
- **Progress made:**
  1. completed 1, 6.
- **Next steps:**
  1. implement asyncio for get_weather and handler functions
  2. start headers in weather.py
  3. build a project timeline and plan to start working on app.js after i've finished weather.py
  4. add stuff to netlify.toml
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:**
      - I feel much better only comitting 2 hrs today to this project. It allows me to prioritize other things and keeps my goals for the day acheivable. It felt very good to be able to debug my get_weather function. I am definitely noticing that I can dissect my errors much easier than before and find myself going back to the [documents](#documents) and my web [recources](#web-resources) to find answers instead of google. I do look forward to seeing how far I can get in my weather.py file tomorrow.
    - **Challenges faced:**
      1. I added a get_weather function to weather.py. When I attempted to run it locally I got this error:
      ```
      {'statusCode': 500, 'body': '{"error": "Error: start and end must have format \'%Y-%m-%dT%H:%M:%SZ\' | \'%Y-%m-%d\' | \'%Y-%m-%d %H:%M:%S\'"}'}
      ```
      2. Not enough time. 
    - **Solutions found:**
      1. I'm getting the statusCode 500 because my time format doesn't work with noaa api. I need to change from '%m-%d-%Y' to '%Y-%m-%d' in both my startDate and endDate variables.
          1. After making the above changes I got a successful test.
          ```
          python weather.py
          {'statusCode': 200, 'body': '{"message": " 30350, US, 7 test.", "dataLength": 148}'}
          weather fetched successfully
          ```
      2. Because I'm limiting myself to only working 2 hours it really forces me to be very productive with the time I'm allotting myself. I want to work more because I'm on a roll. Tomorrow I will be off from work so I will allow 2-6 hrs of work and try to get the weather.py file completed/tested/committed and merged with the master branch. 

## Current Log
### [10-21-2024] [![Day Status](https://img.shields.io/badge/Status-Ongoing-orange)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-2%20hrs-black)]()
- **Author:** @jlahire
- **Tasks:**
  1. implement asyncio for get_weather and handler functions
  2. start headers in weather.py
  3. build a project timeline and plan to start working on app.js after i've finished weather.py
  4. add stuff to netlify.toml
- **Progress made:**
  1. I added more to the get_weather funciton and then tested it locally.
  2. Added async to get_weather and wrote obs to asyncio.to_thread().
- **Next steps:**
  1. [nextSteps]
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:**
      - [impressions]
    - **Challenges faced:**
      1. [challenge1]
      2. [challenge2]
    - **Solutions found:**
      1. [solution1]
      2. [solution2]

## Challenges
[Back to Top](#table-of-contents)

## Documents
[Back to Top](#table-of-contents)

### [Flask Course - PWA Dev]
[![Read Status](https://img.shields.io/badge/Status-Watched-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** freeCodeCamp
- **Link:** [Flask Course - Python Web Application Development](https://youtu.be/Z1RJmh_OqeA?si=dsNZxf5VmjPw_G4g)
- **Key Takeaways:**
  1. Flask is a popular choice for PWA backends
  2. Provides guidance on Flask projects with Heroku hosting
- **How it applies to the project:** Initially considered for backend development before switching to Netlify

### [Vite PWA Netlifyt]
[![Read Status](https://img.shields.io/badge/Status-Glanced-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Vite
- **Link:** [Vite PWA Netlify Deployment](https://vite-pwa-org.netlify.app/deployment/netlify.html)
- **Key Takeaways:**
  1. Provides information on deploying PWAs to Netlify
  2. Offers guidance on Netlify-specific configurations
- **How it applies to the project:** Reference for PWA deployment

### [Netlify Python Blog]
[![Read Status](https://img.shields.io/badge/Status-Skimmed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Netlify
- **Link:** [Netlify Python Blog Posts](https://www.netlify.com/blog/tags/python/)
- **Key Takeaways:**
  1. Python with Netlify
  2. Has example code
- **How it applies to the project:** Used to gather information on integrating Python with Netlify for the backend

### [Service Workers]
[![Read Status](https://img.shields.io/badge/Status-Read-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Netlify
- **Link:** [Service Workers Explained](https://www.netlify.com/blog/2017/10/31/service-workers-explained/)
- **Key Takeaways:**
  1. Service workers and their usage 
  2. guidance on service workers with Netlify
- **How it applies to the project:** Helped with writing service worker code for the PWA

### [Netlify Config Documentation]
[![Read Status](https://img.shields.io/badge/Status-Reviewed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Netlify
- **Link:** [Netlify Configuration Documentation](https://docs.netlify.com/configure-builds/manage-dependencies/)
- **Key Takeaways:**
  1. Managing dependencies in Netlify
  2. Configuring netlify builds
- **How it applies to the project:** Reference for netlify config

### [Node Version Manager (nvm) Documentation]
[![Read Status](https://img.shields.io/badge/Status-Glanced-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** nvm-sh
- **Link:** [Node Version Manager (nvm) Documentation](https://github.com/nvm-sh/nvm/blob/master/README.md#install--update-script)
- **Key Takeaways:**
  1. Instructions for nvm
  2. has scripts 
- **How it applies to the project:** Reference for node.js

### [Pyenv Documentation]
[![Read Status](https://img.shields.io/badge/Status-Glanced-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** pyenv
- **Link:** [Pyenv Documentation](https://github.com/pyenv/pyenv)
- **Key Takeaways:**
  1. managing Python versions
  2. installation and configuration
- **How it applies to the project:** Used to manage Python versions

### [Enterprise JavaScript Error Handling Presentation]
[![Read Status](https://img.shields.io/badge/Status-Reviewed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** SlideShare
- **Link:** [Enterprise JavaScript Error Handling Presentation](https://www.slideshare.net/slideshow/enterprise-javascript-error-handling-presentation/630870)
- **Key Takeaways:**
  1. error handling in JavaScript
  2. examples of implementing error handling
- **How it applies to the project:** Used as a reference for implementing error handling in the app.js file

### [Python venv Library Documentation]
[![Read Status](https://img.shields.io/badge/Status-Skimmed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Python.org
- **Link:** [Python venv Library Documentation](https://docs.python.org/3/library/venv.html)
- **Key Takeaways:**
  1. How to create and manage virtual environments in Python
  2. venv stuff
- **How it applies to the project:** How set up and manage the Python virtual environment

### [Netlify Headers Not Applying Discussion]
[![Read Status](https://img.shields.io/badge/Status-Delved-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Netlify Community
- **Link:** [Netlify Headers Not Applying Discussion](https://answers.netlify.com/t/headers-in-toml-not-applying/87328/9)
- **Key Takeaways:**
  1. Discusses issues with Netlify headers configuration
  2. Potential solutions and workarounds
- **How it applies to the project:** Investigated as a potential solution to deployment issues, but found to be unrelated(kinda)

### [Python Packaging User Guide]
[![Read Status](https://img.shields.io/badge/Status-Skimmed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Python Packaging Authority
- **Link:** [Python Packaging User Guide](https://packaging.python.org/en/latest/tutorials/packaging-projects/?form=MG0AV3)
- **Key Takeaways:**
  1. Guide on packaging Python projects
  2. creating build processes
- **How it applies to the project:** Used as a reference for writing the build process in Python

### [Netlify Python Dependencies Documentation]
[![Read Status](https://img.shields.io/badge/Status-Read-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Netlify
- **Link:** [Netlify Python Dependencies Documentation](https://docs.netlify.com/configure-builds/manage-dependencies/#python)
- **Key Takeaways:**
  1. How to manage Python dependencies in Netlify
  2. Configuring Python environments for Netlify functions
- **How it applies to the project:** Reference to troubleshoot Python dependency issues in the Netlify environment

### [Netlify Core Functions Documentation]
[![Read Status](https://img.shields.io/badge/Status-Skimmed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Netlify
- **Link:** [Netlify Core Functions Documentation](https://www.netlify.com/platform/core/functions/)
- **Key Takeaways:**
  1. Netlify Functions
  2. Explains how to implement and use serverless functions in Netlify
- **How it applies to the project:** reference for Netlify functions

### [Serverless Functions Netlify: A Beginner's Guide]
[![Read Status](https://img.shields.io/badge/Status-Read-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Daily.dev
- **Link:** [Serverless Functions Netlify: A Beginner's Guide](https://daily.dev/blog/serverless-functions-netlify-a-beginners-blue)
- **Key Takeaways:**
  1. "Beginner-friendly" introduction to Netlify Functions
  2. examples of serverless functions
- **How it applies to the project:** Guide for understanding and implementing serverless functions on netlify

### [Python Logging Handlers Documentation]
[![Read Status](https://img.shields.io/badge/Status-Skimmed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Python.org
- **Link:** [Python Logging Handlers Documentation](https://docs.python.org/3/library/logging.handlers.html)
- **Key Takeaways:**
  1. logging handlers available in Python
  2. logging in Python programs
- **How it applies to the project:** Reference for handlers in Python backends

### [AWS Lambda Python Handler Documentation]
[![Read Status](https://img.shields.io/badge/Status-Glanced-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** Amazon Web Services
- **Link:** [AWS Lambda Python Handler Documentation](https://docs.aws.amazon.com/lambda/latest/dg/python-handler.html)
- **Key Takeaways:**
  1. How to create Python handlers for AWS Lambda functions
  2. examples of serverless Python functions
- **How it applies to the project:** Reference for creating a handler function, ( but not using Lambda)

### [Lambda Function Handler in Python]
[![Read Status](https://img.shields.io/badge/Status-Glanced-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** GeeksforGeeks
- **Link:** [Lambda Function Handler in Python](https://www.geeksforgeeks.org/lambda-function-handler-in-python/)
- **Key Takeaways:**
  1. More lambda function stuff
  2. Examples of lambda handlers
- **How it applies to the project:** Used as a schema to build a custom handler function

### [HTTP Status Codes]
[![Read Status](https://img.shields.io/badge/Status-Skimmed-blue)]()
- **Date Read:** 10-2023
- **Author/Source:** GeeksforGeeks
- **Link:** [HTTP Status Codes](https://www.geeksforgeeks.org/10-most-common-http-status-codes/)
- **Key Takeaways:**
  1. List of common HTTP status codes
- **How it applies to the project:** Used as a reference for adding the correct HTTP status codes

### [Stack Overflow]
[![Read Status](https://img.shields.io/badge/Status-Read-blue)]()
- **Date Read:** Ongoing
- **Author/Source:** Stack Overflow community
- **Link:** [Stack Overflow](https://stackoverflow.com/)
- **Key Takeaways:**
  1. Provides solutions to specific coding problems
  2. Threads/q&a
- **How it applies to the project:** Troubleshooting refernece

### [GeeksforGeeks]
[![Read Status](https://img.shields.io/badge/Status-Read-blue)]()
- **Date Read:** Ongoing
- **Author/Source:** GeeksforGeeks
- **Link:** [GeeksforGeeks](https://www.geeksforgeeks.org/)
- **Key Takeaways:**
  1. Provides solutions to specific coding problems
  2. Tutorials/guides/articles
- **How it applies to the project:** Troubleshooting reference

### [freeCodeCamp YouTube Channel]
[![Read Status](https://img.shields.io/badge/Status-Watched-blue)]()
- **Date Read:** Ongoing
- **Author/Source:** freeCodeCamp
- **Link:** [freeCodeCamp YouTube](https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ)
- **Key Takeaways:**
  1. free coding tutorials
  2. multi language
- **How it applies to the project:** youtube video mentioned before

## Web Resources
[Back to Top](#table-of-contents)

### PWA Build
1. **MDN Progressive Web Apps Guide**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [MDN PWA Guide](https://developer.mozilla.org/en-US/docs/Web/Progressive_web_apps)
   - **Description:** Guide on building PWA/s
   - **How it's being used:** Reference

2. **Google Web Fundamentals - PWA**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [Google PWA](https://developers.google.com/web/progressive-web-apps)
   - **Description:** Google's docs on PWAs
   - **How it's being used:** Reference

### API
3. **NOAA API**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [NOAA API v3](https://www.weather.gov/documentation/services-web-api)
   - **Description:** Official API for National Oceanic and Atmospheric Administration
   - **How it's being used:** The whole project is based around this

4. **NOAA SDK**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [noaa-sdk PyPI](https://pypi.org/project/noaa-sdk/)
   - **Description:** Python SDK for interaction w/ NOAA API
   - **How it's being used:** Fetch weather data in python backend

### Python
5. **Python Official Documentation**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [Python Docs](https://docs.python.org/3/)
   - **Description:** Official Python documentation
   - **How it's being used:** Reference for Python syntax and standard library functions

6. **asyncio — Asynchronous I/O**
[![Usage Status](https://img.shields.io/badge/Status-Read-blue)]()
- **URL:** [Resource Name](https://docs.python.org/3.8/library/asyncio.html)
- **Description:** asyncio is used as a foundation for multiple Python asynchronous frameworks that provide high-performance network and web-servers, database connection libraries, distributed task queues, etc.
- **How it's being used in the project:** Planning to use asyncio in my weather.py so more than one person can use it.

### JavaScript
7. **MDN JavaScript Guide**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [MDN JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide)
   - **Description:** Comprehensive guide to JavaScript
   - **How it's being used:** Reference for JavaScript

8. **Chart.js Documentation**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [Chart.js Docs](https://www.chartjs.org/docs/latest/)
   - **Description:** Documentation for Chart.js library
   - **How it's being used:** Reference for the weather charts

### Netlify
9. **Netlify Docs**
   [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
   - **URL:** [Netlify Docs](https://docs.netlify.com/)
   - **Description:** Official Netlify documentation
   - **How it's being used:** Reference for Netlify

10. **Netlify Functions**
    [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
    - **URL:** [Netlify Functions](https://docs.netlify.com/functions/overview/)
    - **Description:** Guide on Netlify Functions for serverless backend
    - **How it's being used:** Backend functions inside a serverless environment

### Version Control
11. **GitHub Docs**
    [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
    - **URL:** [GitHub Docs](https://docs.github.com/en)
    - **Description:** Official GitHub documentation
    - **How it's being used:** Reference for GitHub

### CSS
12. **MDN CSS Reference**
    [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
    - **URL:** [MDN CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference)
    - **Description:** Comprehensive CSS reference
    - **How it's being used:** Styling the PWA for optimal user experience

    
13. **Copy & Paste CSS**
    [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
    - **URL:** [Copy & Paste CSS](https://copy-paste-css.com/)
    - **Description:** Brief description resource
    - **How it's being used in the project:** Most things css in this project are from here or modified from these templates


### Markdown Template
14. **README/DEVLOG**
    [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
    - **URL:** [README Markdown](https://github.com/othneildrew/Best-README-Template/blob/main/README.md?plain=1)
    - **Description:** Guide for creating good README.md's
    - **How it's being used in the project:** Created both DEVLOG.md and README.md based on this template and the resources provided

### Badges and Shields
15. **Img Shields**
    [![Usage Status](https://img.shields.io/badge/Status-Active-blue)]()
    - **URL:** [Shields.io](https://shields.io)
    - **Description:** A service for creating customizable badges for GitHub repositories
    - **How it's being used:** Creating status badges

--- 

## Templates

### [Link to Add a Mention](#mentions)
### [![Mention Status](https://img.shields.io/badge/Status-statusTemplate-yellow)]()

- **Date:** MM-DD-YYYY
- **Mentioned Person:** @personHandle
- **Role/Contribution:**
  - *Project Area:* Specific area or task
  - *Contribution:* Detailed description of their help
  - *Impact:* How their contribution impacted the project
- **Comments:** 
  - *Thoughts:*
    - *Appreciation:* Express gratitude and appreciation
    - *Noteworthy Aspects:* Any particularly noteworthy aspects of their contribution

### [Link to Add a Daily Log](#daily-logs)
### [MM-DD-YYYY] [![Day Status](https://img.shields.io/badge/Status-statusTemplate-green)]()[![Hours Worked](https://img.shields.io/badge/Hours%20Worked-0%20hrs-black)]()
- **Author:** @devName
- **Tasks:**

- **Progress made:**
  1. [progress]
- **Next steps:**
  1. [nextSteps]
- **Comments:**
  - **Thoughts:**
    - **Initial impressions:**
      - [impressions]
    - **Challenges faced:**
      1. [challenge1]
      2. [challenge2]
    - **Solutions found:**
      1. [solution1]
      2. [solution2]

### [Link to Add a Challenge](#challenges)
### [Challenge Title]
[![Solution Status](https://img.shields.io/badge/Status-statusTemplate-brightgreen)]()
- **Date Encountered:** YYYY-MM-DD
- **Description of the Problem:**
- **Attempted Solutions:**
  1. 
  2. 
- **Final Solution:**
- **Lessons Learned:**

### [Link to Add a Document](#documents)
### [Document Title]
[![Read Status](https://img.shields.io/badge/Status-statusTemplate-blue)]()
- **Date Read:** YYYY-MM-DD
- **Author/Source:** 
- **Link:** [Document Title](URL)
- **Key Takeaways:**
  1. 
  2. 
- **How it applies to the project:**

### [Link to Web Add a Web Resource](#web-resources)
### [Resource Name]
[![Usage Status](https://img.shields.io/badge/Status-statusTemplate-blue)]()
- **URL:** [Resource Name](URL)
- **Description:** Brief description resource
- **How it's being used in the project:**


[Last Updated]: https://img.shields.io/badge/Last%20Updated-MM--DD--YYYY-brightgreen
[Project Status]: https://img.shields.io/badge/Status-In%20Progress-yellow
[Day Status]: https://img.shields.io/badge/Status-Completed-green
[Read Status]: https://img.shields.io/badge/Status-Completed-green
[Solution Status]: https://img.shields.io/badge/Status-Solved-brightgreen
[Usage Status]: https://img.shields.io/badge/Status-Active-blue