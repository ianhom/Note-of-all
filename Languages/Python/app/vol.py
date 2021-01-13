#!/usr/bin/python
import time
import sys

days = time.dayofmonth()
vol_total = sys.argv[1]
vol = int(vol_total) / days

if __name__ == '__main__':
    print(vol)
