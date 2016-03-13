---
title: Python 学习笔记 基础篇
date: 2016-03-13 17:20:25
tags:
  - python
---

整理：Jims of [肥肥世家](http://www.ringkee.com)

[jims.yang@gmail.com](mailto:jims.yang@gmail.com)

Copyright © 2004，2005，2006 本文遵从GNU 的自由文档许可证(Free Document License)的条款，欢迎转载、修改、散布。

发布时间：2004年07月10日

更新时间：2006年06月14日，把参考篇的内容合并进来。

<!--more-->

**Abstract**

现时国内python的中文资料极少，使学习Python较困难。国外的资料虽多，但都是英文的，使我们学习起来很不方便。有鉴于此，我开始了Python中文资料库的整理工作，以推动Python的发展和在中国的应用。在自由的世界里，正因为有你的支持和帮助，才使我得以不断前进。我相信我们每人一小步就可带动python在中国前进一大步。

<!--more-->

**Table of Contents**

+ [1\. 绪论](#id2875104)
    + [1.1\. Python历史](#id2811704)
    + [1.2\. Python功能简介](#id2811781)
    + [1.3\. 应用范围](#id2810170)
    + [1.4\. 如何开始？](#id2810267)
+ [2\. Python编程习惯与特点](#id2861425)
    + [2.1\. 代码风格](#id2861433)
    + [2.2\. 保留字](#id2861575)
    + [2.3\. Python运算符和表达式](#id2861594)
        + [2.3.1\. Python运算符](#id2861602)
        + [2.3.2\. 运算符优先顺序](#id2861844)
        + [2.3.3\. 真值表](#id2808594)
        + [2.3.4\. 复合表达式](#id2808746)
    + [2.4\. 给变量赋值](#id2808820)
+ [3\. Python内建对象类型](#id2808911)
    + [3.1\. Number数值型](#id2808928)
    + [3.2\. String字符串型](#id2809008)
        + [3.2.1\. 字符串的格式化](#id2809192)
        + [3.2.2\. 转义字符](#id2809469)
        + [3.2.3\. Unicode字符串](#id2875369)
        + [3.2.4\. 原始字符串](#id2875512)
    + [3.3\. List列表](#id2875536)
    + [3.4\. Tuple元组](#id2875904)
    + [3.5\. 序列对象](#id2875979)
    + [3.6\. Dictionary字典](#id2876078)
    + [3.7\. File文件](#id2876321)
    + [3.8\. 理解引用](#id2876343)
    + [3.9\. copy and deepcopy](#id2876409)
    + [3.10\. 标识数据类型](#id2876486)
    + [3.11\. 数组对象](#id2876523)
+ [4\. 控制语句](#id2876868)
+ [5\. 函数](#id2877126)
    + [5.1\. 常用函数](#id2877464)
    + [5.2\. 内置类型转换函数](#id2877751)
    + [5.3\. 序列处理函数](#id2878060)
+ [6\. 模块](#id2878241)
    + [6.1\. String模块](#id2878430)
    + [6.2\. time模块](#id2878537)
+ [7\. 类](#id2878619)
+ [8\. 异常处理](#id2878694)
+ [9\. 文件处理](#id2878856)
    + [9.1\. 文件处理的函数和方法](#id2878871)
    + [9.2\. 示例](#id2879330)
+ [10\. 正则表达式](#id2879657)
    + [10.1\. 基本元素](#id2879700)
    + [10.2\. 操作](#id2880568)
+ [11\. 调试](#id2881059)
+ [12\. HOW-TO](#id2881117)

## Chapter 1\. 绪论


## 1.1\. Python历史

Python是一种开源的面向对象的脚本语言，它起源于1989年末，当时，CWI（阿姆斯特丹国家数学和计算机科学研究所）的研究员Guido van Rossum需要一种高级脚本编程语言，为其研究小组的Amoeba分布式操作系统执行管理任务。为创建新语言，他从高级数学语言ABC（ALL BASIC CODE）汲取了大量语法，并从系统编程语言Modula-3借鉴了错语处理机制。Van Rossum把这种新的语言命名为Python（大蟒蛇）---来源于BBC当时正在热播的喜剧连续剧“Monty Python”。

Python于1991年初公开发行，由于功能强大和采用开源方式发行，Python的发展得很快，用户越来越多，形成了一个强大的社区力量。2001年，Python的核心开发团队移师Digital Creations公司，该公司是Zope（一个用Python编写的web应用服务器）的创始者。现在最新的版本是python2.3.4，大家可到[http://www.python.org](http://www.python.org)上了解最新的Python动态和资料 。

## 1.2\. Python功能简介

Python是一种解析性的，交互式的，面向对象的编程语言，类似于Perl、Tcl、Scheme或Java。

Python一些主要功能介绍:

*   Python使用一种优雅的语法，可读性强。

*   Python是一种很灵活的语言，能帮你轻松完成编程工作。并可作为一种原型开发语言，加快大型程序的开发速度。

*   有多种数据类型：numbers (integers, floating point, complex, and unlimited-length long integers), strings (ASCII 和 Unicode), lists, dictionaries。

*   Python支持类和多层继承等的面向对象编程技术。

*   代码能打包成模块和包，方便管理和发布。

*   支持异常处理，能有效捕获和处理程序中发生的错误。

*   强大的动态数据类型支持，不同数据类型相加会引发一个异常。

*   Python支持如生成器和列表嵌套等高级编程功能。

*   自动内存碎片管理，有效利用内存资源。

*   强大的类库支持，使编写文件处理、正则表达式，网络连接等程序变得相当容易。

*   Python的交互命令行模块能方便地进行小代码调试和学习。

*   Python易于扩展，可以通过C或C++编写的模块进行功能扩展。

*   Python解析器可作为一个编程接口嵌入一个应用程序中。

*   Python可运行在多种计算机平台和操作系统中，如各位unix，windows，MacOS,OS/2等等。

*   Python是开源的，可自由免费使用和发布，并且可用于商业用途以获取利润。如想详细了解Python的许可协议可到以下网址查询[http://www.python.org/psf/license.html](http://www.python.org/psf/license.html)

## 1.3\. 应用范围

*   系统编程，提供大量系统接口API，能方便进行系统维护和管理。

*   图形处理，有PIL、Tkinter等图形库支持，能方便进行图形处理。

*   数学处理，NumPy扩展提供大量与许多标准数学库的接口，

*   文本处理，python提供的re模块能支持正则表达式，还提供SGML，XML分析模块，许多程序员利用python进行XML程序的开发。

*   数据库编程，程序员可通过遵循Python DB-API（数据库应用程序编程接口）规范的模块与Microsoft SQL Server，Oracle，Sybase，DB2，Mysql等数据库通信。python自带有一个Gadfly模块，提供了一个完整的SQL环境。

*   网络编程，提供丰富的模块支持sockets编程，能方便快速地开发分布式应用程序。

*   作为Web应用的开发语言，支持最新的XML技术。

*   多媒体应用，Python的PyOpenGL模块封装了“OpenGL应用程序编程接口”，能进行二维和三维图像处理。PyGame模块可用于编写游戏软件。

## 1.4\. 如何开始？

*   进入交互命令行方式。如果是linux类的系统，python解析器应该已经安装在/usr/local/bin/python中，直接打python就可进入交互式命令行界面，如下所示:

    ```
    Python 2.3.3 (#1, Apr 27 2004, 15:17:58)
    [GCC 3.2 20020903 (Red Hat Linux 8.0 3.2-7)] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

    ```

    “>>>”符号是Python命令行界面的提示符，可按CTRL+D退出，如果是windows环境的话就要按CTRL+Z了。还可以用以下命令退出命令行界面：“import sys；sys.exit()”。如果是windows系统，可到[http://www.python.org/download/](http://www.python.org/download/)下载最新的安装程序进行安装。安装完成后直接打python也可进入命令行界面。命令行是python最简单直观，也是最方便的一种执行环境，我们可以在这里学习python语法和调试程序。如果要打印"hello world"可以输入以下命令：

    ```
    >>>print "hello world"
    hello world

    ```

*   以模块文件方式运行。模块文件是包含python语句的文本，以.py结尾。运行模块文件只要输入python xxx.py就可以了。

*   以linux脚本方式运行。和shell脚本差不多，以vi或其它文本编辑器输入以下内容:

    ```
    #!/usr/local/bin/python
    print "test ............"

    ```

    存盘后，把文件属性改为可执行，就可象shell脚本一样执行了。

*   **Table 1.1\. Python命令行选项**

    ```
    | 选项 | 作用 |
    | --- | --- |
    | -c cmd | 在命令行直接执行python代码。如python -c 'print "hello world"'。 |
    | -d | 脚本编译后从解释器产生调试信息。同PYTHONDEBUG=1。 |
    | -E | 忽略环境变量。 |
    | -h | 显示python命令行选项帮助信息。 |
    | -i | 脚本执行后马上进入交互命令行模式。同PYTHONINSPECT=1。 |
    | -O | 在执行前对解释器产生的字节码进行优化。同 PYTHONOPTIMIZE=1。 |
    | -OO | 在执行前对解释器产生的字节码进行优化，并删除优化代码中的嵌入式文档字符串。 |
    | -Q arg | 除法规则选项，-Qold(default)，-Qwarn，-Qwarnall，-Qnew。 |
    | -S | 解释器不自动导入site.py模块。 |
    | -t | 当脚本的tab缩排格式不一致时产生警告。 |
    | -u | 不缓冲stdin、stdout和stderr，默认是缓冲的。同PYTHONUNBUFFERED=1。 |
    | -v | 产生每个模块的信息。如果两个-v选项，则产生更详细的信息。同PYTHONVERBOSE=x。 |
    | -V | 显示Python的版本信息。 |
    | -W arg | 出错信息控制。(arg is action:message:category:module:lineno) |
    | -x | 忽略源文件的首行。要在多平台上执行脚本时有用。 |
    | file | 执行file里的代码。 |
    | - | 从stdin里读取执行代码。 |
    ```

## Chapter 2\. Python编程习惯与特点


## 2.1\. 代码风格

*   在Python中，每行程序以换行符代表结束，如果一行程序太长的话，可以用“\”符号扩展到下一行。在python中以三引号(""")括起来的字符串，列表，元组和字典都能跨行使用。并且以小括号(...)、中括号[...]和大括号{...}包围的代码不用加“\”符也可扩展到多行。如：

*   在Python中是以缩进来区分程序功能块的，缩进的长度不受限制，但就一个功能块来讲，最好保持一致的缩进量。

*   如果一行中有多条语句，语句间要以分号（;）分隔。

*   以“#”号开头的内容为注释，python解释器会忽略该行内容。

*   在python中，所有标识符可以包括英文、数字以及下划线（\_），但不能以数字开头。python中的标识符是区分大小写的。

*   以下划线开头的标识符是有特殊意义的。以单下划线开头（\_foo）的代表不能直接访问的类属性，需通过类提供的接口进行访问，不能用“from xxx import \*”而导入；以双下划线开头的（\_\_foo）代表类的私有成员；以双下划线开头和结尾的（\_\_foo\_\_）代表python里特殊方法专用的标识，如\_\_init\_\_（）代表类的构造函数。

*   在交互模式下运行python时，一个下划线字符(\_)是特殊标识符，它保留了表达式的最后一个计算结果。

    ```
    >>> "hello"
    'hello'
    >>> _
    'hello'
    >>> 10+10
    20
    >>> _
    20
    ```

*   在python中，函数、类、模块定义的第一段代码如果是字符串的话，就把它叫作文件字串，可通过\_\_doc\_\_属性访问。如:

    ```
    def test():
    "this is a document string"

    return 100+1000

    >>>print test.__doc__
    this is a document string

    ```

## 2.2\. 保留字

```
	and		elif		global		or          yield
	assert		else		if		pass
	break		except		import		print
	class		exec		in		raise
	continue	finally		is		return
	def		for		lambda		try
	del		from		not		while

```

## 2.3\. Python运算符和表达式

### 2.3.1\. Python运算符



**Table 2.1\. Python运算符列表**

| 运算符 | 描述 |
| --- | --- |
| x+y，x-y | 加、减，“+”号可重载为连接符 |
| x\*y，x\*\*y，x/y，x%y | 相乘、求平方、相除、求余，“*”号可重载为重复，“%”号可重载为格式化 |
| &lt;，&lt;=，&gt;，&gt;=，==，&lt;&gt;，!= | 比较运算符 |
| +=，-=，\*=，/=，%=，\*\*=，&lt;&lt;=，&gt;&gt;=，&=，^=，&#124;= | 自变运算符 |
| x&#124;y | 按位或 |
| x^y | 按位异或 |
| x&y | 按位与 |
| ~x | 按位取反 |
| x&lt;&lt;，x&gt;&gt;y | x向左或向右移y位 |
| is, is not | 等同测试 |
| in, not in | 是否为成员测试 |
| or，and，not | 逻辑运算符 |
| x[i]，x[i:j]，x.y，x(...) | 索引，分片，限定引用，函数调用 |
| (...)，[...]，{...}，'...' | 元组，列表，字典，转化为字符串 |

### 2.3.2\. 运算符优先顺序



**Table 2.2\. 运算符优先顺序列表(从最高到最低)**

| 运算符 | 描述 |
| --- | --- |
| 'expr' | 字符串转换 |
| {key:expr,...} | 字典 |
| [expr1,expr2...] | 列表 |
| (expr1,expr2,...) | 元组 |
| function(expr,...) | 函数调用 |
| x[index:index] | 切片 |
| x[index] | 下标索引取值 |
| x.attribute | 属性引用 |
| ~x | 按位取反 |
| +x，-x | 正，负 |
| x\*\*y | 幂 |
| x\*y，x/y，x%y | 乘，除，取模 |
| x+y，x-y | 加，减 |
| x&lt;&lt;y，x&gt;&gt;y | 移位 |
| x&y | 按位与 |
| x^y | 按位异或 |
| x&#124;y | 按位或 |
| x&lt;y，x&lt;=y，x==y，x!=y，x&gt;=y，x&gt;y | 比较 |
| x is y，x is not y | 等同测试 |
| x in y，x not in y | 成员判断 |
| not x | 逻辑否 |
| x and y | 逻辑与 |
| x or y | 逻辑或 |
| lambda arg,...:expr | Lambda匿名函数 |

### 2.3.3\. 真值表



**Table 2.3\.**

| 对象/常量 | 值 |
| --- | --- |
| "" | 假 |
| "string" | 真 |
| 0 | 假 |
| &gt;=1 | 真 |
| &lt;=-1 | 真 |
| ()空元组 | 假 |
| []空列表 | 假 |
| {}空字典 | 假 |
| None | 假 |

### 2.3.4\. 复合表达式

*   对于and，当计算a and b时，python会计算a，如果a为假，则取a值，如果a为真，则python会计算b且整个表达式会取b值。如：

    ```
    >>> a,b=10,20
    >>> a and b   #a is true
    20
    >>> a,b=0,5   #a is false
    >>> a and b
    0
    ```

*   对于or，当计算a or b时，python会计算a，如果a为真，则整个表达式取a值，如果a为假，表达式将取b值。如：

    ```
    >>> a,b=10,20
    >>> a or b
    10
    >>> a,b=0,5
    >>> a or b
    5
    ```

*   对于not，not将反转表表达式的“实际值”，如果表达式为真，not为返回假，如为表达式为假，not为返回真。如：

    ```
    >>> not 2
    False
    >>> not 0
    True
    >>> not "test"
    False
    >>> not ""
    True
    ```

## 2.4\. 给变量赋值

*   简单赋值，Variable(变量)=Value(值)。

    ```
    >>>a=1
    >>>b=2
    >>>print a,b
    1 2
    ```

*   多变量赋值，Variable1,variable2,...=Value1,Value2,...

    ```
    >>>a,b,c=1,2,3
    >>>print a
    1
    >>>print b
    2
    >>>print c
    3
    ```

    多变量赋值也可用于变量交换，接上例：

    ```
    >>>a,b,c=c,b,a
    >>>print a
    3
    >>>print b
    2
    >>>print c
    1
    ```

*   多目标赋值，a=b=variable

    ```
    >>> a=b=1
    >>> a
    1
    >>> b
    1
    >>> a=2
    >>> a
    2
    >>> b
    1
    ```

*   自变赋值，如+=，-=，*=等。在自变赋值中，python仅计算一次，而普通写法需计算两次；自变赋值会修改原始对象，而不是创建一个新对象。

## Chapter 3\. Python内建对象类型


在Python中，所有数据都是对象，数据有各种类型，如数值型、列表型、字符串型等。除系统内建的数据类型外，程序员也可以创建自已的数据类型。以下主要介绍Python内建的数据类型。

## 3.1\. Number数值型

在python中，数值有四种类型，分别是整型、长整形、浮点型和复数。

*   整型---从-2147483648至2147483647，有符号位32位长，可表达的最大数为2^31-1。如：number=123，number1=-123。在数字前加0x或0X 前缀表示十六进制数，在数字前加前缀0表示八进制数，与C/C++ and perl一样。

    > 为方便起见，sys模块包含一个maxint成员，该成员保留了整形变量的最大正数值。

    ```
    >>> import sys
    >>> print sys.maxint
    2147483647
    ```

*   长整型---python支持任意长度的长整型，长整型的最大值和最小值由可用的内存确定。长整型数在数字常量尾加L or l，一般都是用L，因为小写的l太容易与数字1混淆了。如：long=1232132131231232132132131L。

*   浮点数---python支持普通十进制和科学计数法表示的浮点数。如：number=123.456，nubmer1=123.2E10。浮点数在python中的存储格式与C中的双精度数相同。

*   复数---复数的实部和虚部用加号分开，虚部使用后缀j表示，如：number=1.2+2j

## 3.2\. String字符串型

*   字符串在python被看成是单个字符的序列，具有序列对象的特殊功能，字符串是固定的，不可变的。如：string="hello world"。

*   可在字符串中使用单引号和双引号。如：string="I'm a boy"。

*   字符串内部的一个反斜杠“\”可允许把字符串放于多行：如：

    ```
    >>> "test \
    ... python"
    'test python'
    ```

*   使用三个单引号或双引号可使字符串跨行显示。如：

    ```
    helptext="""this a help test.if you have any quesions.
                please call me anytime.I will help you.I
                like python.I hope so as you."""
    ```

*   使用“+”号可连接字符串。如：string = "hello" + "world"，注意，不能将字符串与其它对象进行连接。如string = "ok" + 5。其实不用“+”号，直接用空格也可连接两个字符串。如：string="hello" "world"。

*   可用“\*”号重复字符串，如：'hello'\*5会生成'hellohellohellohellohello'。

*   可用索引访问字符串中的字符。如：string="hello world"，print string[1]将显示字符e。

*   字符串可用in或not in运算符来测试字符是不属于一个字符串的成员。

*   可对字符串分片，如string="hello world",print string[6:]将显示world。分片的格式为：

    ```
                 string[start:end]
    ```

    分片和索引的规则如下：

    *   返回的字符串包含从start起始到end但不包括end结束的所有字符。

    *   若指定了start但未指定end，则一直向后分片，直至字符串结束。

    *   若指定了end但未指定start，则从0开始分片直至end，但不包括end指定的字符。

    *   若start和end为负数，则索引从字符串尾部开始算起，最后一个字符为-1。

python提供了一个string模块来进行字符串处理。

### 3.2.1\. 字符串的格式化

象C 中的sprintf函数一样，可以用“%”来格式化字符串。



**Table 3.1\. 字符串格式化代码**

| 格式 | 描述 |
| --- | --- |
| %% | 百分号标记 |
| %c | 字符及其ASCII码 |
| %s | 字符串 |
| %d | 有符号整数(十进制) |
| %u | 无符号整数(十进制) |
| %o | 无符号整数(八进制) |
| %x | 无符号整数(十六进制) |
| %X | 无符号整数(十六进制大写字符) |
| %e | 浮点数字(科学计数法) |
| %E | 浮点数字(科学计数法，用E代替e) |
| %f | 浮点数字(用小数点符号) |
| %g | 浮点数字(根据值的大小采用%e或%f) |
| %G | 浮点数字(类似于%g) |
| %p | 指针(用十六进制打印值的内存地址) |
| %n | 存储输出字符的数量放进参数列表的下一个变量中 |

> %格式化符也可用于字典，可用%(name)引用字典中的元素进行格式化输出。

> 负号指时数字应该是左对齐的，“0”告诉Python用前导0填充数字，正号指时数字总是显示它的正负(+，-)符号，即使数字是正数也不例外。

> 可指定最小的字段宽度，如："%5d" % 2。也可用句点符指定附加的精度，如："%.3d" % 3。

### 3.2.2\. 转义字符

在需要在字符中使用特殊字符时，python用反斜杠(\)转义字符。如下表：



**Table 3.2\. python支持的转义字符表**

| 转义字符 | 描述 |
| --- | --- |
| \(在行尾时) | 续行符 |
| \\ | 反斜杠符号 |
| \' | 单引号 |
| \" | 双引号 |
| \a | 响铃 |
| \b | 退格(Backspace) |
| \e | 转义 |
| \000 | 空 |
| \n | 换行 |
| \v | 纵向制表符 |
| \t | 横向制表符 |
| \r | 回车 |
| \f | 换页 |
| \oyy | 八进制数yy代表的字符，例如：\o12代表换行 |
| \xyy | 十进制数yy代表的字符，例如：\x0a代表换行 |
| \other | 其它的字符以普通格式输出 |

### 3.2.3\. Unicode字符串

在python2.0中才完全支持Unicode字符串，Unicode字符采用16位(0---65535)值表示，能进行多语言支持。要使用Unicode字符串，只要在字符串前加上“u”即可。如：

```
>>> a=u"test"
>>> print a
test
```

原始Unicode字符串用ur前缀，如：

```
>>> u'hello world\0020'
u'hello world\x020'
>>> ur'hello world\0020'
u'hello world\\0020'
```

#### 3.2.3.1\. Unicode转换

只要和Unicode连接，就会产生Unicode字串。如：

```
>>> 'help'
'help'
>>> 'help，' + u'python'     
u'help，python'
```

对于ASCII(7位)兼容的字串，可和内置的str()函数把Unicode字串转换成ASCII字串。如：

```
>>> str(u'hello world')
'hello world'
```

> 转换非ASCII兼容的字串会出错。编码和译码字符串时的错误引发UnicodeError异常。

可使用encode()函数转换Unicode字串格式：

```
u'unicode\xb1\xe0\xc2\xeb\xb2\xe2\xca\xd4'
>>> a.encode('utf-8')   #转换成utf-8，显示结果会根据终端的字符集支持不同而不同，下面是在GB18030下的显示结果
'unicode\xc2\xb1\xc3\xa0\xc3\x82\xc3\xab\xc2\xb2\xc3\xa2\xc3\x8a\xc3\x94'     
```

可使用unicode()函数把字符串转换成unicode格式，如：

```
>>> a=u'unicode测试'
>>> a
u'unicode\xb2\xe2\xca\xd4'
>>> a.encode('utf-8')     #把unicode字串转换成utf-8
'unicode\xc2\xb2\xc3\xa2\xc3\x8a\xc3\x94'
>>> b=a.encode('utf-8')   #给变量b赋值
>>> b
'unicode\xc2\xb2\xc3\xa2\xc3\x8a\xc3\x94'
>>>unicode(b,'utf-8')           #用unicode()函数把utf-8格式字串转换回unicode格式。
u'unicode\xb2\xe2\xca\xd4'      #和原始的这是a相同           
```

ord()支持unicode，可以显示特定字符的unicode号码，如：

```
>>>ord('A')
65
```

使用unichr()函数可将unicode号码转换回unicode字符，如：

```
>>> unichr(65)
u'A'
```

### 3.2.4\. 原始字符串

有时我们并不想让转义字符生效，我们只想显示字符串原来的意思，这就要用r和R来定义原始字符串。如：

```
print r'\t\r'
```

实际输出为“\t\r”。

## 3.3\. List列表

*   列表是序列对象，可包含任意的Python数据信息，如字符串、数字、列表、元组等。列表的数据是可变的，我们可通过对象方法对列表中的数据进行增加、修改、删除等操作。可以通过list(seq)函数把一个序列类型转换成一个列表。列表的几个例子：

    *   `list = [ "a", "b", "c" ]`，这是字符列表。

    *   `list = [ 1, 2, 3, 4 ]`，这是数字列表。

    *   `list = [ [1,2,3,4], ["a","b","c"] ]`，这是列表的列表。

    *   `list = [ (1,2,3,4), ("a","b","c") ]`，这是元组列表。

    *   list((1,2))把一个元组转换成一个列表[1,2]，list('test')可把字符串转换成['t','e','s','t']列表。

*   访问列表可通过索引来引用，如：list[0]将引用列表的第一个值。list[0:1]返回第一和第二个元素。

*   用range()和xrange()函数可自动生成列表，具体用法请参考“python参考篇”的内容。

*   可通过列表综合来创建列表，该功能是在python2.0版本中新增加的。如果想对列表中的每个项进行运算并把结果存储在一个新列表中，可者想创建一个仅包含特定满足某种条件的项，采用该方法是很适合的。如：[x\*x for x in range(1,10)]会得到一个X的平方的新列表；我们还可添加if条件控制输出，如：[x\*x for x in range(1,10) if x%2==0]；还可在列表中使用多个for语句，如：

    ```
    >>> [x+y for x in "123" for y in "abc"]
    ['1a', '1b', '1c', '2a', '2b', '2c', '3a', '3b', '3c']
    ```

    x,y值可取列表或元组等，以构成更复杂的结构。

*   “+”号可连接两个列表。

*   访问列表的列表(嵌套列表)可用list[1][0]，这将访问嵌套中的第二个列表的第一个元素。

*   可用数字与列表相乘以复制内容，如：list\*2会得到一个[1,2,3,4,1,2,3,4]的列表。注意，不能用列表与列表相乘。

*   由于列表是可变的，我们可用赋值语句进行操作，如：list[0] = 2。

*   列表对象方法可对列表进行操作，如列表内容的添加，删除，排序等。如list.sort()可对list列表进行排序。



    **Table 3.3\. 列表对象支持的方法**

    ```
    | 方法 | 描述 |
    | --- | --- |
    | append(x) | 在列表尾部追加单个对象x。使用多个参数会引起异常。 |
    | count(x) | 返回对象x在列表中出现的次数。 |
    | extend(L) | 将列表L中的表项添加到列表中。返回None。 |
    | Index(x) | 返回列表中匹配对象x的第一个列表项的索引。无匹配元素时产生异常。 |
    | insert(i,x) | 在索引为i的元素前插入对象x。如list.insert(0,x)在第一项前插入对象。返回None。 |
    | pop(x) | 删除列表中索引为x的表项，并返回该表项的值。若未指定索引，pop返回列表最后一项。 |
    | remove(x) | 删除列表中匹配对象x的第一个元素。匹配元素时产生异常。返回None。 |
    | reverse() | 颠倒列表元素的顺序。 |
    | sort() | 对列表排序，返回none。bisect模块可用于排序列表项的添加和删除。 |
    ```

## 3.4\. Tuple元组

Tuple(元组)和List(列表)很相似，但元组是不可变的。不能对元组中的元素进行添加，修改和删除操作。如果需修改元组内容只有重建元组。元组用小括号来表示。如tuple=(1,2,3)。

*   tuple=(1,)，这是单个元素的元组表示，需加额外的逗号。

*   tuple=1，2，3，4，这也可以是一个元组，在不使用圆括号而不会导致混淆时，Python允许不使用圆括号的元组。

*   和列表一样，可对元组进行索引、分片、连接和重复。也可用len()求元组长度。

    > 元组的索引用tuple[i]的形式，而不是tuple(i)。

*   和列表类似，使用tuple(seq)可把其它序列类型转换成元组。

## 3.5\. 序列对象

上面介绍的字符串、列表和元组的对象类型均属于称为序列的Python对象。它是一种可使用数字化索引进行访问其中元素的对象。

*   可用算术运算符联接或重复序列。

*   比较运算符(&lt;，&lt;=，&gt;，&gt;=，!=，==)也可用于序列。

*   可通过下标(test[1])，切片(test[1:3])和解包来访问序列的某部份。解包示例如下：

    ```
    >>>s=1,2,3
    >>>x,y,z=s
    >>>print x,y,z
    1,2,3
    ```

*   in运算符可判断当有对象是否序列对象成员，如:

    ```
    >>>list = [1,2,3]
    >>>1 in list
    1
    >>>4 in list
    0
    ```

*   也可通过循环运算符对序列对象进行迭代操作。如:

    ```
    for day in days:
        print day
    ```

有关序列的处理函数请参考“python参考篇”相关内容，这里就不详细讲了。

## 3.6\. Dictionary字典

字典是一个用大括号括起来的键值对，字典元素分为两部份，键(key)和值。字典是python中唯一内置映射数据类型。通过指定的键从字典访问值。如：

```
monthdays = { "Jan":31, "Feb":28, "Mar":31, "Apr":30, "May":31, "Jun":30, "Jul":31, "Aug":31, "Sep":30, "Oct":31, "Nov":30,"Dec":31 }
```

*   字典可嵌套，可以在一个字典里包含另一个字典。如test={"test":{"mytest":10} }

*   可用键访问字典，如monthdays["Jan"]，可访问值31。如果没有找到指定的键，则解释器会引起异常。

*   字典是可修改，如monthdays["Jan"]=30，可把Jan的值由31改为30。如monthdays["test"]=30可添加一个新键值对。

*   del monthdays["test"]可删除字典条目。

*   字典不属序列对象，所以不能进行连接和相乘操作。字典是没有顺序的。

*   字典提供keys和values方法，用来返回字典中定义的所有键和值。

*   和列表一样，字典也提供了对象方法来对字典进行操作。



    **Table 3.4\. 字典方法**

    ```
    | 方法 | 描述 |
    | --- | --- |
    | has_key(x) | 如果字典中有键x，则返回真。 |
    | keys() | 返回字典中键的列表 |
    | values() | 返回字典中值的列表。 |
    | items() | 返回tuples的列表。每个tuple由字典的键和相应值组成。 |
    | clear() | 删除字典的所有条目。 |
    | copy() | 返回字典高层结构的一个拷贝，但不复制嵌入结构，而只复制对那些结构的引用。 |
    | update(x) | 用字典x中的键值对更新字典内容。 |
    | get(x[,y]) | 返回键x，若未找到该键返回none，若提供y，则未找到x时返回y。 |
    ```

## 3.7\. File文件

可用内置的open()函数对文件进行操作。如：

```
input = open("test.txt")
for line in input.readlines():
    print line
input.close()
```

## 3.8\. 理解引用

*   Python把一块数据存储在对象中，变量是对象的唯一引用；它们是计算机内存中特殊地点的名字。所有对象都具有唯一的身份号、类型和值。对象的类型不会改变，对于可变类型而言，它的值是可变的。id(obj)函数可用于检索对象的身份，也就是内存中的对象的地址。

*   每个对象都包含引用计数器，它记录当前有多少个变量正在引用该对象。当给对象指定一个变量或使对象成为列表或其它包容器的成员时，引用计数就增加；当从包容器中撤消、重新分配或删除对象时，引用计数减少。当引用计数达到0值时(即没有任何变量引用这个对象)，python的回收机制会自动回收它使用的内存。注意，del可用来删除变量，但不能删除对象。

    > sys.gettrefcount(obj)函数可返回给定对象的引用计数。

## 3.9\. copy and deepcopy

通过给列表分配一个变量能创建对列表的引用，如果要创建列表的副本就要理解浅副本和深副本的概念。

*   列表或其他包容器对象的浅副本(Shallow)能够生成对象本身的副本，但也会创建对由列表包含的对象的引用。可用分片(object[:])和copy模块的copy(obj)函数创建。

*   列表或其他对象包容器对象的深副本能够生成对象本身的副本，并递归地生成所有子对象的副本。可用copy模块的deepcopy(obj)函数创建。

比较两种副本，一般情况下表现一样，但当列表内包含另一个列表的情况下，父列表的浅副本将包含对子列表引用，而不是独立副本。其结果是，当更改内部列表时，从父列表的两个副本中都可见，如：

```
>>> a=[1,2,3,[4,5]]
>>> b=a[:]
>>> b
[1, 2, 3, [4, 5]]
>>> a[3].remove(4)
>>> a
[1, 2, 3, [5]]
>>> b
[1, 2, 3, [5]]
```

如果是深副本，就不会出现这种情况。如：

```
>>> a=[1,2,3,[4,5]]
>>> b=copy.deepcopy(a)
>>> b
[1, 2, 3, [4, 5]]
>>> a[3].remove(4)
>>> a
[1, 2, 3, [5]]
>>> b
[1, 2, 3, [4, 5]]
```

## 3.10\. 标识数据类型

可通过type(obj)函数标识数据类型，如：

```
>>> type(a)
<type 'list'>
>>> type(copy)
<type 'module'>
>>> type(1)
<type 'int'>
```

types模块包含Python的内置数据类型的类型对象。如：

```
>>> import types
>>> types.ListType
<type 'list'>
>>> types.IntType
<type 'int'>
```

## 3.11\. 数组对象

数组对象与列表类似，但数组只包含某些类型的简单数据。所以当数据较简单，且要求性能好的情况下，使用数组是一个好的选择。



**Table 3.5\. 数组类型代码**


| 代码 | 等价的C类型 | 以字节为单位的最小尺寸 |
| --- | --- | --- |
| c | char | 1 |
| b(B) | byte(unsigned byte) | 1 |
| h(H) | short(unsigned short) | 2 |
| i(I) | int(unsigned int) | 2 |
| l(L) | long(unsigned long) | 4 |
| f | float | 4 |
| d | double | 8 |

数组创建方法如下：

```
>>> import array
>>> z=array.array("b")
>>> z.append(1)
>>> z
array('b', [1])
```

数组的itemsize和typecode成员可分别检索数组项的大小和数组对象的类型代码，如：

```
>>> z.itemsize
1
>>> z.typecode
'b'
```

### 3.1\. 数组类型与其它数据类型的转换

*   tolist()方法可把数组转换为列表，如：

    ```
    >>> z.tolist()
    [1, 2, 3]
    ```

    fromlist(list)方法可把列表项附加到数组的末尾，如：

    ```
    >>> z.fromlist([10,11])
    >>> z
    array('b', [1, 2, 3, 10, 11])
    ```

    > 如添加的列表类型与数组类型不同，则fromlist(list)不会把任何项添加到数组对象中。

*   tostring()方法，可以把数组转换为字节的序列，如：

    ```
    >>> z.tostring()
    '\x01\x02\x03\n\x0b'
    ```

    fromstring(list)方法刚好与tostring()相反，它获取一个字节串，并把它们转换为数组的值。如：

    ```
    >>> z.fromstring("\x0b")
    >>> z
    array('b', [1, 2, 3, 10, 11, 11])
    ```

*   tofile(file)方法可把数组转换为字节的序列，并把它们写入文件，如：

    ```
    >>> f=open("aa","wb")
    >>> z.tofile(f)
    >>> f.close()
    ```

    fromfile(file,count)方法用于从文件对象中读取特定数目的项，并把它们附加到数组中，如：

    ```
    >>> z.fromfile(open("aa","rb"),2)
    >>> z
    array('b', [1, 2, 3, 10, 11, 11, 1, 2])
    ```

    当取数项大于文件数据项时，formfile会产生EOFError异常。

*   数组对象支持列表中的很多相同函数和方法：len，append等。访问成员的方法也可列表一样，可用下标和分片。

## Chapter 4\. 控制语句

流程控制是程序设计中一个重要的内容，Python支持三种不同的控制结构：if，for和while。

*   if语句判断表达式是否为真，如果为真则执行指定语句。if语句的格式如下：

    ```
    if   EXPRESSION1:
             STATEMENT1
    elif EXPRESSION2:
             STATEMENT2
    else:
             STATEMENT3
    ```

    如果第一个表达式为真，则执行statement1，否则进行进一步的测试，如果第二个表达式为真则执行statement2，否则执行statement3。

    > 注意语句的缩进量要保持一致。在python中没有switch和case语句，我们可通过多重elif来达到相同的效果。

    示例：

    ```
    #!/usr/bin/env python

    mytest = raw_input("please input a number:")
    mytest = int(mytest)
    if mytest == 10:
            print "you input number is ten."
    elif mytest == 20:
            print "you input number is twenty."
    else:
            print "another number."
    ```

    脚本的执行效果：
    
    ```
    t03:~# python test.py
    please input a number:10
    you input number is ten.
    t03:~# python test.py
    please input a number:20
    you input number is twenty.
    t03:~# python test.py
    please input a number:777
    another number.
    ```

*   while进行循环控制，它对表达式进行测试，如果为真，则循环执行循环体。格式如下：

    ```
    while EXPRESSION:
              STATEMENT
    else:
              STATEMENT

    ```

    如果测试为假，则会执行else块。如果循环被中断(break)，则else块不会执行。

    示例：

    ```
    >>> a = 0
    >>> while a &gt; 5:
    ...     a = a + 1
    ...     print a
    ... else:
    ...     print "a's value is five"
    ...
    1
    2
    3
    4
    5
    a's value is five

    ```

*   for循环可遍历对象，并可进行迭代操作。语名格式如下：

    ```
    for TARGET in OBJECTS：
           STATEMENT
    else:
           STATEMENT

    ```

    和while一样，在循环正常退出时，会执行else块。

    示例：

    ```
    >>> mylist = "for statement"
    >>> for word in mylist:
    ...     print word
    ... else:
    ...     print "End list"
    ...
    f
    o
    r

    s
    t
    a
    t
    e
    m
    e
    n
    t
    End list

    ```

*   在循环的过程中，我们可使用循环控制语句来控制循环的执行。有三个控制语句，分别是break、continue和pass。它们的作用分别是：

    *   break语句会立即退出当前循环，不会执行else块的内容。

        示例：

        ```
        >>> mylist = ["zope","python","perl","Linux"]
        >>> for technic in mylist:
        ...     if technic == "perl":
        ...             break
        ...     else:
        ...             print technic
        ...
        zope
        python

        ```

    *   continue语句会忽略后面的语句，强制进入下一次循环。

        示例：

        ```
        >>> mylist = ["zope","python","perl","Linux"]
        >>> for technic in mylist:
        ...     if technic == "perl":
        ...             continue
        ...     else:
        ...             print technic
        ...
        zope
        python
        Linux

        ```

    *   pass不做任何事情。

        示例：

        ```
        >>> for technic in mylist:
        ...     if technic == "perl":
        ...             pass
        ...     else:
        ...             print technic
        ...
        zope
        python
        Linux

        ```

## Chapter 5\. 函数


函数是一个能完成特定功能的代码块，可在程序中重复使用，减少程序的代码量和提高程序的执行效率。在python中函数定义语法如下：

```
def function_name(arg1,arg2[,...]):
    statement
[return value]  

```

> 返回值不是必须的，如果没有return语句，则Python默认返回值None。

函数名的命名规则：

*   函数名必须以下划线或字母开头，可以包含任意字母、数字或下划线的组合。不能使用任何的标点符号；

*   函数名是区分大小写的。

*   函数名不能是保留字。

Python使用名称空间的概念存储对象，这个名称空间就是对象作用的区域， 不同对象存在于不同的作用域。下面是不同对象的作用域规则：

*   每个模块都有自已的全局作用域。

*   函数定义的对象属局部作用域，只在函数内有效，不会影响全局作用域中的对象。

*   赋值对象属局部作用域，除非使用global关键字进行声明。

LGB规则是Python查找名字的规则，下面是LGB规则：

*   大多数名字引用在三个作用域中查找：先局部(Local)，次之全局(Global)，再次之内置(Build-in)。

    ```
    >>> a=2
    >>> b=2
    >>> def test(b):
    ...     test=a*b
    ...     return test
    >>>print test(10)
    20
    ```

    b在局部作用域中找到,a在全局作用域中找到。

*   如想在局部作用域中改变全局作用域的对象，必须使用global关键字。

    ```
    #没用global时的情况
    >>> name="Jims"
    >>> def set():
    ...     name="ringkee"
    ...
    >>> set()
    >>> print name
    Jims
    #使用global后的情况
    >>> name="Jims"
    >>> def set1():
    ...     global name
    ...     name="ringkee"
    ...
    >>> set1()
    >>> print name
    ringkee
    ```

*   'global'声明把赋值的名字映射到一个包含它的模块的作用域中。

函数的参数是函数与外部沟通的桥梁，它可接收外部传递过来的值。参数传递的规则如下：

*   在一个函数中对参数名赋值不影响调用者。

    ```
    >>> a=1
    >>> def test(a):
    ...     a=a+1
    ...     print a
    ...
    >>> test(a)
    2
    >>> a
    1             # a值不变
    ```

*   在一个函数中改变一个可变的对象参数会影响调用者。

    ```
    >>> a=1
    >>> b=[1,2]
    >>> def test(a,b):
    ...     a=5
    ...     b[0]=4
    ...     print a,b
    ...
    >>> test(a,b)
    5 [4, 2]
    >>> a
    1
    >>> b
    [4, 2]    # b值已被更改
    ```

参数是对象指针，无需定义传递的对象类型。如：

```
>>> def test(a,b):
...     return a+b
...
>>> test(1,2)   #数值型
3
>>> test("a","b")   #字符型
'ab'
>>> test([12],[11])   #列表
[12, 11]

```

函数中的参数接收传递的值，参数可分默认参数，如：

```
def function(ARG=VALUE)

```

元组（Tuples）参数：

```
def function(*ARG)

```

字典（dictionary）参数：

```
def function(**ARG)

```

一些函数规则：

*   默认值必须在非默认参数之后；

*   在单个函数定义中，只能使用一个tuple参数（\*ARG）和一个字典参数（\*\*ARG）。

*   tuple参数必须在连接参数和默认参数之后。

*   字典参数必须在最后定义。

## 5.1\. 常用函数

*   abs(x)

    abs()返回一个数字的绝对值。如果给出复数，返回值就是该复数的模。

    ```
    >>>print abs(-100)
    100
    >>>print abs(1+2j)
    2.2360679775
    ```

*   callable(object)

    callable()函数用于测试对象是否可调用，如果可以则返回1(真)；否则返回0(假)。可调用对象包括函数、方法、代码对象、类和已经定义了“调用”方法的类实例。

    ```
    >>> a="123"
    >>> print callable(a)
    0
    >>> print callable(chr)
    1
    ```

*   cmp(x,y)

    cmp()函数比较x和y两个对象，并根据比较结果返回一个整数，如果x&lt;y，则返回-1；如果x&gt;y，则返回1,如果x==y则返回0。

    ```
    >>>a=1
    >>>b=2
    >>>c=2
    >>> print cmp(a,b)
    -1
    >>> print cmp(b,a)
    1
    >>> print cmp(b,c)
    0
    ```

*   divmod(x,y)

    divmod(x,y)函数完成除法运算，返回商和余数。

    ```
    >>> divmod(10,3)
    (3, 1)
    >>> divmod(9,3)
    (3, 0)
    ```

*   isinstance(object,class-or-type-or-tuple) -&gt; bool

    测试对象类型

    ```
    >>> a='isinstance test'
    >>> b=1234
    >>> isinstance(a,str)
    True
    >>> isinstance(a,int)
    False
    >>> isinstance(b,str)
    False
    >>> isinstance(b,int)
    True
    ```

*   len(object) -&gt; integer

    len()函数返回字符串和序列的长度。

    ```
    >>> len("aa")
    2
    >>> len([1,2])
    2
    ```

*   pow(x,y[,z])

    pow()函数返回以x为底，y为指数的幂。如果给出z值，该函数就计算x的y次幂值被z取模的值。

    ```
    >>> print pow(2,4)
    16
    >>> print pow(2,4,2)
    0
    >>> print pow(2.4,3)
    13.824
    ```

*   range([lower,]stop[,step])

    range()函数可按参数生成连续的有序整数列表。

    ```
    >>> range(10)
    [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(1,10)
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    >>> range(1,10,2)
    [1, 3, 5, 7, 9]
    ```

*   round(x[,n])

    round()函数返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。

    ```
    >>> round(3.333)
    3.0
    >>> round(3)
    3.0
    >>> round(5.9)
    6.0
    ```

*   type(obj)

    type()函数可返回对象的数据类型。

    ```
    >>> type(a)
    <type 'list'>
    >>> type(copy)
    <type 'module'>
    >>> type(1)
    <type 'int'>
    ```

*   xrange([lower,]stop[,step])

    xrange()函数与range()类似，但xrnage()并不创建列表，而是返回一个xrange对象，它的行为与列表相似，但是只在需要时才计算列表值，当列表很大时，这个特性能为我们节省内存。

    ```
    >>> a=xrange(10)
    >>> print a[0]
    0
    >>> print a[1]
    1
    >>> print a[2]
    2
    ```

## 5.2\. 内置类型转换函数

*   chr(i)

    chr()函数返回ASCII码对应的字符串。

    ```
    >>> print chr(65)
    A
    >>> print chr(66)
    B
    >>> print chr(65)+chr(66)
    AB
    ```

*   complex(real[,imaginary])

    complex()函数可把字符串或数字转换为复数。

    ```
    >>> complex("2+1j")
    (2+1j)
    >>> complex("2")
    (2+0j)
    >>> complex(2,1)
    (2+1j)
    >>> complex(2L,1)
    (2+1j)
    ```

*   float(x)

    float()函数把一个数字或字符串转换成浮点数。

    ```
    >>> float("12")
    12.0
    >>> float(12L)
    12.0
    >>> float(12.2)
    12.199999999999999
    ```

*   hex(x)

    hex()函数可把整数转换成十六进制数。

    ```
    >>> hex(16)
    '0x10'
    >>> hex(123)
    '0x7b'
    ```

*   long(x[,base])

    long()函数把数字和字符串转换成长整数，base为可选的基数。

    ```
    >>> long("123")
    123L
    >>> long(11)
    11L
    ```

*   list(x)

    list()函数可将序列对象转换成列表。如：

    ```
    >>> list("hello world")
    ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
    >>> list((1,2,3,4))
    [1, 2, 3, 4]
    ```

*   int(x[,base])

    int()函数把数字和字符串转换成一个整数，base为可选的基数。

    ```
    >>> int(3.3)
    3
    >>> int(3L)
    3
    >>> int("13")
    13
    >>> int("14",15)
    19
    ```

*   min(x[,y,z...])

    min()函数返回给定参数的最小值，参数可以为序列。

    ```
    >>> min(1,2,3,4)
    1
    >>> min((1,2,3),(2,3,4))
    (1, 2, 3)
    ```

*   max(x[,y,z...])

    max()函数返回给定参数的最大值，参数可以为序列。

    ```
    >>> max(1,2,3,4)
    4
    >>> max((1,2,3),(2,3,4))
    (2, 3, 4)
    ```

*   oct(x)

    oct()函数可把给出的整数转换成八进制数。

    ```
    >>> oct(8)
    '010'
    >>> oct(123)
    '0173'
    ```

*   ord(x)

    ord()函数返回一个字符串参数的ASCII码或Unicode值。

    ```
    >>> ord("a")
    97
    >>> ord(u"a")
    97
    ```

*   str(obj)

    str()函数把对象转换成可打印字符串。

    ```
    >>> str("4")
    '4'
    >>> str(4)
    '4'
    >>> str(3+2j)
    '(3+2j)'
    ```

*   tuple(x)

    tuple()函数把序列对象转换成tuple。

    ```
    >>> tuple("hello world")
    ('h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
    >>> tuple([1,2,3,4])
    (1, 2, 3, 4)
    ```

## 5.3\. 序列处理函数

*   常用函数中的len()、max()和min()同样可用于序列。

*   filter(function,list)

    调用filter()时，它会把一个函数应用于序列中的每个项，并返回该函数返回真值时的所有项，从而过滤掉返回假值的所有项。

    ```
    >>> def nobad(s):
    ...     return s.find("bad") == -1
    ...
    >>> s = ["bad","good","bade","we"]
    >>> filter(nobad,s)
    ['good', 'we']
    ```

    这个例子通过把nobad()函数应用于s序列中所有项，过滤掉所有包含“bad”的项。

*   map(function,list[,list])

    map()函数把一个函数应用于序列中所有项，并返回一个列表。

    ```
    >>> import string
    >>> s=["python","zope","linux"]
    >>> map(string.capitalize,s)
    ['Python', 'Zope', 'Linux']
    ```

    map()还可同时应用于多个列表。如：

    ```
    >>> import operator
    >>> s=[1,2,3]; t=[3,2,1]
    >>> map(operator.mul,s,t)   # s[i]*t[j]
    [3, 4, 3]
    ```

    如果传递一个None值，而不是一个函数，则map()会把每个序列中的相应元素合并起来，并返回该元组。如：

    ```
    >>> a=[1,2];b=[3,4];c=[5,6]
    >>> map(None,a,b,c)
    [(1, 3, 5), (2, 4, 6)]
    ```

*   reduce(function,seq[,init])

    reduce()函数获得序列中前两个项，并把它传递给提供的函数，获得结果后再取序列中的下一项，连同结果再传递给函数，以此类推，直到处理完所有项为止。

    ```
    >>> import operator
    >>> reduce(operator.mul,[2,3,4,5])  # ((2*3)*4)*5
    120
    >>> reduce(operator.mul,[2,3,4,5],1) # (((1*2)*3)*4)*5
    120
    >>> reduce(operator.mul,[2,3,4,5],2)  # (((2*2)*3)*4)*5
    240
    ```

*   zip(seq[,seq,...])

    zip()函数可把两个或多个序列中的相应项合并在一起，并以元组的格式返回它们，在处理完最短序列中的所有项后就停止。

    ```
    >>> zip([1,2,3],[4,5],[7,8,9])
    [(1, 4, 7), (2, 5, 8)]
    ```

    如果参数是一个序列，则zip()会以一元组的格式返回每个项，如：

    ```
    >>> zip((1,2,3,4,5))
    [(1,), (2,), (3,), (4,), (5,)]
    >>> zip([1,2,3,4,5])
    [(1,), (2,), (3,), (4,), (5,)]
    ```

## Chapter 6\. 模块

模块可把一个复杂的程序按功能分开，分别存放到不同文件中，使程序更容易维护和管理。在Python中的模块是一个以.py结尾的Python代码文件。可通过import命令输入，如：

```
import sys
```

import会完成以下三个操作：

*   创建新的名称空间（namespace），该名称空间中拥有输入模块中定义的所有对象；

*   执行模块中的代码；

*   创建该名称空间的变量名。

import语句可同时输入多个模块，如：

```
import os,sys,system

```

也可写成：

```
import os
import sys
import system

```

有些模块的名称很长，我们可在输入时给它起个简单的别名，这样在使用模块中的对象就方便很多，如：

```
import ftplib as ftp

```

有时我们可能只想使用模块中某个对象，又不想把整个模块输入，则可以用from...import语句输入特定对象。如：

```
from ftplib import FTP

```

这样，我们就可直接使用FTP()，而不用带前缀。

如果装载模块出错，会引发ImportError异常。我们可捕获该异常进行相应处理。

Python脚本和模块都是一个以.py结束的文件，那程序是如何判断一个.py文件是作为脚本还是模块呢？关键是一个名为\_\_name\_\_的变量，如果它的值是\_\_main\_\_，则不能作为模块，只能作为脚本直接运行。所以在很多脚本的最后都有一段类似下面的语句，限制只能以脚本方式运行，不作为模块：

```
if __name__ == '__main__':
    main()

```

几个功能相近的模块我们可组成一个Python包，存放到一个目录结构中，通过输入包的路径来调用对象。要定义包，就要建一个与包名同名的目录，接着在该目录下创建\_\_init\_\_.py文件。该文件是包的初始化文件，可以为空，也可定义一个代码。例如一个WebDesign包的目录如下：

```
/WebDesign
        __init_.py
        design.py
        draw.py
        ...

```

我们可通过以下语句输入design模块：

```
import WebDesign.design

```

## 6.1\. String模块

*   replace(string,old,new[,maxsplit])

    字符串的替换函数，把字符串中的old替换成new。默认是把string中所有的old值替换成new值，如果给出maxsplit值，还可控制替换的个数，如果maxsplit为1，则只替换第一个old值。

    ```
    >>>a="11223344"
    >>>print string.replace(a,"1","one")
    oneone2223344
    >>>print string.replace(a,"1","one",1)
    one12223344
    ```

*   capitalize(string)

    该函数可把字符串的首个字符替换成大字。

    ```
    >>> import string
    >>> print string.capitalize("python")
    Python
    ```

*   split(string,sep=None,maxsplit=-1)

    从string字符串中返回一个列表，以sep的值为分界符。

    ```
    >>> import string
    >>> ip="192.168.3.3"
    >>> ip_list=string.split(ip,'.')
    >>> print ip_list
    ['192', '168', '3', '3']

    ```

*   join(string[,sep])

    返回用sep连接的字串，默认的sep是空格。

    ```
    >>> import string
    >>> a = ['a','b','c']
    >>> b = string.join(a,'-')
    >>> b
    'a-b-c'
    >>> a
    ['a', 'b', 'c']

    ```

## 6.2\. time模块

内置模块time包含很多与时间相关函数。我们可通过它获得当前的时间和格式化时间输出。

*   time()，以浮点形式返回自Linux新世纪以来经过的秒数。在linux中，00:00:00 UTC, January 1, 1970是新纪元的开始。

    ```
    >>> time.time()
    1150269086.6630149
    >>> time.ctime(1150269086.6630149)
    >>> 'Wed Jun 14 15:11:26 2006'

    ```

*   ctime([sec])，把秒数转换成日期格式，如果不带参数，则显示当前的时间。

    ```
    >>> import time
    >>> time.ctime()
    >>> 'Wed Jun 14 15:02:50 2006'
    >>> time.ctime(1138068452427683)
    'Sat Dec 14 04:51:44 1901'                               

    ```

*   sleep(secs)，定时。

    ```
    >>> time.sleep(10)
    >>>                #10秒后才会出现>>>提示符

    ```

## Chapter 7\. 类

类是面向对象编程的一个重要概念。通过类的创建和继承，可重用代码，减少代码复杂度。Python是一种面向对象的脚本语言，用class语句可创建类，语法规则如下：

```
class classnmae([class_parent,...]):
      ...
      def method():
          ...
...

```

一个例子：

```
#!/usr/bin/python
#-*- encoding:utf-8 -*-

class test:                              #定义一个test类
        desc = "这是一个测试类。"        #在类中定义一个属性desc

        def __init__(self,name1):        #对象构造函数，初始化类
                self.name1 = name1

        def show(self,name2):            #在类中定义一个方法show()
                print "hello world"
                print 'name1:',self.name1
                print 'name2:',name2

instance = test('这是传递给name1的值')   #生成test类的实例对象instance

print instance.desc                      #调用类中的desc属性

instance.show('这是传递给name2的值')     #调用类中的show()方法

```

把该脚本命名为test.py，并用chmod +x test.py使脚本有执行的权限 ，运行该脚本结果如下：

```
debian:~/python# ./test.py
这是一个测试类。
hello world
name1: 这是传递给name1的值
name2: 这是传递给name2的值

```

这里只是Python语言中类的一个简单介绍。详细介绍可参考网站上自由文档栏目中的Python资料。

## Chapter 8\. 异常处理

Python的异常处理能力是很强大的，可向用户准确反馈出错信息。在Python中，异常也是对象，可对它进行操作。所有异常都是基类Exception的成员。异常处理的try语法有两种，一种是：

```
try:
   block
except [exception,[data...]]:
   block
else:
   block

```

该种异常处理语法的规则是：

*   执行try下的语句，如果引发异常，则执行过程会跳到第一个except语句。

*   如果第一个except中定义的异常与引发的异常匹配，则执行该except中的语句。

*   如果引发的异常不匹配第一个except，则会搜索第二个except，允许编写的except数量没有限制。

*   如果所有的except都不匹配，则异常会传递到下一个调用本代码的最高层try代码中。

*   如果没有发生异常，则执行else块代码。

try语句的第二种语法是：

```
try:
   block
finally:
   block

```

该语句的执行规则是：

*   执行try下的代码。

*   如果发生异常，在该异常传递到下一级try时，执行finally中的代码。

*   如果没有发生异常，则执行finally中的代码。

第二种try语法在无论有没有发生异常都要执行代码的情况下是很有用的。例如我们在python中打开一个文件进行读写操作，我在操作过程中不管是否出现异常，最终我都是要把该文件关闭的。

除了系统引发的异常外，我们还可用raise语句手工引发一个异常：

```
raise [exception[,data]]

```

## Chapter 9\. 文件处理


文件是我们储存信息的地方，我们经常要对文件进行读、写、删除等的操作，在Python中，我们可用Python提供的函数和方法方便地操作文件。

## 9.1\. 文件处理的函数和方法

使用Open()函数可打开文件，语法格式如下：

```
file_handler = open(filename,[,mode[,bufsize]]

```

filename是你要操作的文件名，如果不在当前路径，需指出具体路径。mode是打开文件的模式，表示你要如何操作文件，bufsize表示是否使用缓存。



**Table 9.1\. mode**

| 模式 | 描述 |
| --- | --- |
| r | 以读方式打开文件，可读取文件信息。 |
| w | 以写方式打开文件，可向文件写入信息。 |
| a | 以追加方式打开文件，文件指针自动移到文件尾。 |
| r+ | 以读写方式打开文件，可对文件进行读和写操作。 |
| w+ | 消除文件内容，然后以读写方式打开文件。 |
| a+ | 以读写方式打开文件，并把文件指针移到文件尾。 |
| b | 以二进制模式打开文件，而不是以文本模式。该模式只对Windows或Dos有效，类Unix的文件是用二进制模式进行操作的。 |



**Table 9.2\. bufsize**

| bufsize取值 | 描述 |
| --- | --- |
| 0 | 禁用缓冲 |
| 1 | 行缓冲 |
| &gt;1 | 指定缓冲区的大小 |
| &lt;1 | 系统默认的缓冲区大小 |

open()函数返回一个文件对象，我们可通过read()或write()函数对文件进行读写操作，下面是一些文件对象方法：



**Table 9.3\. 文件对象方法**

| 方法 | 描述 |
| --- | --- |
| f.close() | 关闭文件，记住用open()打开文件后一定要记得关闭它，否则会占用系统的可打开文件句柄数。 |
| f.fileno() | 获得文件描述符 |
| f.flush() | 刷新输出缓存 |
| f.isatty() | 如果文件是一个交互终端，则返回True，否则返回False。 |
| f.read([count]) | 读出文件，如果有count，则读出count个字节。 |
| f.readline() | 读出一行信息。 |
| f.readlines() | 读出所有行，也就是读出整个文件的信息。 |
| f.seek(offset[,where]) | 把文件指针移动到相对于where的offset位置。offset为0表示文件开始处，这是默认值 ；1表示当前位置；2表示文件结尾。 |
| f.tell() | 获得文件指针位置。 |
| f.truncate([size]) | 截取文件，使文件的大小为size。 |
| f.write(string) | 把string字符串写入文件。 |
| f.writelines(list) | 把list中的字符串一行一行地写入文件。 |

## 9.2\. 示例

*   文件的打开或创建

    ```
    #!/usr/bin/env python
    #-*- encoding:UTF-8 -*-

    filehandler = open('test.txt','w')               #以写模式打开文件，如果文件不存在则创建
    filehandler.write('this is a file open/create test.\nthe second line.')

    filehandler.close()

    ```

    ```
    #!/usr/bin/env python
    #-*- encoding:UTF-8 -*-

    filehandler = open('test.txt','a')      #以追加模式打开文件，如果文件不存在则创建

    filehandler.write('\nappend the text in another line.\n')

    filehandler.close()

    ```

*   读取文件

    ```
    #!/usr/bin/env python
    #-*- encoding:UTF-8 -*-

    filehandler = open('test.txt','r')    #以读方式打开文件，rb为二进制方式(如图片或可执行文件等)

    print 'read() function:'              #读取整个文件
    print filehandler.read()

    print 'readline() function:'          #返回文件头，读取一行
    filehandler.seek(0)
    print filehandler.readline()

    print 'readlines() function:'         #返回文件头，返回所有行的列表
    filehandler.seek(0)
    print filehandler.readlines()

    print 'list all lines'                #返回文件头，显示所有行
    filehandler.seek(0)
    textlist = filehandler.readlines()
    for line in textlist:
          print line

    print 'seek() function'               #移位到第32个字符，从33个字符开始显示余下内容
    filehandler.seek(32)
    print filehandler.read()

    print 'tell() function'               #移位到文件头，从头开始显示2位字符
    filehandler.seek(0)
    print filehandler.readline()          #显示第一行内容
    print filehandler.tell()              #显示当前位置
    print filehandler.readline()          #显示第二行内容
    print filehandler.read()              #显示余下所有内容

    filehandler.close()                   #关闭文件句柄

    ```

*   文件系统操作

    ```
    #!/usr/bin/env python
    #-*- encoding:utf-8 -*-

    import os,fnmatch,glob

    for fileName in os.listdir ( '/root' ):                 #列出/root目录内容，不包括.和..
       print fileName

    os.mkdir('py')                  #在当前目录下创建一个py目录，且只能创建一层
    os.rmdir( 'py')                 #在当前目录下删除py目录，且只能删除一层
    os.makedirs('py/aa')            #可创建多层目录
    os.removedirs('py/aa')          #可删除多层目录

    print 'demonstration fnmatch module'                 
    for fileName in os.listdir ( '/root/python/file' ):
            if fnmatch.fnmatch(fileName,'*.txt'):        #利用UNIX风格的通配，只显示后缀为txt的文件
                    print fileName

    print 'demonstration glob module'
    for fileName in glob.glob ( '*.txt' ):               #利用UNIX风格的通配，只显示后缀为txt的文件
            print fileName

    ```

*   获取文件状态

    ```
    #!/usr/bin/env python
    #-*- encoding:UTF-8 -*-

    import os,time,stat

    fileStats = os.stat ( 'test.txt' )                         #获取文件/目录的状态
    fileInfo = {
    'Size':fileStats [ stat.ST_SIZE ],                         #获取文件大小
    'LastModified':time.ctime( fileStats [ stat.ST_MTIME ] ),  #获取文件最后修改时间
    'LastAccessed':time.ctime( fileStats [ stat.ST_ATIME ] ),  #获取文件最后访问时间
    'CreationTime':time.ctime( fileStats [ stat.ST_CTIME ] ),  #获取文件创建时间
    'Mode':fileStats [ stat.ST_MODE ]                          #获取文件的模式
    }
    #print fileInfo

    for field in fileInfo:                                     #显示对象内容
            print '%s:%s' % (field,fileInfo[field])

    #for infoField,infoValue in fileInfo:
    #       print '%s:%s' % (infoField,infoValue)
    if stat.S_ISDIR ( fileStats [ stat.ST_MODE ] ):             #判断是否路径
            print 'Directory. '
    else:
            print 'Non-directory.'

    if stat.S_ISREG ( fileStats [ stat.ST_MODE ] ):             #判断是否一般文件
       print 'Regular file.'
    elif stat.S_ISLNK ( fileStats [ stat.ST_MODe ] ):           #判断是否链接文件
       print 'Shortcut.'
    elif stat.S_ISSOCK ( fileStats [ stat.ST_MODe ] ):          #判断是否套接字文件     
       print 'Socket.'
    elif stat.S_ISFIFO ( fileStats [ stat.ST_MODe ] ):          #判断是否命名管道
       print 'Named pipe.'
    elif stat.S_ISBLK ( fileStats [ stat.ST_MODe ] ):           #判断是否块设备
       print 'Block special device.'
    elif stat.S_ISCHR ( fileStats [ stat.ST_MODe ] ):           #判断是否字符设置
       print 'Character special device.'

    ```

    ```
    #!/usr/bin/env python
    #-*- encoding:UTF-8 -*-

    import os.path

    fileStats = 'test.txt'

    if os.path.isdir ( fileStats ):         #判断是否路径
            print 'Directory.'
    elif os.path.isfile ( fileStats ):      #判断是否一般文件
            print 'File.'
    elif os.path.islink ( fileStats ):      #判断是否链接文件
            print 'Shortcut.'
    elif os.path.ismount ( fileStats ):     #判断是否挂接点
            print 'Mount point.'

    ```

    stat模块描述了os.stat(filename)返回的文件属性列表中各值的意义。我们可方便地根据stat模块存取os.stat()中的值。

*   串行化文件

    ```
    #!/usr/bin/env python
    #-*- encoding:UTF-8 -*-

    import pickle

    filehandler = open('pickle.txt','w')

    text = ['this is a pickle demonstrate','aa','bb']

    pickle.dump(text,filehandler)           #把text的内容序列化后保存到pickle.txt文件中

    filehandler.close()

    filehandler2 = open('pickle.txt')

    textlist = pickle.load(filehandler2)    #还原序列化字符串
    print textlist

    filehandler2.close()

    #cpickle是用C写的pickle模块，比标准的pickle速度快很多，使用方法同pickle。

    ```

*   内存文件

    ```
    #!/usr/bin/env python
    #-*- coding: utf-8 -*-

    import StringIO

    fileHandle = StringIO.StringIO ( "Let freedom ring." )   #create file in memory

    print fileHandle.read() # "Let freedom ring."

    fileHandle.close()

    #cStringIO是用C写的StringIO模块，执行速度比StringIO快。

    ```

shutil模块是一个高级的文件处理模块，可实现文件的拷贝、删除等操作。

## Chapter 10\. 正则表达式


正则表达式是一个很有用的工具，可处理复杂的字符匹配和替换工作。在Python中内置了一个re模块以支持正则表达式。

正则表达式有两种基本的操作，分别是匹配和替换。

*   匹配就是在一个文本字符串中搜索匹配一特殊表达式；

*   替换就是在一个字符串中查找并替换匹配一特殊表达式的字符串。

## 10.1\. 基本元素

正则表达式定义了一系列的特殊字符元素以执行匹配动作。



**Table 10.1\. 正则表达式基本字符**

| 字符 | 描述 |
| --- | --- |
| text | 匹配text字符串 |
| . | 匹配除换行符之外的任意一个单个字符 |
| ^ | 匹配一个字符串的开头 |
| $ | 匹配一个字符串的末尾 |

在正则表达式中，我们还可用匹配限定符来约束匹配的次数。



**Table 10.2\. 匹配限定符**


| 最大匹配 | 最小匹配 | 描述 |
| --- | --- | --- |
| * | * | 重复匹配前表达式零次或多次 |
| + | + | 重复匹配前表达式一次或多次 |
| ? | ? | 重复匹配前表达式零次或一次 |
| {m} | {m} | 精确重复匹配前表达式m次 |
| {m,} | {m,} | 至少重复匹配前表达式m次 |
| {m,n} | {m,n} | 至少重复匹配前表达式m次，至多重复匹配前表达式n次 |

据上所述，".\*"为最大匹配，能匹配源字符串所有能匹配的字符串。".\* "为最小匹配，只匹配第一次出现的字符串。如：d.\*g能匹配任意以d开头，以g结尾的字符串，如"debug"和"debugging"，甚至"dog is walking"。而d.\* g只能匹配"debug"，在"dog is walking"字符串中，则只匹配到"dog "。

在一些更复杂的匹配中，我们可用到组和运算符。



**Table 10.3\. 组和运算符**

| 组 | 描述 |
| --- | --- |
| [...] | 匹配集合内的字符，如[a-z],[1-9]或[,./;'] |
| [^...] | 匹配除集合外的所有字符，相当于取反操作 |
| A&#124;B | 匹配表达式A或B，相当于OR操作 |
| (...) | 表达式分组，每对括号为一组，如([a-b]+)([A-Z]+)([1-9]+) |
| \number | 匹配在number表达式组内的文本 |

有一组特殊的字符序列，用来匹配具体的字符类型或字符环境。如\b匹配字符边界，food\b匹配"food"、"zoofood"，而和"foodies"不匹配。



**Table 10.4\. 特殊字符序列**

| 字符 | 描述 |
| --- | --- |
| \A | 只匹配字符串的开始 |
| \b | 匹配一个单词边界 |
| \B | 匹配一个单词的非边界 |
| \d | 匹配任意十进制数字字符，等价于r'[0-9]' |
| \D | 匹配任意非十进制数字字符，等价于r'[^0-9]' |
| \s | 匹配任意空格字符（空格符、tab制表符、换行符、回车、换页符、垂直线符号） |
| \S | 匹配任意非空格字符 |
| \w | 匹配任意字母数字字符 |
| \W | 匹配任意非字母数字字符 |
| \Z | 仅匹配字符串的尾部 |
| \\ | 匹配反斜线字符 |

有一套声明(assertion)对具体事件进行声明。



**Table 10.5\. 正则表达式声明**

| 声明 | 描述 |
| --- | --- |
| ( iLmsux) | 匹配空字符串，iLmsux字符对应下表的正则表达式修饰符。 |
| ( :...) | 匹配圆括号内定义的表达式，但不填充字符组表。 |
| ( P&lt;name&gt;) | 匹配圆括号内定义的表达式，但匹配的表达式还可用作name标识的符号组。 |
| ( P=name) | 匹配所有与前面命名的字符组相匹配的文本。 |
| ( #...) | 引入注释，忽略圆括号内的内容。 |
| ( =...) | 如果所提供的文本与下一个正则表达式元素匹配，这之间没有多余的文本就匹配。这允许在一个表达式中进行超前操作，而不影响正则表达式其余部分的分析。如"Martin"其后紧跟"Brown"，则"Martin( =Brown)"就只与"Martin"匹配。 |
| ( !...) | 仅当指定表达式与下一个正则表达式元素不匹配时匹配，是( =...)的反操作。 |
| ( &lt;=...) | 如果字符串当前位置的前缀字符串是给定文本，就匹配，整个表达式就在当前位置终止。如( &lt;=abc)def表达式与"abcdef"匹配。这种匹配是对前缀字符数量的精确匹配。 |
| ( &lt;!...) | 如果字符串当前位置的前缀字符串不是给定的正文，就匹配，是( &lt;=...)的反操作。 |

正则表达式还支持一些处理标志，它会影响正则式的执行方法。



**Table 10.6\. 处理标志**

| 标志 | 描述 |
| --- | --- |
| I或IGNORECASE | 忽略表达式的大小写来匹配文本。 |

## 10.2\. 操作

通过re模块，我们就可在python中利用正则式对字符串进行搜索、抽取和替换操作。如：re.search()函数能执行一个基本的搜索操作，它能返回一个MatchObject对象。re.findall()函数能返回匹配列表。

```
>>> import re
>>> a="this is my re module test"
>>> obj = re.search(r'.*is',a)
>>> print obj
<_sre.SRE_Match object at 0xb7d7a218>
>>> obj.group()
'this is'
>>> re.findall(r'.*is',a)
['this is']

```

MatchObject对象方法



**Table 10.7\. MatchObject对象方法**

| 方法 | 描述 |
| --- | --- |
| expand(template) | 展开模板中用反斜线定义的内容。 |
| m.group([group,...]) | 返回匹配的文本，是个元组。此文本是与给定group或由其索引数字定义的组匹配的文本，如果没有组定组名，则返回所有匹配项。 |
| m.groups([default]) | 返回一个元组，该元组包含模式中与所有组匹配的文本。如果给出default参数，default参数值就是与给定表达式不匹配的组的返回值。default参数的默认取值为None。 |
| m.groupdict([default]) | 返回一个字典，该字典包含匹配的所有子组。如果给出default参数，其值就是那些不匹配组的返回值。default参数的默认取值为None。 |
| m.start([group]) | 返回指定group的开始位置，或返回全部匹配的开始位置。 |
| m.end([group]) | 返回指定group的结束位置，或返回全部匹配的结束位置。 |
| m.span([group]) | 返回两元素组，此元组等价于关于一给定组或一个完整匹配表达式的(m.start(group),m.end(group)))列表 |
| m.pos | 传递给match()或search()函数的pos值。 |
| m.endpos | 传递给match()或search()函数的endpos值。 |
| m.lastindex |
| m.lastgroup |
| m.re | 创建这个MatchObject对象的正则式对象 |
| m.string | 提供给match()或search()函数的字符串。 |

使用sub()或subn()函数可在字符串上执行替换操作。sub()函数的基本格式如下：

```
sub(pattern,replace,string[,count])

```

示例

```
>>> str = 'The dog on my bed'
>>> rep = re.sub('dog','cat',str)
>>> print rep
The cat on my bed

```

replace参数可接受函数。要获得替换的次数，可使用subn()函数。subn()函数返回一个元组，此元组包含替换了的文本和替换的次数。

如果需用同一个正则式进行多次匹配操作，我们可把正则式编译成内部语言，提高处理速度。编译正则式用compile()函数来实现。compile()函数的基本格式如下：

```
compile(str[,flags])

```

str表示需编译的正则式串，flags是修饰标志符。正则式被编译后生成一个对象，该对象有多种方法和属性。



**Table 10.8\. 正则式对象方法/属性**

| 方法/属性 | 描述 |
| --- | --- |
| r.search(string[,pos[,endpos]]) | 同search()函数，但此函数允许指定搜索的起点和终点 |
| r.match(string[,pos[,endpos]]) | 同match()函数，但此函数允许指定搜索的起点和终点 |
| r.split(string[,max]) | 同split()函数 |
| r.findall(string) | 同findall()函数 |
| r.sub(replace,string[,count]) | 同sub()函数 |
| r.subn(replace,string[,count]) | 同subn()函数 |
| r.flags | 创建对象时定义的标志 |
| r.groupindex | 将r'( Pid)'定义的符号组名字映射为组序号的字典 |
| r.pattern | 在创建对象时使用的模式 |

转义字符串用re.escape()函数。

通过getattr获取对象引用

```
>>> li=['a','b']
>>> getattr(li,'append')
>>> getattr(li,'append')('c')          #相当于li.append('c')
>>> li
['a', 'b', 'c']
>>> handler=getattr(li,'append',None)
>>> handler
<built-in method append of list object at 0xb7d4a52c>
>>> handler('cc')                      #相当于li.append('cc')
>>> li
['a','b','c','cc']
>>>result = handler('bb')
>>>li
['a','b','c','cc','bb']
>>>print result
None

```

## Chapter 11\. 调试

Python自带了一个调试器叫pdb，和Gnu的gbd类似。下面用一个简单的程序来演示pdb的功能。程序代码如下：

```
#!/usr/bin/python

import pdb
a = "aaa"
pdb.set_trace()
b = "bbb"
c = "ccc"
final = a + b + c
print final

```

该程序已导入pdb模块，并在代码中添加的pdb.set_trace()跟踪点。现在让我们来运行该程序。

```
localhost:~/python/pdb# python pdbtest.py
--Return--
> /usr/lib/python2.3/pdb.py(992)set_trace()->None
-> Pdb().set_trace()              # 从跟踪点开始执行
(Pdb) n                           # n 读入下一行代码
> /root/python/pdb/pdbtest.py(6) ()
-> b = "bbb"
(Pdb) n
> /root/python/pdb/pdbtest.py(7) ()
-> c = "ccc"
(Pdb) p b                         # p 打印变量值
'bbb'
(Pdb) l                           # l 显示当前执行位置
  2
  3     import pdb
  4     a = "aaa"
  5     pdb.set_trace()
  6     b = "bbb"
  7  -> c = "ccc"
  8     final = a + b + c
  9     print final
 10
[EOF]
(Pdb) n                          
> /root/python/pdb/pdbtest.py(8) ()
-> final = a + b + c
(Pdb) n                           # 如果命令和上次的一样，也可直接按回车，不用输入'n'
> /root/python/pdb/pdbtest.py(9) ()
-> print final
(Pdb) n
aaabbbccc
--Return--
> /root/python/pdb/pdbtest.py(9) ()->None
-> print final
(Pdb) p a,b,c,final
('aaa', 'bbb', 'ccc', 'aaabbbccc')
(Pdb)
('aaa', 'bbb', 'ccc', 'aaabbbccc')
(Pdb) n
localhost:~/python/pdb#           # 返回shell       

```

pdb还有很多命令，用help命令就可以列出所有的pdb命令，用help p可以查询p命令的说明。

## Chapter 12\. HOW-TO

本章内容记录Python的一些小技巧小知识。来源是网上摘录或自己学习所得。

*   如何判断操作系统类型

    ```
    import sys
    print sys.platform
    print sys.version

    ```

*   显示和修改python的Module搜索路径

    ```
    >>> import sys
    >>> print sys.path
    ['', '/usr/lib/python23.zip', '/usr/lib/python2.3', '/usr/lib/python2.3/plat-linux2',
     '/usr/lib/python2.3/lib-tk', '/usr/lib/python2.3/lib-dynload', '/usr/local/lib/python2.3/site-packages',
     '/usr/lib/python2.3/site-packages']
    >>> sys.path.append('/usr/lib/mypath')
    >>> print sys.path
    ['', '/usr/lib/python23.zip', '/usr/lib/python2.3', '/usr/lib/python2.3/plat-linux2',
    '/usr/lib/python2.3/lib-tk', '/usr/lib/python2.3/lib-dynload', '/usr/local/lib/python2.3/site-packages',
     '/usr/lib/python2.3/site-packages', '/usr/lib/mypath']

    ```

*   把列表转换成字符串

    ```
    >>> t=['a','b','c']
    >>> print t
    ['a', 'b', 'c']
    >>> import string
    >>> print string.join(t)
    a b c

    ```

*   运行系统程序

    ```
    >>>import os
    >>>os.system('ls')            #用os.system()可执行系统命令
    >>>exec "os.system('ls')"     #用exec可执行字符串中的命令，两个命令的效果一样。

    ```

    以上两个命令的输出都是直接显示在屏幕上，不能保存到变量中，如果我们要把输出保存起来，可用os.pope\ n()函数。

    ```
    >>>cmd = '/usr/bin/mkntpwd %s' % password
    >>>handler = os.popen(cmd,'r')
    >>>passwordString=handler.read()   #passwordString为mkntpwd程序的输出结果

    ```

    使用commands模块也可以获取程序的输出，它包含一些基于os.popen()的封装函数，使我们能更方便地获取运行系统命令和获取命令的输出，但该模块只在Unix系统下有效，不能用于Windows平台。

    ```
    >>> import commands
    >>> status,output = commands.getstatusoutput('ls -l')
    >>> print output
    总计 96564
    -rw-r--r--  1 root     root         4459 2005-12-01 10:23 2005.sxw
    -rw-r--r--  1 root     root        27511 2006-04-12 16:54 20060412_user.ods
    -rw-r--r--  1 root     root       202258 2006-01-06 16:48 2006风景-1月.jpg
    ...
    >>> print status
    0

    ```

    在Python2.4中引入一个新的模块叫subprocess，用于取代os.system、os.spawn\*、os.popen\*、popen2.\*、commands.\*。

*   编码转换

    ```
    #!/usr/bin/python
    #-*-coding:utf-8 -*-

    a=u"测试"
    b=a.encode('gb2312')
    print a
    print b

    ```

*   交换两个变量

    ```
    >>> a,b = 1,2
    >>> a,b
    (1, 2)
    >>> a,b = b,a
    >>> a,b
    (2, 1)
    >>> a
    2
    >>> b
    1

    ```

*   测试数据类型

    ```
    >>> a=123
    >>> b='test'
    >>> a
    123
    >>> b
    'test'
    >>> isinstance(a,int)
    True
    >>> isinstance(a,str)
    False
    >>> isinstance(b,int)
    False
    >>> isinstance(b,str)
    True

    ```

*   用in判断是否包含子字符串

    ```
    >>> a='this is my test'
    >>> 'is' in a
    True
    >>> 'mm' in a
    False

    ```

*   \_\_iter\_\_迭代器

    ```
    >>> a = "iterator"
    >>> t = iter(a)
    >>> t.next()
    'i'
    >>> t.next()
    't'
    >>> t.next()
    'e'
    >>> t.next()
    'r'
    >>> t.next()
    'a'
    >>> t.next()
    't'
    >>> t.next()
    'o'
    >>> t.next()
    'r'
    >>> t.next()
    Traceback (most recent call last):
      File "<stdin>", line 1, in  
    StopIteration
    ```

    自已写一个迭代器类

    ```
    >>> class reverse:
    ...     def __init__(self,data):
    ...             self.data=data
    ...             self.index=len(data)
    ...     def __iter__(self):
    ...             return self
    ...     def next(self):
    ...             if self.index == 0:
    ...                     raise StopIteration
    ...             self.index = self.index - 1
    ...             return self.data[self.index]
    ...
    >>> for char in reverse('iterator'):
    ...     print char
    ...
    r
    o
    t
    a
    r
    e
    t
    i
    >>>

    ```

*   通过getattr可以得到一个在运行时才知道具体函数名的对象的引用，能增强我们程序的灵活性。

    ```
    >>> li=['a','b']
    >>> getattr(li,'append')
    >>> getattr(li,'append')('c')          #相当于li.append('c')
    >>> li
    ['a', 'b', 'c']
    >>> handler=getattr(li,'append',None)
    >>> handler
    <built-in method append of list object at 0xb7d4a52c>
    >>> handler('cc')                      #相当于li.append('cc')
    >>> li
    ['a','b','c','cc']
    >>>result = handler('bb')
    >>>li
    ['a','b','c','cc','bb']
    >>>print result
    None
    ```

    编程示例：

    ```
    import statsout

    def output(data, format="text"):                              
        output_function = getattr(statsout, "output_%s" % format)
        return output_function(data)                              

    ```

    以上代码表示，output函数接收一个data参数和format参数，根据format参数的值，从statsout模块中取出output_text函数运行，data参数通过output_function(data)传递给了statsout模块中的output_text函数。format取不同值可从statsout模块中取出不同的函数运行（output_xxxx）。也就是说我们要运行的函数是在程序运行后才确定的。这样我们可把不同的函数以output_xxx形式命名放在statout模块中，通过以上程序可动态调用各种函数。

*   hasattr用于确定一个对象是否具有某个属性。

    语法：

    ```
    hasattr(object, name) -> bool
    ```

    判断object中是否有name属性，返回一个布尔值。

*   拆分序列

    ```
    >>> a=[c for c in 'abcdefg']
    >>> a
    ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    >>>

    ```

    按if条件拆分序列

    ```
    >>> a=[c for c in '123456' if int(c)<3]      如果if的条件为真，则执行for循环
    >>> a
    ['1', '2']
    >>> a=[c for c in '123456' if int(c)>3]      如果if的条件为假，则不执行for循环
    >>> a
    ['4', '5', '6']
    ```

*   \_\_dict\_\_记录模块或类中所有对象的信息，它以字典{name:object}的形式记录这些信息，如果wikiaction是一个模块，则可以这样显示：

    ```
    >>>import wikiaction
    >>>print wikiaction.__dict__
    {'do_test': <function do_test at 0xb7c10534>, 'do_diff': <function do_diff at 0xb7c0ef0c>, 'do_refresh': <fun
    ction do_refresh at 0xb7c1025c>, 'do_userform': <function do_userform at 0xb7c103e4>, 'getHandler': <function
     getHandler at 0xb7c105a4>, 'do_raw': <function do_raw at 0xb7c10454>, 'do_chart': <function do_chart at 0xb7
    c104c4>, 're': <module 're' from '/usr/lib/python2.3/re.pyc'>, 'pysupport': <module 'MoinMoin.util.pysupport'
     from '/usr/lib/python2.3/site-packages/MoinMoin/util/pysupport.pyc'>, 'config': <module 'MoinMoin.config' fr
    om '/usr/lib/python2.3/site-packages/MoinMoin/config.pyc'>}
    ```

*   'and'的特殊用法

    ```
    >>> 'a' and 'b'         #如果两个都为真值，返回最后一个真值
    'b'
    >>> 'b' and 'a'         #同上
    'a'
    >>> 'a' and 'b' and 'c' #同上
    'c'
    >>> '' and 'a'          #如果有假值，则返回假值
    ''
    >>> 'a' and '' and 'c'  #同上
    ''
    >>> '' and 0            #如果两个都为假值，返回第一个假值
    ''
    >>> 0 and ''            #同上
    0

    ```

*   'or'的的特殊用法

    ```
    >>> 'a' or 'b'          #如果有一个为真值，则返回第一个真值
    'a'
    >>> 'b' or 'a'          #同上
    'b'
    >>> 'a' or 'b' or ''    #同上
    'a'
    >>> 0 and '' and {}     #如果所有都是假值，则返回第一个假值
    0
    >>> {} and '' and {}    #同上
    {}

    ```

*   lambda匿名函数的用法

    ```
    >>> a=lambda c:c*2
    >>> a
    <function <lambda> at 0xb7dd710c>
    >>> a(2)
    4
    >>> a(5)
    10
    ```
