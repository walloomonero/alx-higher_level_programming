#!/usr/bin/python3
"""The script that takes in a URL,
   sends a request to the URL and displays
   the body of the response (decoded in utf-8).
"""
from urllib.request import Request, urlopen
from urllib.error import HTTPError
from sys import argv

if __name__ == "__main__":
    url = argv[1]
    reque = Request(url)

    try:
        with urlopen(reque) as respon:
            print(respon.read().decode('UTF-8'))
    except HTTPError as err:
        print("Error code: {}".format(err.code))
