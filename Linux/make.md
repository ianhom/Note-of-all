# make
## 简介
- make是用于管理编译复杂源码的脚本化工作，可以方便的编译庞大的工程
- make的基本原则如下
···
object ： requirement
  command
···
- 举例
···
main : main.c
  cc -o main main.c
···
