"""
The Weather app
Write a console application which takes as an input a city name and returns current weather in the format of your choice.
For the current task, you can choose any weather API or website or use https://openweathermap.org
"""

import requests
import argparse

if __name__ == "__main__":
    API_KEY = "686c8b13cb3a52a68964fcb473263add"
    parser = argparse.ArgumentParser(description='Current weather')
    parser.add_argument('city', action="store", help="City name")
    parser.add_argument('-f', action="store", dest="format", default="JSON",
                        help="Response format: JSON, XML or HTML. Default is JSON")
    args = parser.parse_args()
    response = requests.get(f"http://api.openweathermap.org/data/2.5/weather?appid={API_KEY}&q={args.city}&mode={args.format}")
    print(response.text)
