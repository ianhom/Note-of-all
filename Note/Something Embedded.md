
# 嵌入式软件工程师学习笔记

## 目标
本文档记录一些本人嵌入式学习过程的经验总结，旨在帮助大家更好地学习嵌入式软件知识！

## 散记
### 关于链表
链表对于学纯软件的工程师而言是个非常简单的概念，但对于嵌入式软件工程师，因为面对都是资源受限的MCU的平台，难得有机会使用这样“高大上”的数据结构，所以回觉得陌生。但随着MCU的发展，主频和储存都在不断扩大，嵌软工程师们也开始不断尝试更复杂的数据结构或软件模型。链表就是一个最典型的需要了解的数据结构，因为由它展开的应用非常多，也非常实用。

#### 链表原理
对于链表的原理在这里暂不描述，网上资源很多，以后有机会再补充该章节

#### 链表的应用 —— 软件定时器
因为链表本身是一种逻辑上连续，空间上不要求连续的数据结构，所以链表可以灵活的增加或缩短。对于这个特性，在嵌入式中用于软件定时器模块是非常合适的。    
在软件定时器中，链表结构中除了指向下一个节点的ptNext， 还需要两个关键成员：1、软件定时器节点启动的时间点OldTime；2、软件定时器定时时间Period。有了这两个变量，结合我们的当前时间点CurrentTime，就可以知道一个定时时间有没有到期（CurrentTime - OldTime > Period）。    
下面的代码定义了一个最简单定时器节点。
```C
typedef sturct _T_TIMER
{
    struct _T_TIMER  *ptNext;  /* Address of next node  */
    uint32 u32OldTm;           /* The start time point  */
    uint32 u32Period;          /* The delay time period */
}T_TIMER；
```

下面我们尝试丰富一下这个定时器的功能。    
很多和定时相关的功能并不是只定时一次的，而是采用周期的方式，那我们就需要增加一个变量，用以表示周期性计时和单次计时的差别。对上述节点定义做如下修改    
```C
typedef sturct _T_TIMER
{
    struct _T_TIMER  *ptNext;   /* Address of next node           */
    uint32 u32OldTm;            /* The start time point           */
    uint32 u32Period;           /* The delay time period          */
    uint16 u16Count;            /* The count for repeating timing */
}T_TIMER；
```

如果u16Count的值为1，那就是单次触发，触发完就可以删除该节点。如果0，那这里可以表示永远重复计时，时间一到就重新启动。    
但是这里为什么要定义一个u16类型呢，一个BOOL型的变量不就足够了吗？相信聪明的读者已经发现了，其实我们不经可以做单次触发和无限制触发，我们还可以设定触发次数，比如u16Count的值为10次，那这个定时器就可以计10的相同周期时间。    

至此，一个软件定时器模块所需要的数据结构就定义好了，结构中的成员是定时功能所需要的信息，其实我们可以增加更多成员，来构建更有趣的功能。    
定时器计时结束可以视为一个事件发生（定时时间到事件），一般情况下对这个事件有相应的操作，比如定时结束就点亮LED，关闭风扇等等。如果我们将此类和某个定时器相关的操作也放进定时器节点中会怎样呢？
```C
typedef uint32 (*PF_TIMER_CB)(void *p);  /* Callback function when time is up */

typedef sturct _T_TIMER
{
    struct _T_TIMER  *ptNext;   /* Address of next node              */
    PF_TIMER_CB pfTmCb;         /* Callback function when time is up */
    uint32 u32OldTm;            /* The start time point              */
    uint32 u32Period;           /* The delay time period             */
    uint16 u16Count;            /* The count for repeating timing    */
}T_TIMER；
```
这里设置无限次重触发，在每次定时结束后就执行一次pfTmCb回调函数，那就可以构建一个基于时间轮片的多任务框架。

下面我们再进一步，在多任务嵌入式操作系统中的时间管理模块，就会使用类似于上述的数据结构，但是还需要一个变量，用于标记与该定时器相关联的任务编号。
```C
typedef uint32 (*PF_TIMER_CB)(void *p);  /* Callback function when time is up */

typedef sturct _T_TIMER
{
    struct _T_TIMER  *ptNext;   /* Address of next node              */
    PF_TIMER_CB pfTmCb;         /* Callback function when time is up */
    uint32 u32OldTm;            /* The start time point              */
    uint32 u32Period;           /* The delay time period             */
    uint16 u16Count;            /* The count for repeating timing    */
    uint16 u16TaskId;           /* The ID of destination task        */
}T_TIMER；
```
上述的结构体成员需要注意排序的问题，在主流的32位MCU中注意4字节对齐问题。

### 关于队列
同链表一下，队列也是一个嵌入式新手容易忽略的，但却很有用的一个数据结构。
#### 队列原理
同样这里也就不再赘述队列原理，如果有空我在丰富该章节。

#### 队列的应用 ———— 缓存

未完待续。。。。
