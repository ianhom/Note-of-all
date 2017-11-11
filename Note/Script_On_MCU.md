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
 
```python
from machine import ADC

adc = ADC(0)            # create ADC object on ADC pin
adc.read()              # read value, 0-1024
```

``` python
from machine import Pin, SPI

# construct an SPI bus on the given pins
# polarity is the idle state of SCK
# phase=0 means sample on the first edge of SCK, phase=1 means the second
spi = SPI(-1, baudrate=100000, polarity=1, phase=0, sck=Pin(0), mosi=Pin(2), miso=Pin(4))

spi.init(baudrate=200000) # set the baudrate

spi.read(10)            # read 10 bytes on MISO
spi.read(10, 0xff)      # read 10 bytes while outputing 0xff on MOSI

buf = bytearray(50)     # create a buffer
spi.readinto(buf)       # read into the given buffer (reads 50 bytes in this case)
spi.readinto(buf, 0xff) # read into the given buffer and output 0xff on MOSI

spi.write(b'12345')     # write 5 bytes on MOSI

buf = bytearray(4)      # create a buffer
spi.write_readinto(b'1234', buf) # write to MOSI and read from MISO into the buffer
spi.write_readinto(buf, buf) # write buf to MOSI and read MISO back into buf 
```    

``` python
from machine import Pin, SPI

hspi = SPI(1, baudrate=80000000, polarity=0, phase=0)
```    

``` python
from machine import Pin, I2C

# construct an I2C bus
i2c = I2C(scl=Pin(5), sda=Pin(4), freq=100000)

i2c.readfrom(0x3a, 4)   # read 4 bytes from slave device with address 0x3a
i2c.writeto(0x3a, '12') # write '12' to slave device with address 0x3a

buf = bytearray(10)     # create a buffer with 10 bytes
i2c.writeto(0x3a, buf)  # write the given buffer to the slave
```  

```python
from machine import RTC

rtc = RTC()
rtc.datetime((2017, 8, 23, 1, 12, 48, 0, 0)) # set a specific date and time
rtc.datetime() # get date and time
```    

```python
import machine

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# check if the device woke from a deep sleep
if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()
```    

```python
from machine import Pin
import onewire

ow = onewire.OneWire(Pin(12)) # create a OneWire bus on GPIO12
ow.scan()               # return a list of devices on the bus
ow.reset()              # reset the bus
ow.readbyte()           # read a byte
ow.writebyte(0x12)      # write a byte on the bus
ow.write('123')         # write bytes on the bus
ow.select_rom(b'12345678') # select a specific device by its ROM code
```    

```python
import time, ds18x20
ds = ds18x20.DS18X20(ow)
roms = ds.scan()
ds.convert_temp()
time.sleep_ms(750)
for rom in roms:
    print(ds.read_temp(rom))
```    

```python
from machine import Pin
from neopixel import NeoPixel

pin = Pin(0, Pin.OUT)   # set GPIO0 to output to drive NeoPixels
np = NeoPixel(pin, 8)   # create NeoPixel driver on GPIO0 for 8 pixels
np[0] = (255, 255, 255) # set the first pixel to white
np.write()              # write data to all pixels
r, g, b = np[0]         # get first pixel colour
```   

```python
import dht
import machine

d = dht.DHT11(machine.Pin(4))
d.measure()
d.temperature() # eg. 23 (°C)
d.humidity()    # eg. 41 (% RH)

d = dht.DHT22(machine.Pin(4))
d.measure()
d.temperature() # eg. 23.6 (°C)
d.humidity()    # eg. 41.3 (% RH)
```    


未完待续。。。。    
---

欢迎关注我的微信公众号：**墨意MOE**    
![](../Pic/Misc/qrcode_for_gh_a64f54357afb_258.jpg)

