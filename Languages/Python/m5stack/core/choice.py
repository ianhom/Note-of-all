from m5stack import *
from m5ui import *
from uiflow import *
import time

setScreenColor(0xffffff)


f = None


rectangle0 = M5Rect(108, 72, 30, 30, 0xFFFFFF, 0xFFFFFF)
image0 = M5Img(59, 38, "res/afn2.jpg", True)
image1 = M5Img(59, 38, "res/afn3.jpg", True)
image2 = M5Img(59, 38, "res/afn4.jpg", True)
image3 = M5Img(59, 38, "res/afn5.jpg", True)



def buttonB_wasPressed():
  global random, f
  f = 1
  pass
btnB.wasPressed(buttonB_wasPressed)

def buttonA_wasPressed():
  global random, f
  f = 0
  pass
btnA.wasPressed(buttonA_wasPressed)


f = 1
while True:
  while f:
    image0.show()
    if not f:
      break
    wait_ms(25)
    image1.show()
    if not f:
      break
    wait_ms(25)
    image2.show()
    if not f:
      break
    wait_ms(25)
    image3.show()
    if not f:
      break
    wait_ms(25)
  wait_ms(2)
