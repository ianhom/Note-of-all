本文档用于记录项目学习过程中的相关参考、笔记及总结

## **8th Nov 2016**
最终我们选择了FriendlyARM的NanoPi-NEO作为硬件平台，该平台功能、资源丰富、性价比极高，利于项目开发和传播。   
软件平台是H3制造商全志提供的lichee工程包，lichee包含了linux源码、编译器、众多驱动及强大实用的编译脚本，可以快速实现u-boot，内核和文件系统的全套编译。   
### **开发环境搭建**
  1. 在PC机上安装Ubuntu 14.04 LTS-64bit（推荐虚拟机安装）；
  2. 更新ubuntu14.04: `sudo apt-get install gawk git gnupg flex bison gperf build-essential zip curl libc6-dev libncurses5-dev:i386 x11proto-core-dev libx11-dev:i386 libreadline6-dev:i386 libgl1-mesa-glx:i386 libgl1-mesa-dev g++-multilib mingw32 tofrodos python-markdown libxml2-utils xsltproc zlib1g-dev:i386 u-boot-tools`
  3. 下载lichee源码： `git clone https://github.com/friendlyarm/h3_lichee.git lichee`   
  4. 编译linux内核： `./build.sh -p sun8iw7p1 -b nanopi-h3 -m kernel`

## **16th Nov 2016**
lichee中有很多成熟的驱动程序，其中就包括了DHT11模块。我们先使用该模块研究驱动如何以文件的形式呈现，如何操作这些文件。   
根据友善之臂提供的matrix源码，我们可以一步步找到DHT11的驱动文件在哪里，是如何操作。首先，下载matix源码到NEO后，按照要求编译，使用“Matrix-temp_humidity”命令就可以获得温度和湿度，于是在友善的matrix源码中搜索相同的关键字，可以找到[Matrix-temp_humidity.C](https://github.com/friendlyarm/matrix/blob/ceaf84299a69e1334df62029c78a8e784eb84a9a/demo/matrix-temperature_and_humidity_sensor/Matrix-temp_humidity.c)文件，该文件就是调用DHT11驱动的应用文件（c语言编写），有以下几点我们着重看一下：
* sprintf()是将一部分字符串使用printf类似的风格“打印”到一个内存区，不是打印到屏幕，而是将这些字符串复制到一个内存区域中。
* system()比较特殊，参数是个字符串，作用是将字符串的内容作为shell中的指令在shell执行。结合上面的sprintf可以看出，这个c文件使用这样的方式在shell中调用了“modprobe DHT11”命令——即加载了DHT11的驱动。   
* 后面紧接着调用了dht11Read()函数变得到了温湿度的值，也就是说这个在这个操作中涉及到了驱动对应的文件。搜索关键字dht11Read，我们可以在[iio.c](https://github.com/friendlyarm/matrix/blob/ceaf84299a69e1334df62029c78a8e784eb84a9a/lib/iio.c)(industry input/output)文件中找到dht11Read函数的具体实现。进而我们找到了DHT11温湿度传感器的相关文件**“/sys/devices/platform/dht11/in_humidityrelative_input”**及**“/sys/devices/platform/dht11/in_temp_input”**，分别对应的是湿度及温度。（P.S:这两个文件是在DHT11驱动加载后才出现的）。   
* 找到文件之后，我们再来看这些文件是如何操作的，程序调用了readIntValueFromFile函数，继续搜索可知该函数在[common.c](https://github.com/friendlyarm/matrix/blob/ceaf84299a69e1334df62029c78a8e784eb84a9a/lib/common.c)中，在这个函数的具体实现中使用了c的文件操作函数fopen，fread，及fclose对文件进行了打开、读取及关闭操作，进而得到了我们所需要的温湿度值。这里需要注意的是，这里从文件读出来的不是整形数值，而是ascii字符串，也就是说温湿度值是以文本的形式存于文件之中，读取文件后，需要根据实际应用进行转换。   
   
至此，我们知道了的DHT11驱动以文件形式存于何处，和如何操作这个文件的方法，随后我们使用c及python分别写了简单的应用程序读取了温湿度，试验成功。
