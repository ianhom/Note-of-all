
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

-------

### 关于队列
同链表一下，队列也是一个嵌入式新手容易忽略的，但却很有用的一个数据结构。

#### 队列原理
同样这里也就不再赘述队列原理，如果有空我在丰富该章节。

#### 队列的应用 ———— 缓存
在写通讯类应用的时候，经常会遇到一种情况，就是接收到一条报文，还没有来得及处理又来了一条报文。对于这种“生产速度”瞬时大于“消费速度”的情形，缓存是最常见的方法。
首先我们来定义一个简单的数组型的队列缓存    
```c
typedef struct _BUFFER
{
    uint8  *pu8Data;        /* Pointer of buffer data     */
    uint32  u32DataLen;     /* The bytes of per data      */
    uint32  u32DataCntMax;  /* The count of datas         */
    uint32  u32DataCntCur;  /* Current count of datas     */
    uint32  u32DataHead;    /* The position of first data */
}
```
一般的队列都有头位置和尾位置，头位置是最早进入队列的数据所在的位置，尾位置是下一个数据即将放入的位置，所以通过尾位置减去头位置就可以知道有多少个数据。当然这里还有一个例外，就是头尾位置相同时，可以表示队列为空，或表示队列为满。为了处理这样的误解，我们在队列的数据结构中增加一个计数器用于统计目前有多少个有效数据。每次压入准备压入新数据时，先行比较当前有效数据是否已经达到最大数，这样既可以识别队列是否为满。而头位置、尾位置和如队列的计数三者的关系本身就是知其二可得第三，所以这里设计只有头位置和计数，尾位置通过头位置+计数可获得。

----

## 软件框架   
谈到框架、架构，总会让人联想到高大上的东西，但实际上这些概念一直被我们使用，只是没有全面地了解它。软件框架不同于链表，队列这样简小且具体的概念，它更难成形描述却默默应用于我们写的代码之中。   
本章节从最简单的系统软件框架开始，循序渐进深入理解操作系统原理。重新认识目前设计框架的原理、方法和优缺点，并帮助大家逐步地理解各种操作系统多任务、同步、进程间通信等概念。   
内容：    

  序号 | 话题 | 说明
-------|-----|-----
  1    | 常用框架（轮询/前后台）及典型设计方法（状态机）| 面向基础，把原理讲透，把现有的软件设计好。   
  2    | 分时系统框架（软件定时器的实现及应用）        | 逐步提升，强化链表等实用数据结构的应用。  
  3    | 事件驱动框架                              | 重新认识事件概念，强化对现有软件设计思路。
  4    | 抢占式操作系统                            | 从以往的协作型调度向抢占型调度转变思路，通过否定再认定协作型调度的过程在深入理解现有设计模型的细节（堆、栈、资源与效率）   
  5    | 操作系统原理（任务管理、时间管理、消息机制、信号量及其他） | 进阶，通用操作系统的原理，框架、调度以外的实用组件
  6    | 简易操作系统实现                          | 实践，亲自体验各种框架的优缺与区别。    

### 常用框架（轮询/前后台）及典型设计方法（状态机）
在嵌入式系统中，C语言是最为主流的开发语言，而如何使用C语言开发功能复杂的代码，就需要使用框架来帮助设计整体的程序。常用的嵌入式框架可以分为轮询框架、前后台框架和多任务框架：   
    
**轮询框架**    
轮询框架最为简单，即只有一各主循环，在这个循环中，每个任务依次执行。这里对任务的概念进行一下说明。刚学编程的时候，我们大多没有任务的概念，所有的代码都写在一个main函数中，慢慢的随着编程熟练和功能变得复杂，我们开始学会用函数封装某些具体的操作流程，比如将按键检测写在一个Key_Input函数中，把led操作写在Led_Output函数当中，在main主函数中循环调用这两个函数。在这里我们可以把这些函数理解为任务，一个任务就是做具体的某一件事所需要的步骤，这和封装好的函数差不多。
解释完任务的概念，我们举个例子：这里有任务ABC，对应调用a(),b(),c()三个函数来执行任务。那在main函数中就是如下的写法：
```c
int main(void)
{
   while(1)   /* Loop forever */
   {
       a();   /* 执行任务A */
       b();   /* 执行任务B */
       c();   /* 执行任务C */
   }
   return 0;
}
```   
如上代码，任务ABC是依次执行并周而复始，只要每个任务执行的时间都很短，那完成一次循环的时间也很短，从宏观上感觉三个任务都是并行的（虽然微观上还是串行的）。这个就是我们最先接触也最熟悉的框架。这个框架会遇到如下的问题：    
  1. 某个任务执行时间过长或任务中有长时间的等待（while/for之类的长时间循环）将会影响其他任务的执行。    
  2. 外部事件是随机产生的，产生时对应的任务可能刚刚执行完成，错过了对事件响应和处理的时机，必须等待下次循环再进行处理。    
  
从实时性能角度上来看，轮询框架在实时性上没有天然的保证，必须由开发人员处理好每个任务，让任务必须在短时间内执行完成，才能使该框架正常工作。状态机就是一种有效的设计方法，在后面的章节中我们将详细讲解下状态机的运用。    
    
    
**前后台框架**    
前后台框架在轮询基础上引入了中断来响应事件。循环执行的主程序为后台，一个或多个响应事件的中断为前台。当事件发生时，由前台中断先行响应，若对事件的处理较多，则中断仅记录事件状态，进行标记，退出中断后再由后台主循环中检查标记进行处理。若对事件的处理较少，可以在中断中直接处理完。前后台框架可以在事件发生时打断主循环的运行，并通过中断来响应事件，大大提高了对事件响的应实时性。    
优点：实时性得到一定提升；缺点：事件得到实时响应，但处理依旧还是轮询方式。
    
    
**多任务框架**    
多任务框架又在前后台框架之上，从实时性角度进一步进行改进。在这一框架之下，主循环程序被改造成对事件敏感，或称为“事件驱动”。在之前所述的后台系统不再是对每一个任务进行轮询，在任务中通过状态机检查自己是否需要执行何种操作。改造后的后台系统检查是否有事件发生，这个事件是给哪个任务的，然后就直接调用那个任务对事件进行处理。这里最大的不同，就是对事件判断的工作从任务中剥离，交由调度任务的上层框架来处理，    


## 状态机    
### 为什么使用状态机        
c语言是面向过程的语言，它更多地描述的是处理一个事情的流程。比如我们定义一个任务A，执行A1，A2步骤，等3秒后执行A3步骤，这就是一个操作的过程。但往往实现一个应用不仅仅只有一个过程，比如我们还有一个任务B，执行B1，等待3秒后执行B2，B3，这样我就有了两个并行的任务，因为这两个任务中都有较长时间的操作（等待3秒），所以我们无法直接通过把任务AB串行来实现微观串行，宏观并行的效果。如果我们有支持多线程环境，操作系统会自然地帮我们把两个任务做切分，这样编写任务AB的程序员就不需要考虑独占CPU而造成堵塞的情况。但在大部分的资源受限的MCU环境下是不支持多线程环境的，那就需要程序员寻求一种方法来分割任务的过程，最常用的方法就是状态机。    

### 如何使用状态    
在无多线程支持的环境中，对任务进行状态分割，每次进入都有一个当前状态，每个状态下有对应的处理。   　　　　
**经典的switch**    
上面的描述很容易联想到C语言中switch语句——switch一个状态变量，跳转到对应的分支，就可以进行相应的处理。    
```c
/**************************************************************************************
                 ________                             _____________ ________ 
                         |  Debounce |               |  Debounce   |
                   Idle  | Press PRE |   Pressed     | Release Pre |  Idle         
                         |           |               |             |    
                         |___________|_______________|             |
                         |           |               |             |
                         V           V               V             V
                    Press Evt    Pressed Evt   Short release Evt   Short release Evt
****************************************************************************************/
swtich(u8St)
{
    case BTN_IDLE_ST:
        .....
        if(BTN_PRESS)
            u8St = BTN_PRESS_PRE_ST;
        break;
    case BTN_PRESS_PRE_ST:
        ....
        if(BTN_PRESS)
        {
            if(TIME_UP)
                u8St =BTN_PRESSED_ST;
        }
        else
            u8St = BTN_IDLE_ST;
        break;
    case BTN_PRESSED_ST:
        ....
        if(BTN_RELEASE)
            u8St = BTN_RELEASE_PRE_ST;
        break;
    case BTN_RELEASE_PRE_ST:
        if(BTN_RELEASE)
        {
            if(TIME_UP)
                u8St = BTN_IDLE_ST; 
        }
        else
            u8St = BTN_PRESSED_ST;
        break;
}

```    
**改良的状态转移表**       
每次的状态切换都会明确指定下一次状态，如果我们对状态进行整理排序，通过一个数组来将下一次的状态整理好，那整体的处理流程将更为清晰。

```c
/**************************************************************************************
                 ________                             _____________ ________ 
                         |  Debounce |               |  Debounce   |
                   Idle  | Press PRE |   Pressed     | Release Pre |  Idle         
                         |           |               |             |    
                         |___________|_______________|             |
                         |           |               |             |
                         V           V               V             V
                    Press Evt    Pressed Evt   Short release Evt   Short release Evt
****************************************************************************************/

const uint8 cg_aau8StateMachine[BTN_STATE_NUM][BTN_TRG_NUM] = 
{
    /*  Situation 1  */   /*  Situation 2 */   /*  Situation 3  */    /* Situation 4  */
    /* Btn NOT press */   /* Btn press    */   /* Btn NOT press */    /* Btn press    */
    /* Time NOT out  */   /* Time NOT out */   /* Time out      */    /* Time out     */
    {BTN_IDLE_ST       , BTN_PRESS_PRE_ST    , BTN_IDLE_ST         , BTN_PRESSED_PRE_ST},  /* BTN_IDLE_ST        */  
    {BTN_IDLE_ST       , BTN_PRESS_PRE_ST    , BTN_IDLE_ST         , BTN_PRESSED_ST    },  /* BTN_PRESS_PRE_ST   */
    {BTN_RELEASE_PRE_ST, BTN_PRESSED_ST      , BTN_RELEASE_PRE_ST  , BTN_PRESSED_ST    },  /* BTN_PRESSED_ST     */
    {BTN_RELEASE_PRE_ST, BTN_PRESSED_ST      , BTN_IDLE_ST         , BTN_PRESSED_ST    }   /* BTN_RELEASE_PRE_ST */
};

     switch(u8BtnSt)
     {
         case BTN_IDLE_ST:
             ....
             break;
         case BTN_PRESS_PRE_ST:
             ....
             break;
         ...
     }

    /*************************** Find the Next state ***************************/
    /* Check if button is press or NOT */
    if(u8BtnSt != ptBtnPara->u8NormalSt)
    {   /* If button is pressed, update index number  */
        u8NextSt++;
    }
    
    /* Check if the debounce or long-press time is out or NOT */
    if(u8TmOut)
    {   /* If time is out, update index number */
        u8NextSt += BTN_TM_TRG_EVT_OFFSET;
    }
    u8BtnSt = cg_aau8StateMachine[u8BtnSt][u8NextSt];
```
    
**高效的函数指针数组**    
switch的原理其实是很多个if，越靠后的case则与靠后进行if判断。这里的判断类似于挨家挨户的询问，知道询问的case为想要的状态。既然我们都已经知道了状态，为何不能像数组一样直接索引到具体的状态的操作呢？我们当然可以，而且我们使用的也正是数组。    
在switch的方案中，每个case内的代码就是当前状态下的操作。    
```c
switch(u8State)
{
    case STATE_A:         /* State A */
    {
        a1();             /* State A下的操作1 */
        a2();             /* State A下的操作2 */
        a3();             /* State A下的操作3 */
        StateUpate();     /* 更新状态         */
        break;
    }
    case STATE_B:         /* State B */
    {
        b1();             /* State B下的操作1 */
        b2();             /* State B下的操作2 */
        b3();             /* State B下的操作3 */
        StateUpate();     /* 更新状态         */
        break;
    }
    case STATE_C:         /* State C */
    {
        c1();             /* State C下的操作1 */
        c2();             /* State C下的操作2 */
        c3();             /* State C下的操作3 */
        StateUpate();     /* 更新状态         */
        break;
    }
    default:              /* 异常情况         */
    {
        break;
    }
}
```

如果我们把这段代码封装成函数
```c
void State_A(void)    /* State A的操作函数 */
{
    a1();             /* State A下的操作1 */
    a2();             /* State A下的操作2 */
    a3();             /* State A下的操作3 */
    StateUpate();     /* 更新状态         */
}

void State_B(void)    /* State B的操作函数 */
{
    b1();             /* State B下的操作1 */
    b2();             /* State B下的操作2 */
    b3();             /* State B下的操作3 */
    StateUpate();     /* 更新状态         */
}

void State_C(void)    /* State C的操作函数 */
{
    c1();             /* State C下的操作1 */
    c2();             /* State C下的操作2 */
    c3();             /* State C下的操作3 */
    StateUpate();     /* 更新状态         */
}

switch(u8State)
{
    case STATE_A:         /* State A */
    {
        State_A();
        break;
    }
    case STATE_B:         /* State B */
    {
        State_B();
        break;
    }
    case STATE_C:         /* State C */
    {
        State_C();
        break;
    }
    default:              /* 异常情况         */
    {
        break;
    }
}
```    
这样的替换感觉有点多余，但实际上想替换的是switch，我们再做一下修改。
```c
typedef void (*PF_STATE)(void);

void State_A(void)    /* State A的操作函数 */
{
    a1();             /* State A下的操作1 */
    a2();             /* State A下的操作2 */
    a3();             /* State A下的操作3 */
    StateUpate();     /* 更新状态         */
}

void State_B(void)    /* State B的操作函数 */
{
    b1();             /* State B下的操作1 */
    b2();             /* State B下的操作2 */
    b3();             /* State B下的操作3 */
    StateUpate();     /* 更新状态         */
}

void State_C(void)    /* State C的操作函数 */
{
    c1();             /* State C下的操作1 */
    c2();             /* State C下的操作2 */
    c3();             /* State C下的操作3 */
    StateUpate();     /* 更新状态         */
}

PF_STATE apfState[3] = {State_A, State_B,State_C};

while(1)
{
    apfState[u8State]();   /* 执行状态机 */
}

```    

```c
/**************************************************************************************
                 ________                             _____________ ________ 
                         |  Debounce |               |  Debounce   |
                   Idle  | Press PRE |   Pressed     | Release Pre |  Idle         
                         |           |               |             |    
                         |___________|_______________|             |
                         |           |               |             |
                         V           V               V             V
                    Press Evt    Pressed Evt   Short release Evt   Short release Evt
****************************************************************************************/
typedef void (*PF_STATE)(void);

void Btn_Idle(void){....};
void Btn_Press_Pre(void){....};
void Btn_Pressed(void){....};
void Btn_Release_Pre(void){....};

PF_STATE apfState[4] = {Btn_Idle, Btn_Press_Pre, Btn_Pressed, Btn_Release_Pre};

while(1)
{
    apfState[u8State]();   /* 执行状态机 */
}

```
这样就从switch逐个case的判断，转换为函数指针数组直接的调用。在case比较多的情况下，执行效率会高很多，但是这里没有了default分支，所以在状态更新的时候，需要特别注意异常状态。

----
## 编译
用习惯IDE的同学对编译的理解就是一个按钮，而实际上这个按钮的背后有很多细节，可以分为“预处理、编译、汇编、链接”四个阶段    
### 预处理     
在预处理阶段，将对C源码进行一次替换处理，形成最终的“源文件”。与预处理阶段相关的操作有#define，#include，#if,#ifdef等。下面举一个简单的例子：    
头文件Head.h
```c
#define A 20
#define B 10
#define OPERATION_ADD 
```    
源文件main.c
```c
#include "Head.h"
int main(void)
{
#ifdef OPERATION_ADD
    int c = A + B;
#else
    int c = A - B;
#endif
    return c;
}
```
在预处理中先对main.c源文件进行include
```c
#define A 20
#define B 10
#define OPERATION_ADD 
int main(void)
{
#ifdef OPERATION_ADD
    int c = A + B;
#else
    int c = A - B;
#endif
    return c;
}
```
然后对main.c源文件进行条件编译
```c
#define A 20
#define B 10
#define OPERATION_ADD 
int main(void)
{
    int c = A + B;
    return c;
}
```
最后再对main.c源文件进行宏定义替换，我们就获得了真正的用于后续编译的源文件了。
```c
int main(void)
{
    int c = 20 + 10;
    return c;
}
```
### 编译
这里的编译不是我们平常理解的宏观定义（完成的预处理、编译、汇编、链接），而是更明确的“由C转换会汇编”的过程。这里几乎所有的操作都有编译器完成，由编译器决定如何将源码的c语句转换成汇编指令。当然程序员对转换的结果有一定的控制，这时就需要关注如const，volatile，static等修饰词，同时还有编译器优化等级和偏向这些要素来影响最终的汇编指令。经过编译器的的编译处理，我们上述的源代码将会转换成如下的汇编指令。    
```asm
    MOV R1,#20
    MOV R2,#10
    ADD R0,{R1,R2}
```

### 汇编
经过上面的编译处理，C语言已经变成更为底层的汇编语句了，但是汇编代码不是最终执行的机器代码，众所周知机器只知道0和1，所以我们还需要对人类依旧可读的汇编语句进行处理转换成机器码，这个操作就叫汇编。    

### 链接
这个时候，几乎所有的代码基都转换成了机器码，但这些机器码还没有地址。所以需要连接器Linker来根据芯片的资源和代码中指定的地址或分区来为各个汇编好的机器码分配地址。当每个函数都有入口地址后，代码中的函数调用也就可以填写对应的地址来实现调用，文件之间的关联。

### 库
库是某些源文件，经过预处理、编译和汇编之后的文件集合，在库中已经无法看到C源码的具体实现，但依旧可以和其他C源码一同开发，在链接的时候融合成一个hex或bin。

未完待续。。。。
