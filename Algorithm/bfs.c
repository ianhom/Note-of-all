
#include<stdio.h>
#include<stdlib.h>
 
#define MAX 10
#define INFINITY 65535
#define TRUE 1
#define FALSE 0
 
typedef char VertexType;
typedef int EdgeType;
 
typedef int Boole;  //布尔类型 存储TRUE FALSE
Boole visited[MAX];    //访问标志数组 
 
typedef int QElemType;    //链队列的数据类型 
typedef int Status; 
 
 
/*邻接矩阵结构*/ 
typedef struct
{
	VertexType vexs[MAX];   //顶点表 
	EdgeType arc[MAX][MAX];   //邻接矩阵 可看作边表   
	int numVertexes,numEdges;   //顶点数和边数 
}MGraph;
 
/*队列结构*/
typedef struct QNode
{
	QElemType data;
	struct QNode *next;
}QNode,*QueuePtr;
 
typedef struct
{
	QueuePtr front,rear;  //队头队尾指针 
}LinkQueue;
 
 
//构造邻接矩阵
void create(MGraph *G)
{
	int i,j,k,w;
	printf("请输入顶点数和边数:\n");
	scanf("%d%d",&G->numVertexes,&G->numEdges);
	fflush(stdin);
	for(i=0;i<G->numVertexes;i++)     //建立顶点表
	{ 
		printf("\n第%d个顶点",i+1);
		scanf("%c",&G->vexs[i]);
		getchar();
	}
	
	for(i=0;i<G->numVertexes;i++)   //矩阵初始化 
		for(j=0;j<G->numVertexes;j++)
			G->arc[i][j]=INFINITY;
			
	for(k=0;k<G->numEdges;k++)
	{
		printf("输入边（Vi,Vj）的上下标i,j和权w(空格隔开)：");
		scanf("%d%d%d",&i,&j,&w);
		G->arc[i][j]=w;
		G->arc[j][i]=G->arc[i][j];
	}			 
} 
 
  //输出邻接矩阵 
void Output(MGraph *G)   
{
	int i,j,count=0;
	for(i=0;i<G->numVertexes;i++)
		printf("\t%c",G->vexs[i]);
	printf("\n");
	for(i=0;i<G->numVertexes;i++)
	{
		printf("%4c",G->vexs[i]);
		for(j=0;j<G->numVertexes;j++)
		{	
			
				printf("\t%d",G->arc[i][j]);
				count++;
				if(count%G->numVertexes==0)
				printf("\n");	
		} 
    }	 
 } 
 
 
//创建空队列
Status InitQueue(LinkQueue &Q)
{
	Q.front=Q.rear=(QueuePtr)malloc(sizeof(QNode));
	if(!Q.front)
		exit(0);
	Q.front->next=NULL;
	return 1;	
} 
 
//入队列
//将s作为新元素加入队尾 
Status EnQueue(LinkQueue &Q,int i)
{
	QueuePtr s;
	s=(QueuePtr)malloc(sizeof(QNode));
	if(!s)
		exit(0);
	s->data=i;
	s->next=NULL;
	Q.rear->next=s;
	Q.rear=s;
	return 1;	
}
 
//检验是否为空
Status QueueEmpty(LinkQueue Q)
{
	if(Q.front->next==NULL)
		return 0;
	else
		return 1;	
 } 
 
//出队列
Status DeQueue(LinkQueue *Q,int *i)
{
	QueuePtr p;
	if(Q->front==Q->rear)
		return 0;
	p=Q->front->next;     //该写法值得商榷
						//相当于p储存第一个结点
	*i=p->data;
	Q->front->next=p->next;
	
	if(p==Q->rear)   //若队头是队尾	,删除后将rear指向头结点		
		Q->rear==Q->front;
	free(p);
	return 1;			
 } 
 
 
 
/*广度遍历*/ 
void BFSTraverse(MGraph G)
{
 
	int i,j;
	LinkQueue Q;
	for(i=0;i<G.numVertexes;i++)
		visited[i]=FALSE;
	InitQueue(Q);          //&的用法??     初始化队列    
	for(i=0;i<G.numVertexes;i++)
	{
		if(!visited[i])    //未访问过 该顶点 
		{
			visited[i]=TRUE;
			printf("%c->",G.vexs[i]);
			EnQueue(Q,i);      //将其入队列 
			while(!QueueEmpty(Q))
			{
				DeQueue(&Q,&i);    //将队中元素出队列，赋值给i 
				for(j=0;j<G.numVertexes;j++)
				{
					if(G.arc[i][j]==1&&!visited[j])      //其他顶点与该顶点存在边   且未访问过 
					{
						visited[j]=TRUE;
						printf("%c",G.vexs[j]);
						EnQueue(Q,j);                 //入队列 
					}
					
				} 
			} 
		}
	}
} 
 
 
int main()
{
	MGraph G;
	create(&G);
	printf("邻接矩阵数据如下：\n");
	Output(&G);
	printf("\n");
	BFSTraverse(G); 
	printf("\n图遍历完毕");
	return 0;	 
	
}
