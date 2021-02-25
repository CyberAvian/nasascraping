import os
import nasapy
from datetime import date

api_key = os.getenv("API_KEY")
nasa = nasapy.Nasa(api_key)
today = date.today()

responses = []
for day in range(1,today.day+1):
    fetch_date = date(today.year,today.month,day).strftime("%Y-%m-%d")
    response = nasa.picture_of_the_day(fetch_date, hd=True)
    responses.append(response["url"])

for url in enumerate(responses, 1):
    print(f"{url[0]}. {url[1]}")