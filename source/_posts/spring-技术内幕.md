title: spring技术内幕（第2版）
date: 2015-11-14 10:28:36
categories:
  - spring
---

![](http://img3.doubanio.com/lpic/s28047189.jpg)

格式：EPUB
类型：文字版

<!--more-->

## 出版信息 ##

作者: 计文柯 
出版社: 机械工业出版社
副标题: 深入解析Spring架构与设计原理
出版年: 2012-2
页数: 399
定价: 69.00元
装帧: 平装
ISBN: 9787111365709

## 简介 ##

《spring技术内幕：深入解析spring架构与计原理(第2版)》是国内唯一一本系统分析spring源代码的著作，也是spring领域的问鼎之作，由业界拥有10余年开发经验的资深java专家亲自执笔，java开发者社区和spring开发者社区联袂推荐。本书第1版不仅在内容上获得了读者的广泛好评，而且在销量上也摘取了同类书的桂冠，曾经一度掀起java类图书的销售热潮。第2版不仅继承了第1版在内容组织和写作方式上的优点，而且还根据广大读者的反馈改进了若干细节上的不足。更为重要的是，结合spring的最新版本对过时的内容进行了更新，并增加了大量新内容，使本书更趋近于完美。
《spring技术内幕：深入解析spring架构与计原理(第2版)》从源代码的角度对spring的内核和各个主要功能模块的架构、设计和实现原理进行了深入剖析。你不仅能从本书中参透spring框架的优秀架构和设计思想，还能从spring优雅的实现源码中一窥java语言的精髓。本书在开篇之前对spring的设计理念和整体架构进行了全面的介绍，能让读者从宏观上厘清spring各个功能模块之间的关系；第一部分详细分析了spring的核心：ioc容器和aop的实现，能帮助读者了解spring的运行机制；第二部分深入阐述了各种基于ioc容器和aop的java ee组件在spring中的实现原理；第三部分讲述了acegi安全框架、dm模块以及flex模块等基于spring的典型应用的设计与实现。
无论你是java程序员、spring开发者，还是平台开发人员、系统架构师，抑或是对开源软件源代码着迷的代码狂人，都能从本书中受益。

## 目录 ##

前言
第1章　spring的设计理念和整体架构 / 1
1.1　spring的各个子项目 / 2
1.2　spring的设计目标 / 5
1.3　spring的整体架构 / 7
1.4　spring的应用场景 / 10
1.5　小结 / 12
第一部分　spring核心实现篇
第2章　spring framework的核心：ioc容器的实现 / 16
2.1　spring ioc容器概述 / 17
2.1.1　ioc容器和依赖反转模式 / 17
2.1.2　spring ioc的应用场景 / 18
2.2　ioc容器系列的设计与实现：beanfactory和applicationcontext / 19
2.2.1　spring的ioc容器系列 / 19
2.2.2　spring ioc容器的设计 / 21
2.3　ic容器的初始化过程 / 28
2.3.1　beandefinition的resource定位 / 29
2.3.2　beandefinition的载入和解析 / 37
2.3.3　beandefinition在ioc容器中的注册 / 52
.2.4　ioc容器的依赖注入 / 54
2.5　容器其他相关特性的设计与实现 / 75
2.5.1　applicationcontext和bean的初始化及销毁 / 75
2.5.2　lazy-init属性和预实例化 / 81
2.5.3　factorybean的实现 / 82
2.5.4　beanpostprocessor的实现 / 85
2.5.5　autowiring（自动依赖装配）的实现 / 88
2.5.6　bean的依赖检查 / 90
2.5.7　bean对ioc容器的感知 / 91
2.6　小结 / 92
第3章　spring aop的实现 / 94
3.1　spring aop概述 / 95
3.1.1　aop概念回顾 / 95
3.1.2　advice通知 / 98
3.1.3　pointcut切点 / 102
3.1.4　advisor通知器 / 105
3.2　spring aop的设计与实现 / 106
3.2.1　jvm的动态代理特性 / 106
3.2.2　spring aop的设计分析 / 108
3.2.3　spring aop的应用场景 / 108
3.3　建立aopproxy代理对象 / 109
3.3.1　设计原理 / 109
3.3.2　配置proxyfactorybean / 110
3.3.3　proxyfactorybean生成aopproxy代理对象 / 111
3.3.4　jdk生成aopproxy代理对象 / 116
3.3.5　cglib生成aopproxy代理对象 / 117
3.4　spring aop拦截器调用的实现 / 119
3.4.1　设计原理 / 119
3.4.2　jdkdynamicaopproxy的invoke拦截 / 120
3.4.3　cglib2aopproxy的intercept拦截 / 121
3.4.4　目标对象方法的调用 / 122
3.4.5　aop拦截器链的调用 / 123
3.4.6　配置通知器 / 124
3.4.7　advice通知的实现 / 129
3.4.8　proxyfactory实现aop / 136
3.5　spring aop的高级特性 / 138
3.6　小结 / 140
第二部分　spring组件实现篇
第4章　spring mvc与web环境 / 145
4.1　spring mvc概述 / 146
4.2　web环境中的spring mvc / 148
4.3　上下文在web容器中的启动 / 149
4.3.1　ioc容器启动的基本过程 / 149
4.3.2　web容器中的上下文设计 / 151
4.3.3　contextloader的设计与实现 / 154
4.4　spring mvc的设计与实现 / 158
4.4.1　spring mvc的应用场景 / 158
4.4.2　spring mvc设计概览 / 158
4.4.3　dispatcherservlet的启动和初始化 / 160
4.4.4　mvc处理http分发请求 / 166
4.5　spring mvc视图的呈现 / 178
4.5.1　dispatcherservlet视图呈现的设计 / 178
4.5.2　jsp视图的实现 / 182
4.5.3　excelview的实现 / 185
4.5.4　pdf视图的实现 / 187
4.6　小结 / 189
第5章　数据库操作组件的实现 / 191
5.1　spring jdbc的设计与实现 / 192
5.1.1　应用场景 / 192
5.1.2　设计概要 / 192
5.2　spring jdbc中模板类的设计与实现 / 193
5.2.1　设计原理 / 193
5.2.2　jdbctemplate的基本使用 / 193
5.2.3　jdbctemplate的execute实现 / 194
5.2.4　jdbctemplate的query实现 / 196
5.2.5　使用数据库connection / 197
5.3　spring jdbc中rdbms操作对象的实现 / 199
5.3.1　sqlquery的实现 / 200
5.3.2　sqlupdate的实现 / 204
5.3.3　sqlfunction / 206
5.4　spring orm的设计与实现 / 208
5.4.1　应用场景 / 208
5.4.2　设计概要 / 208
5.5　spring驱动hibernate的设计与实现 / 209
5.5.1　设计原理 / 210
5.5.2　hibernate的sessionfactory / 210
5.5.3　hibernatetemplate的实现 / 215
5.5.4　session的管理 / 219
5.6　spring驱动ibatis的设计与实现 / 222
5.6.1　设计原理 / 222
5.6.2　创建sqlmapclient / 222
5.6.3　sqlmapclienttemplate的实现 / 224
5.7　小结 / 227
第6章　spring事务处理的实现 / 228
6.1　spring与事务处理 / 229
6.2　spring事务处理的设计概览 / 229
6.3　spring事务处理的应用场景 / 230
6.4　spring声明式事务处理 / 231
6.4.1　设计原理与基本过程 / 231
6.4.2　实现分析 / 231
6.5　spring事务处理的设计与实现 / 241
6.5.1　spring事务处理的编程式使用 / 241
6.5.2　事务的创建 / 242
6.5.3　事务的挂起 / 249
6.5.4　事务的提交 / 251
6.5.5　事务的回滚 / 253
6.6　spring事务处理器的设计与实现 / 255
6.6.1　spring事务处理的应用场景 / 255
6.6.2　datasourcetransactionmanager的实现 / 256
6.6.3　hibernatetransactionmanager的实现 / 259
6.7　小结 / 265
第7章　spring远端调用的实现 / 267
7.1　spring远端调用的应用场景 / 268
7.2　spring远端调用的设计概览 / 268
7.3　spring远端调用的实现 / 271
7.3.1　spring http调用器的实现 / 271
7.3.2　spring hession/burlap的实现原理 / 282
7.3.3　spring rmi的实现 / 295
7.4　小结 / 302
第三部分　spring应用实现篇
第8章　安全框架acegi的设计与实现 / 307
8.1　spring acegi安全框架概述 / 308
8.1.1　概述 / 308
8.1.2　设计原理与基本实现过程 / 308
8.1.3　acegi的bean配置 / 309
8.2　配置spring acegi / 310
8.3　acegi的web过滤器实现 / 313
8.4　acegi验证器的实现 / 315
8.4.1　authenticationmanager的authenticate / 315
8.4.2　daoauthenticationprovider的实现 / 318
8.4.3　读取数据库用户信息 / 320
8.4.4　完成用户信息的对比验证 / 323
8.5　acegi授权器的实现 / 324
8.5.1　与web环境的接口filtersecurityinterceptor / 324
8.5.2　授权器的实现 / 327
8.5.3　投票器的实现 / 329
8.6　小结 / 330
第9章　spring dm模块的设计与实现 / 332
9.1　spring dm模块的应用场景 / 333
9.2　spring dm的应用过程 / 334
9.3　spring dm设计与实现 / 338
9.4　小结 / 348
第10章　spring flex的设计与实现 / 350
10.1　spring flex模块的应用场景 / 351
10.2　spring flex的应用过程 / 353
10.3　spring flex的设计与实现 / 355
10.4　小结 / 362
附录a　spring项目的源代码环境 / 363
附录b　构建spring项目的发布包 / 378
附录c　使用spring ide / 381
附录d　spring pet clinic应用实例 / 385

## 下载 ##

+ [微盘下载](http://vdisk.weibo.com/s/aADaW4YRFaCnq)
+ [千易下载](http://1000eb.com/1hrxz)
+ [FilePi下载](http://filepi.com/i/i9zjUkp)
