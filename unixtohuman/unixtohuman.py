#!/usr/bin/python3
#unixtohuman.py is a simple commandline utility built to do quick conversions of unix timestamps into human readable timestamps

import datetime
import sys

if len(sys.argv) == 1:
    print('Usage: "# unixtohuman.py <unix-timestamp> <unix-timestamp>".\n\
Note: you can use as many <unix-timestamp> as you please, and they will all convert!')

for i in sys.argv:
    if i != sys.argv[0]:
        try:
            timestamp = float(i)
        except ValueError:
            print('\nERROR! Could not convert "', i, '" to float! Usage: "# unixtohuman.py <unix-timestamp> <unix-timestamp>".\n\
Note: you can use as many <unix-timestamp> as you please, and they will all convert!')
            sys.exit(1)
        timestampconverted = datetime.datetime.fromtimestamp(timestamp)
        print(timestamp, " == ", timestampconverted.strftime('%c'))

