import apod
from decouple import config

API_KEY = config("API_KEY")

a = apod.APOD(API_KEY)
a.main()