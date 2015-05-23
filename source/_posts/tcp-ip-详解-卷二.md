title: tcp ip 详解 卷二 （中文版）
date: 2015-05-22 07:28:56
categories:
  - 网络
---

![](http://img3.douban.com/lpic/s2414170.jpg)

格式：PDF
类型：文字版

<!--more-->

## 出版信息 ##

作者: 史蒂文斯 
出版社: 机械工业出版社
译者: 陆雪莹 
出版年: 2004-1
页数: 901
定价: 78.00元
丛书: TCP/IP详解（中文版）
ISBN: 9787111075677

## 简介 ##

《TCP/IP详解·卷2：实现》完整而详细地介绍了TCP/IP协议是如何实现的。书中给出了约500个图例，15000行实际操作的C代码，采用举例教学的方法帮助你掌握TCP/IP实现。《TCP/IP详解·卷2：实现》不仅说明了插口API和协议族的关系以及主机实现与路由器实现的差别。还介绍了4.4BSD-Lite版的新的特点。《TCP/IP详解·卷2：实现》适用于希望理解TCP/IP协议如何实现的人，包括编写网络应用程序的程序员以及利用TCP/IP维护计算机网络的系统管理员。

## 目录 ##

第一章 概述
1.1 引言
1.2 源代码表示
1.3 历史
1.4 应用编程接口
1.5 程序示例
1.6 系统调用和库函数
1.7 描述符
1.8 网络实现概述
1.9 mbuf与输出处理
1.10 输入处理
1.11 网络实现概述
1.12 中断级别与并发
1.13 源代码组织
1.14 测试网络
1.15 小结
第二章 mduf:存储器缓存
2.1 引言
2.2 代码介绍
2.3 mduf的定义
2.4 mduf结构
2.5 简单的mduf宏和函数
2.6 m_devget和m_pullup函数
2.7 mduf宏和函数的小结
2.8 Net/3联网数据结构小结
2.9 m_copy和簇引用记数
2.10 其他选择
2.11 小结
第三章 接口层
3.1 引言
3.2 代码介绍
3.3 ifnet结构
3.4 ifaddr结构
3.5 sockaddr结构
3.6 ifnet与ifaddr的专用化
3.7 网络初始化概述
3.8 以太网初始化
3.9 SLIP初始化
3.10 环回初始化
3.11 if_attach函数
3.12 ifinit函数
3.13 小结
第四章 接口：以太网
4.1 引言
4.2 代码介绍
4.3 以太网接口
4.4 ioctl系统调用
4.5 小结
第五章 接口：SLIP和环回
5.1 引言
5.2 代码介绍
5.3 SLIP接口
5.4 环回接口
5.5 小结
第六章 IP编址
6.1 引言
6.2 代码介绍
6.3 接口和地址小结
6.4 sockaddr_in结构
6.5 in_ifaddr结构
6.6 地址指派
6.7 接口ioctl处理
6.8 internet实用函数
6.9 ifnet实用函数
6.10 小结
第七章 域和协议
7.1 引言
7.2 代码介绍
7.3 domain结构
7.4 protosw结构
7.5 IP的domain和protosw结构
7.6 pffindproto和pffindtype函数
7.7 pfctlinput函数
7.8 IP初始化
7.9 sysctl系统调用
7.10 小结
第八章 IP：网际协议
8.1 引言
8.2 代码介绍
8.3 IP分组
8.4 输入处理：ipintr函数
8.5 转发：ip_forward函数
8.6 输出处理：ip_output函数
8.7 Internet检验和：in_cksum函数
8.8 setsockopt和getsockopt系统调用
8.9 ip_sysctl函数
8.10 小结
第九章 IP选项处理
9.1 引言
9.2 代码介绍
9.3 选项格式
9.4 ip_dooptions函数
9.5 记录路由选项
9.6 源站和记录路由选项
9.7 时间戳选项
9.8 ip_insertoptions函数
9.9 ip_pcbopts函数
9.10 一些限制
9.11 小结
第十章 IP的分片与重装
10.1 引言
10.2 代码介绍
10.3 分片
10.4 ip_optcopy函数
10.5 重装
10.6 ip_optcopy函数
10.7 ip_slowtimo函数
10.8 小结
第十一章 ICMP：Internet控制报文协议
第十二章 IP多播
第十三章 IGMP：Internet组管理协议
第十四章 IP多播选路
第十五章 插口层
第十六章 插口I/O
第十七章 插口选项
第十八章 Radix树路由表
第十九章 选路请求和选路消息
第二十章 选路接口
第二十一章 ARP：地址解析协议
第二十二章 协议控制块
第二十三章 UDP：用户数据报协议
第二十四章 TCP：传输控制协议
第二十五章 TCP的定时器
第二十六章 TCP输出
第二十七章 TCP的函数
第二十八章 TCP的输入
第二十九章 TCP的输入（续）
第三十章 TCP的用户需求
第三十一章 BPF：BSD分组过滤程序
第三十二章 原始IP
结束语
附录A 部分习题的解答
附录B 源代码的获取
附录C RFC 1122的有关内容
参考文献

## 下载 ##

+ [百度云下载](http://pan.baidu.com/s/1i3y6vEt)
+ [微盘下载](http://vdisk.weibo.com/s/aADaW4YRFwzrq)
+ [MEGA下载](https://mega.co.nz/#!XAskkCZB!MYKYyXpoqOJ_0EaP2hTc-AD1i9z7cDQBliBgxbYtIn4)