#!/usr/bin/python3

"""The script that takes in a URL,
   sends a request to the URL and displays
   the body of the response (decoded in utf-8).
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        with urllib.request.urlopen(url) as respon:
            body = respon.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as err:
        print("Error code:", err.code)
