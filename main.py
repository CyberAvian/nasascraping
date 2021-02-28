import os
import apod

key = os.getenv("API_KEY")

a = apod.APOD(key)
a.main()