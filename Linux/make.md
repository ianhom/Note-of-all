# make
## 简介
- make是用于管理编译复杂源码的脚本化工作，可以方便的编译庞大的工程
- make的基本原则如下
```
object ： requirement
  command
```
- 举例
```
main : main.c
  cc -o main main.c
```
- main是我们要生成的目标可执行文件，需要使用main.c这个源文件，我们通过cc指令（gcc）来将main.c源码编译成main可执行文件。
- make也有自动推导功能，可以免去繁琐的重名
- make命令首先找当前文件夹下的makefile和Makefile文件，然后按照文件中的脚本内容开始执行。
