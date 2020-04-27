#!/bin/bash

rm -f version     #删除旧的verison文件

echo -e "THE HARDWARE VERSION:\n$1" > version  #创建新的version文件，带入版本号信息变量

cat version   # 查看version更新的内容
