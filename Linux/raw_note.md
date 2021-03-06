# raw note
## cmd
- scp: 远程拷贝，在没有ftp的条件下通过网络拷贝文件到目标机器上。
- file: 解释查看应用文件类型，是否可执行，动态链接还是静态连接，依赖库，版本等
- readelf：读取文件的elf信息 -d可以查看其依赖的库
- curl: 从网络上获取资源，配合bash可以执行网络上的脚本资源。
- chroot: 修改更目录路径，用于在子系统中编译
- time：后跟其他指令后，可以获取该指令执行时间
- ldd：查看应用所依赖的动态库信息
- cat：查看文件内容
    - 查看温度：cat /dev/class/thermal/temp
    - 查看CPU信息：cat /proc/cpuinfo
    - 查看系统版本： cat /proc/version
    
## other
- 遇到一个奇怪的现象，交叉编译居然比本地编译要慢，即使本地机器性能较弱。一样的源码，一样的环境（使用chroot），有如下几点怀疑：
    - 交叉编译器效率很低（两种编译器变出的可执行文件一致）
        - 验证方法也比较容易，写一个简单的程序，不依赖复杂的库，但是需要较长的编译过程，然后对比两种编译器
    - 64位机器编译32位应用本身就慢
    - 可能需要重新生成32位的库

- 建立web服务器，使用apache方案：
    - sudo apt-get install apache2
    - 重启后在主机的浏览器中输出linux机器的ip地址，即可登录主页。
    - 修改\var\www\html\index.html来更改主页内容。

### iotivity
- 增加必要的源码和库：
    - git clone https://github.com/iotivity/iotivity.git
    - git clone https://github.com/intel/tinycbor.git extlibs/tinycbor/tinycbor -b v0.5.1
    - git clone https://github.com/ARMmbed/mbedtls.git extlibs/mbedtls/mbedtls -b mbedtls-2.4.2
    - sudo apt-get install libglib2.0-dev
    - sudo apt-get install sqlite3
    - sudo apt-get install libsqlite3-dev
    - sudo apt-get install autoconf automake libtool
    - sudo apt-get install libffi-dev
    - sudo apt-get install curl libcurl3 libcurl3-dev php5-curl
