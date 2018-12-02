# scons
- scons是一个基于python的编译工具，与makefile类似，但更为方便，切夸平台。
- scons中Program()是最关键的函数，该函数用于编译源码
- 通过Environment（）函数可以生成环境对象，设置不同的环境参数。
    - 例如env1 = Environment(LINKFLAGS='-static')创建了环境对象，就可以通过env1.Program('hello.c')就可以静态编译hello了。    
    - 而env2 = Environment()创建了一个默认环境，则env2.Program('hello.c')则是一个动态链接的hello
