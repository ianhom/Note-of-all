# scons
- scons是一个基于python的编译工具，与makefile类似，但更为方便，切夸平台。
- scons中Program()是最关键的函数，该函数用于编译源码
- 通过Environment（）函数可以生成环境对象，设置不同的环境参数。
    - 例如env = Environment(LINKFLAGS='-static')创建了环境对象，就可以通过env.Program('hello.c')就可以静态编译hello了
