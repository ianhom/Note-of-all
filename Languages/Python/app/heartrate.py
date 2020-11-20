import sys
import datetime

birth = 1987
peace_rate = 60
if len(sys.argv) > 1:
    peace_rate = sys.argv[1]
if len(sys.argv) > 2:
    birth = sys.argv[2]

age = datetime.datetime.now().year - birth
MAX = 220 - age
hrr = MAX - peace_rate

def cal(a):
    global hrr
    global peace_rate
    return hrr * a / 100 + peace_rate

Ep  = MAX * 0.6
Mp  = MAX * 0.75
Tp  = MAX * 0.9




