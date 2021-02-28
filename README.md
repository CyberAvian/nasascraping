# nasascraping

Purpose:
    Fetches NASA Astronomy Photos of the Day and stores them in a folder to be used as a screensaver slideshow. Can also just be a gallery of NASA APOD. 

Set Up:
    1. Go to https://api.nasa.gov/
    2. Generate an API Key if you haven't already
    3. Create a file in this directory named '.env'
    4. Create a variable named API_KEY and set it equal to your API Key in quotes
        a. Example: API_KEY="1234567890"
    
Usage:
    1. Run main.py
    2. Select the date range you want to pull from
        a. Today = Pull the photo of the day for today
        b. Month = Pull the photos of the day for everyday this month (up to today)
    3. Point your system's screensaver to the folder that is created for you
        a. This folder is yourhomedirectory/documents/screensaver/APODScreensavers