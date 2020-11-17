import sys
import datetime

if len(sys.argv) == 0:
    birth = 1987
    peace_rate = 60

age = datetime.datetime.now().year - birth
MAX = 220 - age
Ep  = MAX * 0.6
Mp  = MAX * 0.75
Tp  = MAX * 0.9




