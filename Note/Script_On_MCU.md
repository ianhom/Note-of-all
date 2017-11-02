# Script On MCU / 脚本语言在MCU上的应用
## 概念
- MCU（Microcontroller Unit）：微控制器单元是以控制为主（而不是计算）的微型芯片
- 脚本语言：用于执行某种操作而预先编写的流程，一般需要操作系统平台支持。

## 背景
- 脚本语言是一种、易学习、使用便捷的编程语言，例如JavaScript、python都是非常适合编程入门的编程语言。广泛应用于前端，服务器，上位机应用等领域。但其需要操作系统支持，故在资源少，速率低，实时要求高的这类嵌入式应用中很少使用脚本语言编程。而在嵌入式平台上，大多采用c/c++等编译型语言。
- 脚本语言与硬件之间还有较远的距离，一是嵌入式硬件资源有待提高，二是脚本语言对操作系统的依赖，但如果从两方面共同努力，就有可能让脚本语言直接运行在MCU这样的硬件上。

## 问题：一个Python工程师离硬件有多远
- python工程师 ---> python应用程序 ---> python解释器 ---> 操作系统 ---> 底层驱动 ---> 硬件.   
- 上述环节中，操作系统其实是可以删除的,因为操作系统主要功能是资源分配，如果没有其他程序运行，只有Python在跑，那就不需要分配资源给其他不存在的程序。
- 如果没有的操作系统的支持，那硬件上直接跑解释器就可以了，同样没有了操作系统，一些底层驱动可以更简洁一些，这样Python程序员就离硬件控制更进一步，也更便于调试。 
 
## 原理
- 在MCU上直接建立Python解释器，python应用程序直接运行在硬件上。python的库函数通过更底层语言（c或汇编），python应用可以通过这些库函数直接操作硬件。
- 目前最主流的可以运行在MCU上的python解释器是[MicroPython](https://github.com/micropython/micropython)，已在多款硬件平台上完成移植。
- 而对于板级的驱动，可以在MicroPython中编写自己的库函数，从而连接Python应用程序和硬件。
- 对于多线程的支持，可能需要RT内核的支持。
- 依然分为交互模式和脚本模式，在交互模式下可以即刻编写并执行所输入的代码，而脚本模式则对已保存的文本文件进行逐行解析
- 目前很多MCU都有很高的主频（i.mx rt 1050可达到600MHz），RAM也可以达到上百KByte，已经基础以不成长，具备条件来运行脚本语言。

## 示例
[MicroPython](https://github.com/micropython/micropython)是目前非常流行的运行在单片机上的Python解释器，符合python3语法，有很多实用的库函数供应用实用，对硬件的操作使用machine的库。同样也支持os简单文件系统、time等库        
```python 
import machine
     
machine.freq()          # get the current frequency of the CPU
machine.freq(160000000) # set the CPU frequency to 160 MHz
```

```python
import time

time.sleep(1)           # sleep for 1 second
time.sleep_ms(500)      # sleep for 500 milliseconds
time.sleep_us(10)       # sleep for 10 microseconds
start = time.ticks_ms() # get millisecond counter
delta = time.ticks_diff(time.ticks_ms(), start) # compute time difference
```
 
 ```python
from machine import Pin

p0 = Pin(0, Pin.OUT)    # create output pin on GPIO0
p0.on()                 # set pin to "on" (high) level
p0.off()                # set pin to "off" (low) level
p0.value(1)             # set pin to on/high

p2 = Pin(2, Pin.IN)     # create input pin on GPIO2
print(p2.value())       # get value, 0 or 1

p4 = Pin(4, Pin.IN, Pin.PULL_UP) # enable internal pull-up resistor
p5 = Pin(5, Pin.OUT, value=1) # set pin high on creation
```
 
 
未完待续。。。。    
---

欢迎关注我的微信公众号：**墨意MOE**    
![](../Pic/Misc/qrcode_for_gh_a64f54357afb_258.jpg)

