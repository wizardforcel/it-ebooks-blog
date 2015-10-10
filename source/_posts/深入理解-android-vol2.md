title: 深入理解android卷二
date: 2015-06-30 14:18:32
categories:
  - android
---

![](http://img3.douban.com/lpic/s11162474.jpg)

格式：EPUB
类型：文字版

<!--more-->

## 出版信息 ##

作者: 邓凡平 
出版社: 机械工业出版社
副标题: 卷II
出版年: 2012-8
页数: 440
定价: 79.00元
丛书: 深入理解Android
ISBN: 9787111389187

## 简介 ##

《深入理解Android:卷2》是“深入理解Android”系列的第2本，第1本书上市后获得广大读者高度评价，在Android开发者社群内口口相传。《深入理解Android:卷2》不仅继承了第1本书的优点并改正了其在细微处存在的一些不足，而且还在写作的总体思想上进行了创新，更强调从系统设计者的角度去分析Android系统中各个模块内部的实现原理和工作机制。从具体内容上讲，重点是Android Framework的Java层，对Java层涉及的核心模块和服务进行了深入而细致的分析。通过《深入理解Android:卷2》，读者不仅能对Android系统本身有更深入的理解，而且还能掌握分析大型复杂源代码的能力。
《深入理解Android:卷2》共8章：第1章介绍了阅读本书所需要做的准备工作，包括Android 4.0源码的下载和编译、Eclipse环境的搭建，以及Android系统进程（system_process）的调试等；第2章对Java Binder和MessageQueue的实现进行了深入分析；第3章仔细剖析了SystemServer的工作原理，这些服务包括EntropyService、DropboxManagerService、DiskStatsService、DeviceStorageMonitorService、SamplingProfilerService和ClipboardService；第4章对系统中负责Package信息查询和APK安装、卸载、更新等工作的服务PackageManagerService进行了详细分析；第5章则对Android系统中负责电源管理的核心服务 PowerManagerService的原理进行了一番深入的分析；第6章以ActivityManagerService为分析重点，它的启动、Activity的创建和启动、BroadcastReceiver的工作原理、Android中的进程管理等内容展开了较为深入的研究；第7章对ContentProvider的创建和启动、SQLite、Cursor query和close的实现等进行了深入分析；第8章以ContentService和AccountManagerService为分析对象，介绍了数据更新通知机制的实现，以及账户管理和数据同步等相关知识。

## 目录 ##

前　言
第1章　搭建Android源码工作环境 / 1
1.1　Android系统架构 / 2
1.2　搭建开发环境 / 3
1.2.1　下载源码 / 3
1.2.2　编译源码 / 4
1.2.3　利用Eclipse调试system_process / 5
1.3　本章小结 / 11
第2章　深入理解Java Binder和MessageQueue / 12
2.1　概述 / 13
2.2　Java层中的Binder架构分析 / 13
2.2.1　Binder架构总览 / 13
2.2.2　初始化Java层Binder框架 / 14
2.2.3　addService实例分析 / 17
2.2.4　Java层Binder架构总结 / 26
2.3　心系两界的MessageQueue / 27
2.3.1　MessageQueue的创建 / 27
2.3.2　提取消息 / 28
2.3.3　nativePollOnce函数分析 / 31
2.3.4　MessageQueue总结 / 41
2.4　本章小结 / 42
第3章　深入理解SystemServer / 44
3.1 概述 / 45
3.2　SystemServer分析 / 45
3.2.1　main函数分析 / 45
3.2.2　Service群英会 / 48
3.3　EntropyService分析 / 49
3.4　DropBoxManagerService分析 / 50
3.4.1　DBMS构造函数分析 / 51
3.4.2　dropbox日志文件的添加 / 51
3.4.3　DBMS和settings数据库 / 56
3.5　DiskStatsService和DeviceStorageMonitorService分析 / 56
3.5.1　DiskStatsService分析 / 56
3.5.2　DeviceStorageManagerService分析 / 58
3.6　SamplingProfilerService分析 / 60
3.6.1　SamplingProfilerService构造函数分析 / 61
3.6.2　SamplingProfilerIntegration分析 / 62
3.7　ClipboardService分析 / 64
3.7.1　复制数据到剪贴板 / 64
3.7.2　从剪切板粘贴数据 / 67
3.7.3　CBS中的权限管理 / 69
3.8 本章小结 / 73
第4章　深入理解PackageManagerService / 74
4.1　概述 / 75
4.2　初识PackageManagerService / 76
4.3　PKMS的main函数分析 / 77
4.3.1　构造函数分析之前期准备工作 / 78
4.3.2　构造函数分析之扫描Package / 90
4.3.3　构造函数分析之扫尾工作 / 105
4.3.4　PKMS构造函数总结 / 105
4.4　APK Installation分析 / 105
4.4.1　adb install分析 / 105
4.4.2　pm分析 / 107
4.4.3　installPackageWithVerification函数分析 / 109
4.4.4　APK 安装流程总结 / 121
4.4.5　Verification介绍 / 122
4.5　queryIntentActivities分析 / 124
4.5.1　Intent及IntentFilter介绍 / 124
4.5.2　Activity信息的管理 / 125
4.5.3　Intent 匹配查询分析 / 128
4.5.4　queryIntentActivities总结 / 131
4.6　installd及UserManager介绍 / 131
4.6.1　installd介绍 / 131
4.6.2　UserManager介绍 / 136
4.7　本章学习指导 / 138
4.8　本章小结 / 138
第5章　深入理解PowerManagerService / 139
5.1　概述 / 140
5.2　初识PowerManagerService / 140
5.2.1　PMS构造函数分析 / 141
5.2.2　init分析 / 141
5.2.3　systemReady分析 / 147
5.2.4　BootComplete处理 / 148
5.2.5　初识PowerManagerService总结 / 149
5.3　PMS WakeLock分析 / 149
5.3.1　WakeLock客户端分析 / 149
5.3.2　PMS acquireWakeLock分析 / 151
5.3.3　Power类及LightService类介绍 / 160
5.3.4　WakeLock总结 / 163
5.4　userActivity及Power按键处理分析 / 164
5.4.1　userActivity分析 / 164
5.4.2　Power按键处理分析 / 167
5.5　BatteryService及BatteryStatsService分析 / 168
5.5.1　BatteryService分析 / 169
5.5.2　BatteryStatsService分析 / 172
5.5.3　BatteryService及BatteryStatsService总结 / 182
5.6　本章学习指导 / 183
5.7　本章小结 / 183
第6章　深入理解ActivityManagerService / 184
6.1　概述 / 185
6.2　初识ActivityManagerService / 186
6.2.1　ActivityManagerService的main函数分析 / 187
6.2.2　AMS的 setSystemProcess分析 / 197
6.2.3　AMS的 installSystemProviders函数分析 / 202
6.2.4　AMS的 systemReady分析 / 211
6.2.5　初识ActivityManagerService总结 / 218
6.3　startActivity分析 / 219
6.3.1　从am说起 / 219
6.3.2　AMS的startActivityAndWait函数分析 / 221
6.3.3　startActivityLocked分析 / 230
6.4　Broadcast和BroadcastReceiver分析 / 265
6.4.1　registerReceiver流程分析 / 267
6.4.2　sendBroadcast流程分析 / 272
6.4.3　BROADCAST_INTENT_MSG消息处理函数 / 276
6.4.4　应用进程处理广播分析 / 282
6.4.5　广播处理总结 / 284
6.5　startService之按图索骥 / 285
6.5.1　Service知识介绍 / 285
6.5.2　startService流程图 / 286
6.6　AMS中的进程管理 / 287
6.6.1　Linux进程管理介绍 / 287
6.6.2　关于Android中的进程管理的介绍 / 289
6.6.3　AMS进程管理函数分析 / 294
6.6.4　AMS进程管理总结 / 305
6.7　App的 Crash处理 / 305
6.7.1　应用进程的Crash处理 / 306
6.7.2　AMS的handleApplicationCrash分析 / 306
6.7.3　AppDeathRecipient binderDied分析 / 309
6.7.4　App的Crash处理总结 / 313
6.8　本章学习指导 / 314
6.9　本章小结 / 315
第7章　深入理解ContentProvider / 316
7.1　概述 / 317
7.2　MediaProvider的启动及创建 / 318
7.2.1　Context的getContentResolver函数分析 / 318
7.2.2　MediaStore.Image.Media的query函数分析 / 319
7.2.3　MediaProvider的启动及创建总结 / 329
7.3　SQLite创建数据库分析 / 330
7.3.1　SQLite及SQLiteDatabase家族 / 330
7.3.2　MediaProvider创建数据库分析 / 335
7.3.3　SQLiteDatabase创建数据库的分析总结 / 344
7.4　Cursor 的query函数的实现分析 / 345
7.4.1　提取query关键点 / 346
7.4.2　MediaProvider 的query分析 / 349
7.4.3　query关键点分析 / 356
7.4.4　Cursor query实现分析总结 / 368
7.5　Cursor close函数实现分析 / 368
7.5.1　客户端close的分析 / 369
7.5.2　服务端close的分析 / 371
7.5.3　finalize函数分析 / 372
7.5.4　Cursor close函数总结 / 373
7.6　ContentResolver openAssetFileDescriptor函数分析 / 373
7.6.1　openAssetFileDescriptor之客户端调用分析 / 374
7.6.2　ContentProvider的 openTypedAssetFile函数分析 / 376
7.6.3　跨进程传递文件描述符的探讨 / 379
7.6.4　openAssetFileDescriptor函数分析总结 / 384
7.7　本章学习指导 / 384
7.8　本章小结 / 385
第8章　深入理解ContentService和AccountManagerService / 386
8.1　概述 / 387
8.2　数据更新通知机制分析 / 387
8.2.1　初识ContentService / 388
8.2.2　ContentResovler 的registerContentObserver分析 / 389
8.2.3　ContentResolver的 notifyChange分析 / 391
8.2.4　数据更新通知机制总结和深入探讨 / 393
8.3　AccountManagerService分析 / 395
8.3.1　初识AccountManagerService / 396
8.3.2　AccountManager addAccount分析 / 402
8.3.3　AccountManagerService的分析总结 / 414
8.4　数据同步管理SyncManager分析 / 415
8.4.1　初识SyncManager / 415
8.4.2　ContentResolver 的requestSync分析 / 424
8.4.3　数据同步管理SyncManager分析总结 / 436
8.5　本章学习指导 / 437
8.6　本章小结 / 437
“深入理解Android”系列书籍的规划路线图 / 438

## 下载 ##

+ [百度云下载](http://pan.baidu.com/s/1eQFG9KA)
+ [微盘下载](http://vdisk.weibo.com/s/aADaW4YRFh2U5)
+ [FilePi下载](http://filepi.com/i/hqFhhCE)
+ [千易下载](http://1000eb.com/1dxjq)