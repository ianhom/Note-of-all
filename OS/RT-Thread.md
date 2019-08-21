# RT-Thread
- RT-Thread是一款优秀国产操作系统，简称rtt。
## 散记
- msh是类似shell的交互环境，如果需要自启动或在特定位置执行某命令，可以调用函数msh_exec
- env是RTT的配置工具，可以模拟Linux的shell环境，使用menucofnig，scons，pkgs等cmd来配置需要的RTT工程
- MicroPython可以作为RTT的一个软件包运行在RTT系统上，原则上只有硬件上移植了RTT，就可以运行MicroPython
- RTT有两个版本：RTT IoT和RTT nano。nano更接近于典型的RTOS，IoT更全面。
