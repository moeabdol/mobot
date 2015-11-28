#!/usr/bin/env python
import requests
import json
import ujson
from argparse import ArgumentParser

class OpenWeatherMapAPIWrapper:
  def __init__(self, api_key):
    self.api_key = api_key
    args = self.process_arguments()
    self.get_weather_info(args)

  def process_arguments(self):
    parser = ArgumentParser(description="Get weather information from the " +
                                        "Open Weather Map API")
    forecast_group = parser.add_mutually_exclusive_group()
    forecast_group.add_argument("-f",
                                "--forecast",
                                dest="forecast",
                                action="store_true",
                                help="Get five day weather forcast for city")
    forecast_group.add_argument("-d",
                                "--days",
                                dest="n",
                                type=int,
                                help="Get N days weather forcast for city")
    parser.add_argument("city",
                        help="Name of city you want to get weather for",
                        nargs=1)
    return parser.parse_args()

  def get_weather_info(self, args):
    if args.forecast is True:
      self.print_to_screen(self.get_5day_forcast_by_city_name(args.city[0]))
    elif args.n > 0:
      self.print_to_screen(self.get_daily_forcast_by_city_name(args.city[0],
                                                               days=args.n))
    else:
      self.print_to_screen(self.get_current_weather_by_city_name(args.city[0]))

  def get_current_weather_by_city_name(self, city_name):
    end_point = "http://api.openweathermap.org/data/2.5/weather"
    city_query = "?q={}".format(city_name)
    appid_query = "&APPID={}".format(self.api_key)
    response = requests.get(end_point + city_query + appid_query)
    return ujson.loads(response.text)

  def get_5day_forcast_by_city_name(self, city_name):
    end_point = "http://api.openweathermap.org/data/2.5/forecast"
    city_query = "?q={}".format(city_name)
    appid_query = "&APPID={}".format(self.api_key)
    response = requests.get(end_point + city_query + appid_query)
    return ujson.loads(response.text)

  def get_daily_forcast_by_city_name(self, city_name, days=7):
    end_point = "http://api.openweathermap.org/data/2.5/forecast/daily"
    city_query = "?q={}".format(city_name)
    days_query = "&cnt={}".format(days)
    appid_query = "&APPID={}".format(self.api_key)
    response = requests.get(end_point + city_query + days_query +
                            appid_query)
    return ujson.loads(response.text)

  def print_to_screen(self, weather_info_json):
    print json.dumps(weather_info_json, sort_keys=True, indent=2,
                     separators=(",", ": 2"))

if __name__ == "__main__":
  from utils import get_api_keys
  owm_api_key = get_api_keys("api_keys.txt")["openweathermap_api_key"]
  owmaw = OpenWeatherMapAPIWrapper(owm_api_key)
