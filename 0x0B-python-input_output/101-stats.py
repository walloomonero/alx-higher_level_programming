#!/usr/bin/python3
"""Defines a script that reads stdin line by line and computes metrics.

Each 10 lines and after a keyboard interruption (CTRL + C),
prints those statistics since the beginning:
    - Total file size: File size: <total size>.
    - where is the sum of all previous.
    - Number of lines by status code.
"""


def print_stats(size, status_codes):
    """To print accumulated metrics.

    Args:
        size (int): Accumulated read file size.
        status_codes (dict): Accumulated count of status codes.
    """
    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))


if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}
    poss_codes = ['200', '301', '400', '401', '403', '404', '405', '500']
    count = 0

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

            line = line.split()

            try:
                size += int(line[-1])
            except (IndexError, ValueError):
                pass

            try:
                if line[-2] in poss_codes:
                    if status_codes.get(line[-2], -1) == -1:
                        status_codes[line[-2]] = 1
                    else:
                        status_codes[line[-2]] += 1
            except IndexError:
                pass

        print_stats(size, status_codes)

    except KeyboardInterrupt:
        print_stats(size, status_codes)
        raise
