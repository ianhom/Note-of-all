# Sipeed dev board
- Sipeed开发板系列主要是以K210为核心的AI开发板系列，目前有
   - MAIXGO
   - MAIXDUINO
   - MAIXBIT
   - M1 Dock    
## 参考资料
- https://maixpy.sipeed.com/zh/
- http://bbs.sipeed.com/
## k210
- 400mhz
- 双核64位 risc-v
- 8mb SRAM，6mb通用，分4mb和2mb两个bank，还有2mb为kpu专用。
- 拥有kpu主流框架人工神经网络处理器，apu音频处理器
- 双核独立中断系统，7优先级，64个外部中断，可跨核触发
- 可编程io阵列
- 1.8v和3.3b电压兼容
- Dvp接口可同时输出图像到kpu和显示屏。
- 具备硬件AES加速器
- 硬件sha-256加速器
- uart分高速uart0（不支持流控）和通用型uartx，最高速率均可达到5mbps。
- 两路wdt计时器，任意起始值开始计数。可触发复位或进入中断后再复位。
- 高速GPIOHS，可以映射至FGPIOA的48个管脚中任意一个；通用型GPIO;
- I2C
- I2S
- SPI
- DMA
- TIMER

