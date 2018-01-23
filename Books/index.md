# 《Python网络编程攻略》
## 第1章 套接字、IPv4和简单的客户端／服务器编程1
- 1.1 简介1 
- 1.2 打印设备名和IPv4地址2 
- 1.3 获取远程设备的IP地址4 
- 1.4 将IPv4地址转换成不同的格式5 
- 1.5 通过指定的端口和协议找到服务名6 
- 1.6 主机字节序和网络字节序之间相互转换7 
- 1.7 设定并获取默认的套接字超时时间8 
- 1.8 优雅地处理套接字错误9 
- 1.9 修改套接字发送和接收的缓冲区大小12 
- 1.10 把套接字改成阻塞或非阻塞模式13 
- 1.11 重用套接字地址14 
- 1.12 从网络时间服务器获取并打印当前时间16 
- 1.13 编写一个SNTP客户端17 
- 1.14 编写一个简单的回显客户端／服务器应用18  
## 第2章 使用多路复用套接字I／O提升性能22 
- 2.1 简介22 
- 2.2 在套接字服务器程序中使用ForkingMixIn23 
- 2.3 在套接字服务器程序中使用ThreadingMixIn25 
- 2.4 使用select.select编写一个聊天室服务器28 
- 2.5 使用select.epoll多路复用Web服务器34 
- 2.6 使用并发库Diesel多路复用回显服务器37 
## 第3章 IPv6、Unix域套接字和网络接口40 
- 3.1 简介40 
- 3.2 把本地端口转发到远程主机41 
- 3.3 通过ICMP查验网络中的主机44 
- 3.4 等待远程网络服务上线48 
- 3.5 枚举设备中的接口51 
- 3.6 找出设备中某个接口的IP地址52 
- 3.7 探测设备中的接口是否开启53 
- 3.8 检测网络中未开启的设备55 
- 3.9 使用相连的套接字执行基本的进程间通信57 
- 3.10 使用Unix域套接字执行进程间通信58 
- 3.11 确认你使用的Python是否支持IPv6套接字61 
- 3.12 从IPv6地址中提取IPv6前缀63 
- 3.13 编写一个IPv6回显客户端／服务器64 
## 第4章 HTTP协议网络编程68 
- 4.1 简介68 
- 4.2 从HTTP服务器下载数据68 
- 4.3 在你的设备中伺服HTTP请求70 
- 4.4 访问网站后提取cookie信息72 
- 4.5 提交网页表单75 
- 4.6 通过代理服务器发送Web请求77 
- 4.7 使用HEAD请求检查网页是否存在78 
- 4.8 把客户端伪装成Mozilla Firefox79  
- 4.9 使用HTTP压缩节省Web请求消耗的带宽80 
- 4.10 编写一个支持断点续传功能的HTTP容错客户端82 
- 4.11 使用Python和OpenSSL编写一个简单的HTTPS服务器84 
## 第5章 电子邮件协议、FTP和CGI编程87 
- 5.1 简介87 
- 5.2 列出FTP远程服务器中的文件87 
- 5.3 把本地文件上传到远程FTP服务器中89 
- 5.4 把当前工作目录中的内容压缩成ZIP文件后通过电子邮件发送91 
- 5.5 通过POP3协议下载谷歌电子邮件94 
- 5.6 通过IMAP协议查收远程服务器中的电子邮件95 
- 5.7 通过Gmail的SMTP服务器发送带有附件的电子邮件97 
- 5.8 使用CGI为基于Python的Web服务器编写一个留言板 99  
## 第6章 屏幕抓取和其他实用程序103 
- 6.1 简介103 
- 6.2 使用谷歌地图API搜索公司地址103 
- 6.3 使用谷歌地图URL搜索地理坐标105 
- 6.4 搜索维基百科中的文章106 
- 6.5 使用谷歌搜索股价110 
- 6.6 搜索GitHub中的源代码仓库111 
- 6.7 读取BBC的新闻订阅源114 
- 6.8 爬取网页中的链接116 
## 第7章 跨设备编程119 
- 7.1 简介119 
- 7.2 使用telnet在远程主机中执行shell命令119 
- 7.3 通过SFTP把文件复制到远程设备中121 
- 7.4 打印远程设备的CPU信息123 
- 7.5 在远程主机中安装Python包126 
- 7.6 在远程主机中运行My