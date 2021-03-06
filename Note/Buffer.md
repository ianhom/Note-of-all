# 缓存设计
- 在嵌入式开发中，经常会遇到消费跟不上生产的情况，这时就需要缓存来对短时突发生产出来的数据进行缓冲，带消费者慢慢消化。
- 简单的缓存模型使用队列结构即可，突发产生的事件都保存在队列中，然后应用从队列中获取事件并消费。
- 事件可以是信号量、标志，也可以是报文数据，如果是报文数据，这里就有可能存在数据搬移的问题。
- 大量的内存拷贝对嵌入式而言是影响效率的存在，需要重新设计
- 解决内存拷贝需要解决的时候多个缓存中数据交换的方式，如果缓存中保存的是数据本身，那从一个缓存到另一个缓存就需要内存的拷贝。所以基本思路是缓存中不保存数据本身，而是指向数据的指针，这样只需要交换指针就可以实现数据交换。
- 但这样同时会带来其他问题。比如，缓存A到缓存B，数据指针是交换了，这时数据对A而言就是已经消费掉了，但是B正在消费这个数据，所以不能在A消费过后就处理掉数据，需要判断B是否完成消费，及是否数据还需要继续使用来决定。
- 在这里可以使用链表来记录哪些内存块是正在使用的，哪些可以free掉，这样可以就有了机制保证数据在在消费前都能保持有效。

## 实现方式1
- 申请一个内存块，这个内存块中分配n个条目，每个条目保存一条数据。创建两个链表，一个用于保存有效数据，一个用于保存空闲数据。
- 初始的时候，所有的内存条目都保存在空闲链表上，有效链表是空的。
- 当有数据数据需要入队列A时，就从空闲链表上取一个使用，并把其放到有效链表上。从队列A到队列B，仅仅做地址的交换，其数据仍在有效链表上。当队列B也消费完成数据后，即可把改条目从有效链表上转移到空闲链表上，以便后用。

```c
/* Define of Queue structure */
typedef struct _T_Q
{
    unsigned int u32Head;
    unsigned int u32Tail;
    unsigned int u32Cnt;
    unsigned int u32Max;
    unsigned int *pu32Data;
}T_Q;

typedef struct _T_NODE
{
    struct _T_NODE *ptNext;
    unsigned int pu32Data;
}T_NODE;

typedef struct _T_HEAD
{
    unsigned char      u8Used;  /* Used or available   */
    unsigned char      u8No;    /* Belong to which one */
    unsigned short int u16Len;  /* Length of used data */
}T_HEAD;

typedef struct _T_EASY_HEAD
{
    unsigned short int u16Len;  /* Length of used data. 0 means NOT used */
}T_EASY_HEAD;

static T_Q sg_tQA，sg_tQB;
static T_NODE sg_tLinklistUsed,sg_LinkListEmpty;
```

## 实现方式2
- 同方式1，申请一个内存块，划分n个条目，每个条目保存一条数据，同时还做一个标记，用以标识该数据是否有效。每个条目的size相同，所以查找空闲内存只需固定偏移来查找标记即可。
- 这种方式有个弊端，就是数据块固定，意味着存在浪费（但对于报文接收这种有固定长度的需求，影响相对较小）；同时查找时间不固定。

## 实现方式3
- 基本同方式2，使用malloc来申请内存条目，在改条目中依旧使用标记。
- 采用这样的方式可以解决方式2中的使用相同size的内存而造成的内存浪费问题。
- 但这样malloc和free容易产生碎片，动态分配的过程也会花费时间。
- 这里要特别注意数据长度，其实上述几种方法中数据都要求保存长度，否则访问信息不足，尤其是malloc的方式，越界方位会破坏malloc空间的下一个头部信息，不仅仅破坏了内存块，堆空间的使用也会遭到严重的破坏。


## 实现方式4
- to be done
