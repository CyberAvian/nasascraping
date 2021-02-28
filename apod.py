import os
import pathlib
import urllib.request
from datetime import date
from pathlib import Path

import nasapy
    

class APOD:
    def __init__(self, key: str):
        self.key = key
        self.nasa = nasapy.Nasa(key)

    def main(self, date_range: str = None) -> None:
        # Get list of dates
        if not date_range:
            error = ""
            while True:
                print("Please input the date range to pull.\n")
                choices = ["today", "this month"]
                for choice in enumerate(choices, 1):
                    print(f"{choice[0]}. {choice[1].title()}")
                response = input(f"\n{error}> ")[0] # strip everything but the first character in case user inputs the period

                if response in [str(i) for i in range(1, len(choices)+1)]:
                    date_range = choices[int(response)-1]
                    break
                else:
                    error = "Invalid input. Please type the number of the option you wish to choose.\n"
        
        print("Formatting dates...\n")
        fetch_dates = self.get_dates(date_range)
        
        # Get picture urls for dates
        print("Retrieving URLs...\n")
        picture_urls = self.get_picture_urls(fetch_dates)

        # Save pictures to UserProfile/Documents/APOD
        print("Saving pictures...\n")
        self.save_pictures(picture_urls)

        print("Finished!")
        return

    def get_dates(self, date_range: str) -> list:
        dates = []

        if date_range == 'today':
            dates.append(date.today().strftime("%Y-%m-%d"))
        elif date_range == 'this month':
            for day in range(1, date.today().day):
                year = date.today().year
                month = date.today().month
                formatted_date = date(year, month, day).strftime("%Y-%m-%d")
                dates.append(formatted_date)

        return dates

    def get_picture_urls(self, dates: list) -> list:
        responses = []

        for day in dates:
            response = self.nasa.picture_of_the_day(day, hd=True)
            responses.append(response["url"])

        return responses

    def save_pictures(self, urls: list('str')) -> None:
        # Create APODScreensavers directory if it doesn't already exist
        apod_screensaver_path = pathlib.Path.home() / 'documents' / 'screensavers' / 'APODScreensavers'
        Path(apod_screensaver_path).mkdir(parents=True, exist_ok=True)
        
        # Make sure the url points to an image then save
        for url in urls:
            if url.endswith('.jpg'):    
                picture = url.split('/')[-1]
                urllib.request.urlretrieve(url, f"{apod_screensaver_path}/{picture}")
        
        print(f"Pictures are saved in {apod_screensaver_path}\n")
        return
