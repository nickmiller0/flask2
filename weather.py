import forecastio
from geopy.geocoders import Nominatim
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

def get_weather (address):
	api_key = os.environ['WEATHER_API_KEY']
	geolocator = Nominatim()
	location = geolocator.geocode(address)
	lat = location.latitude
	lng = location.longitude
	forecast = forecastio.load_forecast(api_key, lat, lng).currently()
	
	# weather = []

	summary = forecast.summary
	temperature = forecast.temperature

	#weather.append({"summary": summary, "temperature": temperature, "address": address})
	return("{} and {}° in {}".format(summary, temperature, address))	

	#return weather

#weather = get_weather(address, api_key)

# print(weather)