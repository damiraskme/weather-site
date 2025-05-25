from __future__ import print_function
import time
import weatherapi
from weatherapi.rest import ApiException
from pprint import pprint
from datetime import datetime, date, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
def pretify_current_weather(api_response):
    try:
        pretify = {
    "picture": api_response["current"]["condition"]["icon"],
    'condition': f"Weather: {api_response["current"]["condition"]["text"]}",
    'temp_c': f"Temperature: {api_response["current"]["temp_c"]}°C / {api_response["current"]["temp_f"]}°F",
    'feelslike_c': f"Feels like: {api_response["current"]["feelslike_c"]}°C / {api_response["current"]["feelslike_f"]}°F",
    'cloud': f"Cloudness: {api_response["current"]["cloud"]}%",
    'gust_kph': f"Gust: {api_response["current"]["gust_kph"]} km/h {api_response["current"]["gust_mph"]} mph",
    'wind_degree': f"Wind: {api_response["current"]["wind_degree"]}{api_response["current"]["wind_dir"]}",
    'wind_kph': f"Wind speed: {api_response["current"]["wind_kph"]} km/h {api_response["current"]["wind_mph"]} mph",
    'pressure_mb': f"Pressure: {api_response["current"]["pressure_mb"]}",
    'uv': f"UV index: {api_response["current"]["uv"]}",
    'humidity': f"Humidity: {api_response["current"]["humidity"]}%",
    'last_updated': f"Last update: {api_response["current"]["last_updated"]}",
 }
    except:
        return None
    return pretify

def pretify_future_weather(api_response):
    pretify = {}
    try:
     for i in api_response:
        pretify[i] = {
            "picture": api_response[i]["condition"]["icon"],
            "temp": f"Temp: {api_response[i]["avgtemp_c"]}°C / {api_response[i]["avgtemp_f"]}°F",
            "condition": f"{api_response[i]["condition"]["text"]}",
            'daily_chance_of_rain': f"Chance of rain: {api_response[i]["daily_chance_of_rain"]}%",
            'daily_chance_of_snow': f"Chance of snow: {api_response[i]["daily_chance_of_snow"]}%"
        }
    except:
        return None
    
    return pretify

def get_weather(q):
    configuration = weatherapi.Configuration()
    configuration.api_key['key'] = os.getenv("API_KEY")

    api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
    lang = 'en' 

    try:
        api_response = api_instance.realtime_weather(q, lang=lang)
        return api_response
    except ApiException as e:
        print("Exception when calling APIsApi->realtime_weather: %s\n" % e)

def get_future_weather(q):
    configuration = weatherapi.Configuration()
    configuration.api_key['key'] = os.getenv("API_KEY")

    api_instance = weatherapi.APIsApi(weatherapi.ApiClient(configuration))
    lang = 'en' 
    try:
    # Forecast API
        api_response = api_instance.forecast_weather(q, days=5, alerts="no", aqi="no", tp=24)
        res = {}
        for i in api_response["forecast"]["forecastday"]:
            res[i["date"]] = i["day"]
        return res
    except ApiException as e:
        print("Exception when calling APIsApi->forecast_weather: %s\n" % e)

def current_weather(location):
    return pretify_current_weather(get_weather(location))
def forecast_weather(location):
    return pretify_future_weather(get_future_weather(location))



