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

Ep  = cal(65)
Mp  = cal(74)
Tp  = cal(88)

print("Age is %d, peace rate is %d"%(age,hrr))
print("Level\t%\tHRR")
print("E\t65~74\t%d~%d"%(cal(65),cal(74))
print("M\t74~85\t%d~%d"%(cal(74),cal(85))
print("T\t85~88\t%d~%d"%(cal(85),cal(88))
print("I\t88~97\t%d~%d"%(cal(88),cal(97))

