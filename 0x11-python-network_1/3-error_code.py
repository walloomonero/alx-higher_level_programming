#!/usr/bin/python3
"""The script that takes in a URL,
   send a request to URL, and dispaly body
   of the response (decoded in utf-8).
"""


if __name__ == "__main__":
    from urllib import request, error
    import sys

    try:
        with request.urlopen(sys.argv[1]) as resp:
            print(resp.read().decode('UTF-8'))
    except error.HTTPError as er:
        print('Error code:', er.code)
