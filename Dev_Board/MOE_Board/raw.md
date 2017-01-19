# MOE board project    
- 板载CMSIS-DAP仿真器，仿真器可独立工作    
- 单个usb实现供电，下载，仿真，虚拟串口，U盘拷贝式烧写程序    
- 大容量MCU 5186TEV    
- 支持系统:各类rtos，MOE，各类脚本解释器
- Arduino接口兼容，排针双支持
- 星空配色
- 卡片size = 86 * 54 mm

# 关于Arduino接口
- Arduino接口是非常流行的接口，Arduino爱好者本身就很多，很多开发板也愿意支持该接口（st的Nucleo系列，Freescale的FRDM系列）。这同样引导了很多有趣功能丰富的扩展板支持Arduino接口。 我以前遇到一个问题，就是FRDM系列的开发板和对应的扩展板，都没有焊上排针排母，一般习惯是在开发板上焊排针，但这样就无法使用同样为排针的Arduino扩展。为了解决这个问题，MOE板将设计Arduino的排针+排母的接口，方便大家使用。
