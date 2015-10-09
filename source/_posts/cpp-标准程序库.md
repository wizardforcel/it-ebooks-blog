title: c++标准程序库（中文版）
date: 2015-07-11 19:13:13
categories:
  - cpp
---

![](http://img4.douban.com/lpic/s1092079.jpg)

格式：PDF
类型：扫描版
大小：12.4M

<!--more-->

## 出版信息 ##

作者: [德] Nicolai M. Josuttis
出版社: 华中科技大学出版社
副标题: 自修教程与参考手册
原作名: The C++ Standard Library
译者: 侯捷 / 孟岩
出版年: 2002-9
页数: 800
定价: 108.00元
装帧: 平装
ISBN: 9787560927824

## 简介 ##

这本包含最新资料的完整书籍，反映出被ANSI/ISO C++语言标准规格书纳入的C++标准程序库的最新组成。更明确地说，这本书将焦点放在标准模板库身上，检验其中的容器、迭代器、仿函数和算法。读者还可以找到特殊容、字串、数值类别、国际化议题、IOStream。每一个元素都有深刻的呈现，包括其介绍、设计、运用实例、细部解说、陷阱、意想不到的危险，以及相关类别和函数的精确樯记式和定义式。

## 目录 ##

侯捷译序a
孟岩译序g
目录（contents） v
前言（preface） xvii
致谢（acknowledgments） xix
1 关于本书1
1.1 缘起1
1.2 阅读前的必要基础2
1.3 本书风格与结构2
1.4 如何阅读本书4
1.5 目前发展形式5
1.6 范例程序代码及额外信息5
1.7 回应5
2 c++ 及其标准程序库简介7
2.1 沿革7
2.2 新的语言特性9
2.2.1 templates（模板） 9
2.2.2 基本型别的显式初始化（explicit initialization） 14
2.2.3 异常处理（exception handling） 15
.2.2.4 命名空间（namespaces） 16
2.2.5 bool型别18
2.2.6 关键词explicit 18
2.2.7 新的型别转换操作符（type conversion operators） 19
2.2.8 常数静态成员（constant static members）的初始化20
2.2.9 main() 的定义21
2.3 复杂度和big-o 表示法21
3 一般概念（general concepts） 23
3.1 命名空间（namespace）std 23
3.2 头文件（header files） 24
3.3 错误（error）处理和异常（exception）处理25
3.3.1 标准异常类别（standard exception classes） 25
3.3.2 异常类别（exception classes）的成员28
3.3.3 抛出标准异常29
3.3.4 从标准异常类别（exception classes）中派生新的类别30
3.4 配置器（allocators） 31
4 通用工具（utilities） 33
4.1 pairs（对组） 33
4.1.1 便捷函数make_pair() 36
4.1.2 pair运用实例37
4.2 class auto_ptr 38
4.2.1 auto_ptr的发展动机38
4.2.2 auto_ptr拥有权（ownership）的转移40
4.2.3 auto_ptrs 做为成员之一44
4.2.4 auto_ptrs 的错误运用46
4.2.5 auto_ptr运用实例47
4.2.6 auto_ptr实作细目51
4.3 数值极限（numeric limits） 59
4.4 辅助函数66
4.4.1 挑选较小值和较大值66
4.4.2 两值互换67
4.5 辅助性的“比较操作符”（comparison operators） 69
4.6 头文件[cstddef] 和[cstdlib] 71
4.6.1 [cstddef] 内的各种定义71
4.6.2 [cstdlib] 内的各种定义71
5 standard template library（标准模板库） 73
5.1 stl 组件（stl components） 73
5.2 容器（containers） 75
5.2.1 序列式容器（sequence containers） 76
5.2.2 关联式容器（associative containers） 81
5.2.3 容器配接器（container adapters） 82
5.3 迭代器（iterators） 83
5.3.1 关联式容器的运用实例86
5.3.2 迭代器类型（iterator categories） 93
5.4 算法（algorithms） 94
5.4.1 区间（ranges） 97
5.4.2 处理多个区间101
5.5 迭代器之配接器（iterator adapters） 104
5.5.1 insert iterators（安插型迭代器） 104
5.5.2 stream iterators（串流迭代器） 107
5.5.3 reverse iterators（逆向迭代器） 109
5.6 更易型算法（manipulating algorithms） 111
5.6.1 移除（removing）元素111
5.6.2 更易型算法和关联式容器115
5.6.3 算法v.s. 成员函数116
5.7 使用者自定之泛型函数（user-defined generic functions） 117
5.8 以函数做为算法的参数119
5.8.1“以函数做为算法的参数”实例示范119
5.8.2 判断式（predicates） 121
5.9 仿函数（functors or function objects） 124
5.9.1 什么是仿函数124
5.9.2 预先定义的仿函数131
5.10 容器内的元素（container elements） 134
5.10.1 容器元素的条件134
5.10.2 value 语意vs. reference 语意135
5.11 stl内部的错误处理和异常处理136
5.11.1 错误处理（error handling） 137
5.11.2 异常处理（exception handling） 139
5.12 扩展stl 141
6 stl 容器（containers） 143
6.1 容器的共通能力和共通操作144
6.1.1 容器的共通能力144
6.1.2 容器的共通操作144
6.2 vectors 148
6.2.1 vectors 的能力148
6.2.2 vector 的操作函数150
6.2.3 将vectors 当做一般arrays 使用155
6.2.4 异常处理155
6.2.5 vectors 运用实例156
6.2.6 class vector[bool] 158
6.3 deques 160
6.3.1 deques 的能力161
6.3.2 deque 的操作函数162
6.3.3 异常处理（exception handling） 164
6.3.4 deques 运用实例164
6.4 lists 166
6.4.1 lists 的能力166
6.4.2 list 的操作函数167
6.4.3 异常处理（exception handling） 172
6.4.4 lists 运用实例172
6.5 sets和multisets
175
6.5.1 sets 和multisets 的能力176
6.5.2 set 和multiset 的操作177
6.5.3 异常处理（exception handling） 185
6.5.4 sets 和multisets 运用实例186
6.5.5 执行期指定排序准则（sorting criterion） 191
6.6 maps 和multimaps 194
6.6.1 maps 和multimaps 的能力195
6.6.2 map 和multimap 的操作函数196
6.6.3 将maps 视为关联式数组（associated arrays） 205
6.6.4 异常处理（exception handling） 207
6.6.5 maps 和multimaps 运用实例207
6.6.6 综合实例：运用maps, strings 并于执行期指定排序准则213
6.7 其它的stl容器217
6.7.1 strings 可被视为一种stl容器217
6.7.2 arrays 可被视为一种stl容器218
6.7.3 hash tables 221
6.8 动手实现reference 语意222
6.9 各种容器的运用时机226
6.10 细说容器内的型别和成员230
6.10.1 容器内的型别230
6.10.2 生成（create）、复制（copy）、销毁（destroy） 231
6.10.3“非变动性操作（nonmodifying operations） 233
6.10.4 赋值（指派, assignments） 236
6.10.5 直接元素存取237
6.10.6 “会产出迭代器”的各项操作239
6.10.7 元素的安插（inserting）和移除（removing） 240
6.10.8 lists 的特殊成员函数244
6.10.9 对配置器（allocator）的支持246
6.10.10 综观stl容器的异常处理248
7 stl 迭代器（iterators） 251
7.1 迭代器头文件251
7.2 迭代器类型（iterator categories） 251
7.2.1 input（输入）迭代器252
7.2.2 output（输出）迭代器253
7.2.3 forward（前向）迭代器254
7.2.4 bidirectional（双向）迭代器255
7.2.5 random access（随机存取）迭代器255
7.2.6 vector 迭代器的递增（increment）和递减（decrement） 258
7.3 迭代器相关辅助函数259
7.3.1 advance() 可令迭代器前进259
7.3.2 distance() 可处理迭代器之间的距离261
7.3.3 iter_swap() 可交换两个迭代器所指内容263
7.4 迭代器配接器（iterator adapters） 264
7.4.1 reverse（逆向）迭代器264
7.4.2 insert（安插型）迭代器271
7.4.3 stream（串流）迭代器277
7.5 迭代器特性（iterator traits） 283
7.5.1 为迭代器编写泛型函数（generic functions） 285
7.5.2 使用者自定（user-defined）的迭代器288
8 stl 仿函数（functors or function objects） 293
8.1 仿函数的概念293
8.1.1 仿函数可当做排序准则（sort criteria） 294
8.1.2 仿函数可拥有自己的内部状态（internal state） 296
8.1.3 for_each() 的回返值300
8.1.4 判断式（predicates）和仿函数（functors） 302
8.2 预定义的仿函数305
8.2.1 函数配接器（function adapters） 306
8.2.2 针对成员函数而设计的函数配接器307
8.2.3 针对一般函数（非成员函数）而设计的函数配接器309
8.2.4 让自定仿函数也可以使用函数配接器310
8.3 辅助用（组合型）仿函数313
8.3.1 一元组合函数配接器（unary compose function object adapters） 314
8.3.2 二元组合函数配接器（binary compose function object adapters） 318
9 stl 算法（algorithms） 321
9.1 算法头文件（header files） 321
9.2 算法概观322
9.2.1 简介322
9.2.2 算法分门别类323
9.3 辅助函数332
9.4 for_each() 算法334
9.5 非变动性算法（nonmodifying algorithms） 338
9.5.1 计算元素个数338
9.5.2 求最大值和最小值339
9.5.3 搜寻元素341
9.5.4 区间的比较356
9.6 变动性算法（modifying algorithms） 363
9.6.1 复制（copying）元素363
9.6.2 转换（transforming）和结合（combining）元素366
9.6.3 互换（swapping）元素内容370
9.6.4 赋予（assigning）新值372
9.6.5 替换（replacing）元素375
9.7 移除性算法（removing algorithms） 378
9.7.1 移除某些特定元素378
9.7.2 移除重复元素381
9.8 变序性算法（mutating algorithms） 386
9.8.1 逆转（reversing）元素次序386
9.8.2 旋转（rotating）元素次序388
9.8.3 排列（permuting）元素391
9.8.4 重排元素（shuffling, 搅乱次序） 393
9.8.5 将元素向前搬移395
9.9 排序算法（sorting algorithms） 397
9.9.1 对所有元素排序397
9.9.2 局部排序（partial sorting） 400
9.9.3 根据第n 个元素排序404
9.9.4 heap 算法406
9.10 已序区间算法（sorted range algorithms） 409
9.10.1 搜寻元素（searching） 410
9.10.2 合并元素（merging） 416
9.11 数值算法（numeric algorithms） 425
9.11.1 加工运算后产生结果425
9.11.2 相对值和绝对值之间的转换429
10 特殊容器（special containers） 435
10.1 stacks（堆栈） 435
10.1.1 核心界面436
10.1.2 stacks 运用实例437
10.1.3 class stack[] 细部讨论438
10.1.4 一个使用者自定的stack class 441
10.2 queues（队列） 444
10.2.1 核心界面445
10.2.2 queues 运用实例446
10.2.3 class queue[] 细部讨论447
10.2.4 一个使用者自定的queue class 450
10.3 priority queues（优先队列） 453
10.3.1 核心界面455
10.3.2 priority queues 运用实例455
10.3.3 class priority_queue[] 细部讨论456
10.4 bitsets 460
10.4.1 bitsets 运用实例460
10.4.2 class bitset 细部讨论463
11 strings（字符串） 471
11.1 动机471
11.1.1 例一：引出一个临时文件名
472
11.1.2 例二：引出一段文字并逆向打印476
11.2 string classes 细部描述479
11.2.1 string 的各种相关型别479
11.2.2 操作函数（operations）综览481
11.2.3 建构式和解构式（constructors and destructors） 483
11.2.4 strings 和c-strings 484
11.2.5 大小（size）和容量（capacity） 485
11.2.6 元素存取（element access） 487
11.2.7 比较（comparisons） 488
11.2.8 更改内容（modifiers） 489
11.2.9 子字符串及字符串接合492
11.2.10 i/o 操作符492
11.2.11 搜寻和查找（searching and finding） 493
11.2.12 数值npos 的意义495
11.2.13 strings 对迭代器的支援497
11.2.14 国际化（internationalization） 503
11.2.15 效率（performance） 506
11.2.16 strings 和vectors 506
11.3 细说string class 507
11.3.1 内部的型别定义和静态值507
11.3.2 生成（create）、拷贝（copy）、销毁（destroy） 508
11.3.3 大小（size）和容量（capacity） 510
11.3.4 比较（comparisons） 511
11.3.5 字符存取（character access） 512
11.3.6 产生c-strings 和字符数组（character arrays） 513
11.3.7 更改内容514
11.3.8 搜寻（searching and finding） 520
11.3.9 子字符串及字符串接合524
11.3.10 i/o 函数524
11.3.11 产生迭代器525
11.3.12 对配置器（allocator）的支持526
12 数值（numerics） 529
12.1 复数（complex numbers） 529
12.1.1 class complex运用实例530
12.1.2 复数的各种操作533
12.1.3 class complex[] 细部讨论541
12.2 valarrays 547
12.2.1 认识valarrays 547
12.2.2 valarray 的子集（subsets） 553
12.2.3 class valarray 细部讨论569
12.2.4 valarray子集类别（subset classes）细部讨论575
12.3 全域性的数值函数581
13 以stream classes完成输入和输出583
13.1 i/o streams 基本概念584
13.1.1 stream物件584
13.1.2 stream类别584
13.1.3 全域性的stream物件585
13.1.4 stream操作符586
13.1.5 操控器（manipulators） 586
13.1.6 一个简单的例子587
13.2 基本的stream类别和stream对象588
13.2.1 相关类别及其阶层体系588
13.2.2 全域性的stream物件591
13.2.3 头文件（headers） 592
13.3 标准的stream操作符[[ 和]] 593
13.3.1 output操作符[[ 593
13.3.2 input操作符]] 594
13.3.3 特殊型别的i/o 595
13.4 streams 的状态（state） 597
13.4.1 用来表示streams 状态的一些常数597
13.4.2 用来处理streams 状态的一些成员函数598
13.4.3 stream状态与布尔条件测试600
13.4.4 stream的状态和异常602
13.5 标准i/o 函数607
13.5.1 输入用的成员函数607
13.5.2 输出用的成员函数610
13.5.3 运用实例611
13.6 操控器（manipulators） 612
13.6.1 操控器如何运作612
13.6.2 使用者自定操控器614
13.7 格式化（formatting） 615
13.7.1 格式标志（format flags） 615
13.7.2 布尔值（boolean values）的i/o 格式617
13.7.3 字段宽度、填充字符、位置调整618
13.7.4 正记号与大写字620
13.7.5 数值进制（numeric base） 621
13.7.6 浮点数（floating-point）表示法623
13.7.7 一般性的格式定义625
13.8 国际化（internationalization） 625
13.9 文件存取（file access） 627
13.9.1 文件标志（file flags） 631
13.9.2 随机存取634
13.9.3 使用文件描述器（file descriptors） 637
13.10 连接input streams 和output streams 637
13.10.1 以tie()完成“松耦合”（loose coupling） 637
13.10.2 以stream缓冲区完成“紧耦合”（tight coupling） 638
13.10.3 将标准streams 重新导向（redirecting） 641
13.10.4 用于读写的streams 643
13.11 string stream classes 645
13.11.1 string stream classes 645
13.11.2 char* stream classes 649
13.12 “使用者自定型别”之i/o操作符652
13.12.1 实作一个output 操作符652
13.12.2 实作一个input 操作符654
13.12.3 以辅助函数完成i/o 656
13.12.4 以非格式化函数完成使用者自定的操作符658
13.12.5 使用者自定的格式标志（format flags） 659
13.12.6 使用者自定之i/o 操作符的数个依循惯例662
13.13 stream buffer classes 663
13.13.1 从使用者的角度看stream缓冲区663
13.13.2 stream缓冲区迭代器（buffer iterators） 665
13.13.3 使用者自定的stream 缓冲区668
13.14 关于效能（performance） 681
13.14.1 与c 标准输入输出流（standard streams）同步682
13.14.2 stream缓冲区内的缓冲机制682
13.14.3 直接使用stream缓冲区683
14 国际化（internationalization, i18n） 685
14.1 不同的字符编码（character encoding） 686
14.1.1 宽字符（wide-character）和多字节文本（multibyte text） 686
14.1.2 字符特性（character traits） 687
14.1.3 特殊字符国际化691
14.2 locales 的概念692
14.2.1 运用locales 693
14.2.2 locale facets 698
14.3 locales 细部讨论700
14.4 facets 细部讨论704
14.4.1 数值格式化705
14.4.2 时间和日期格式化708
14.4.3 货币符号格式化711
14.4.4 字符的分类和转换715
14.4.5 字符串校勘（string collation） 724
14.4.6 信息国际化725
15 空间配置器（allocators） 727
15.1 应用程序开发者如何使用配置器727
15.2 程序库开发者如何使用配置器728
15.3 c++ 标准程序库的预设配置器732
15.4 使用者自行定义的配置器735
15.5 配置器细部讨论737
15.5.1 内部定义的型别737
15.5.2 各项操作739
15.6“未初始化内存”之处理工具细部讨论740
网络上的资源（internet resources） 743
参考书目（bibliography） 745
索引（index） 747

## 下载 ##

+ [百度云下载](http://pan.baidu.com/s/1gdKyh6j)
+ [微盘下载](http://vdisk.weibo.com/s/aADaW4YRFjV_Y)
+ [FilePi下载](http://filepi.com/i/DN8Vvy8)
+ [千易下载](http://1000eb.com/1eote)
