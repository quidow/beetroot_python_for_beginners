"""
Robots.txt
Download and save to file robots.txt from wikipedia, twitter websites etc.
"""

from urllib.parse import urlparse
import requests
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='robots.txt')
    parser.add_argument('url', action="store", help="valid url with scheme")
    args = parser.parse_args()
    parsed_uri = urlparse(args.url)
    if not parsed_uri.scheme or not parsed_uri.netloc:
        print("url is invalid")
        exit()
    root = '{uri.scheme}://{uri.netloc}'.format(uri=parsed_uri)
    response = requests.get(root + "/robots.txt")
    with open("robots.txt", "w", encoding=response.encoding) as f:
        f.write(response.text)
