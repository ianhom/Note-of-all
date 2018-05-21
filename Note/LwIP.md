# LwIP学习笔记
## 简介
- LwIP是指轻量级的IP协议栈，非常适合于嵌入式设备进行IP通讯。可以裸奔，亦可和操作系统一起使用。最新的2.0.3版本已经支持IPv6，MQTT等物联网特性。
- LwIP有一个操作系统适配层，可以方便的适配各种RTOS，例如uCos、FreeRTOS、LiteOS等。
- 作为一款成熟的IP协议栈，除了要实现复杂的IP协议功能，同时需要提供简介的API，LwIP提供了三种API：Raw API、Sequential API and Socket API
    - Raw API是一种基于CallBack机制的、适合裸编的API
    - Sequential API适合上操作系统
    - Socket API同样适合操作系统，是对Sequential API的一种Socket封装，好处是跟接近于Socket编程，缺点是效率要比Sequential API低。
## 源码架构

## 内核

## To be continued...
