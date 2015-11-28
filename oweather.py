#!/usr/bin/env python
import requests
import json
import ujson
import argparse
from argparse import ArgumentParser
import ipdb

class OpenWeatherMapAPIWrapper:
  def __init__(self, api_key):
    self.api_key = api_key

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

def process_arguments():
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
  key_group = parser.add_mutually_exclusive_group(required=True)
  key_group.add_argument("-k",
                      "--key",
                      type=str,
                      help="Open weather map API key")
  key_group.add_argument("--key-file",
                         dest="file",
                         type=argparse.FileType("r"),
                         help="Text file with open weather map API key")
  parser.add_argument("city",
                      help="Name of city you want to get weather for",
                      nargs=1)
  return parser.parse_args()

def print_weather_info(owmaw, args):
  if args.forecast is True:
    print_json(owmaw.get_5day_forcast_by_city_name(args.city[0]))
  elif args.n > 0:
    print_json(owmaw.get_daily_forcast_by_city_name(args.city[0], days=args.n))
  else:
    print_json(owmaw.get_current_weather_by_city_name(args.city[0]))

def print_json(json_dict):
  print json.dumps(json_dict, sort_keys=True, indent=2,
                    separators=(",", ": 2"))

def get_api_key_from_file(f):
  for line in f.readlines():
    key, value = line.partition("=")[::2]
    if key.strip() == "openweathermap_api_key":
      return value.strip()[1:-1]

def get_api_key(args):
  if args.key is not None:
    return args.key
  elif args.file is not None:
    return get_api_key_from_file(args.file)

if __name__ == "__main__":
  args = process_arguments()
  api_key = get_api_key(args)
  owmaw = OpenWeatherMapAPIWrapper(api_key)
  print_weather_info(owmaw, args)
