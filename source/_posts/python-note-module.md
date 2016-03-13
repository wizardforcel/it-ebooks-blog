---
title: Python 学习笔记 模块篇
date: 2016-03-13 17:26:25
tags:
  - python
---

整理：Jims of [肥肥世家](http://www.ringkee.com)

[jims.yang@gmail.com](mailto:jims.yang@gmail.com)

Copyright © 2004,2005,2006 本文遵从GNU 的自由文档许可证(Free Document License)的条款，欢迎转 载、修改、散布。

发布时间：2004年7月10日

更新时间：2006年03月01日，增加cjkcodecs模块。

<!--more-->

**Abstract**

Python为开发人员提供了丰富的模块，通过这些模块，我们就可快速开发出功能强大的程序。本笔记记录我所接触或学习过的Python模块，为想学习Python的朋友提供一个参考。

**Table of Contents**

+ [1\. Python Imaging Library(PIL)](#id2811889)
    + [1.1\. 安装](#id2811915)
        + [1.1.1\. 下载相关软件](#id2811923)
        + [1.1.2\. 开始安装](#id2809722)
+ [2\. Pmw(Python megawidgets)Python超级GUI组件集](#id2809818)
    + [2.1\. 安装](#id2809843)
    + [2.2\. 模块功能演示](#id2810164)
        + [2.2.1\. ScrolledListBox(滚动列表框)](#id2810171)
        + [2.2.2\. ScrolledText（滚动文本框）](#id2810195)
+ [3\. PyXML](#id2810219)
    + [3.1\. 安装](#id2810394)
    + [3.2\. 使用](#id2810431)
+ [4\. PyGame](#id2810447)
+ [5\. PyOpenGL](#id2810462)
+ [6\. NumPy和Numarray](#id2810479)
+ [7\. MySQLdb](#id2810500)
    + [7.1\. 安装](#id2810521)
    + [7.2\. 模块功能](#id2810555)
    + [7.3\. 模块功能演示](#id2861658)
+ [8\. Tkinter模块](#id2862112)
    + [8.1\. Tkinter简介](#id2862119)
+ [9\. PyGTK](#id2862133)
    + [9.1\. 安装](#id2862104)
    + [9.2\. 示例](#id2862080)
+ [10\. PyQt](#id2861697)
    + [10.1\. 安装](#id2861724)
+ [11\. PyMedia](#id2861855)
+ [12\. Python-ldap](#id2861875)
    + [12.1\. 示例](#id2861891)
+ [13\. ftplib -- FTP protocol client](#id2808494)
    + [13.1\. 示例](#id2808548)
+ [14\. Psyco](#id2808607)
    + [14.1\. 安装](#id2808658)
+ [15\. smtplib](#id2808709)
    + [15.1\. 示例](#id2808717)
+ [16\. XMPPPY](#id2808780)
    + [16.1\. 示例](#id2808800)
    + [16.2\. cjkcodecs](#id2808819)

## Chapter 1\. Python Imaging Library(PIL)


PIL(Python图形库)为python提供强大的图形处理的能力，并提供广泛的图形文件格式支持，当前最新的版本是1.1.4。可到以下网址[http://www.pythonware.com/products/pil/index.htm](http://www.pythonware.com/products/pil/index.htm)了解PIL的最新动态。该库能进行图形格式的转换、打印和显示。还能进行一些图形效果的处理，如图形的放大、缩小和旋转等。是Python用户进行图象处理的强有力工具。

## 1.1\. 安装

### 1.1.1\. 下载相关软件

*   到[http://www.pythonware.com/products/pil/index.htm](http://www.pythonware.com/products/pil/index.htm)下载最新版的PIL安装程序。这里介绍的是在linux下的安装方法。windows平台的安装方法较简单，只要双击安装程序，就可一步步安装好了。

*   如果要PIL支持jpeg格式文件，还需安装jpeg库文件，可到[http://www.ijg.org](http://www.ijg.org)下载，现时最新的版本是jpegsrc.v6b.tar.gz。

*   如果要PIL支持压缩功能，还要下载Zlib库，可到[http://www.gzip.org/zlib/](http://www.gzip.org/zlib/)下载zlib-1.1.4.tar.gz。

### 1.1.2\. 开始安装

*   先安装jpeg库，输入以下命令进行安装：

    ```
    tar xfz jpegsrc.v6b.tar.gz
    cd jpeg-6b
    ./configure
    make
    make test
    make install
    make install-lib

    ```

*   接着安装Zlib库，输入以下命令进行安装：

    ```
    tar xfz zlib-1.1.4.tar.gz
    cd zlib-1.1.4
    ./configure
    make
    make install

    ```

*   最后安装PIL，输入以下命令进行安装：

    ```
    tar xfz Imaging-1.1.4.tar.gz
    cd Imaging-1.1.4
    cd libImaging
    ./configure
    make
    cd ..
    python setup.py build
    python setup.py install

    ```

*   测试安装是否成功，可以在Python的命令行界面输入以下代码：

    ```
    >>>import Image
    >>>im = Image.open("test.jpg")
    >>>im.show()

    ```

    如果成功打开test.jpg图片则安装成功。注意，在linux中，需要用xv程序来显示图片，所以如果没装xv，python会提示找不到xv。可到[http://www.trilon.com/xv/downloads.html](http://www.trilon.com/xv/downloads.html)下载xv。

## Chapter 2\. Pmw(Python megawidgets)Python超级GUI组件集

Pmw是一个在python中利用Tkinter模块构建的高级GUI组件，每个Pmw都合并了一个或多个Tkinter组件，以实现更有用和更复杂的功能。如，Pmw中的一个ScrolledListBox（滚动列表框）实现了Tkinter的Scrollbar（滚动条）和ListBox（列表框）功能，使我们编程更方便。如果你在Python中开发GUI程序，Pmw是将是你的一个好帮手。

## 2.1\. 安装

现在最新的Pmw是1.2版，Pmw的安装比较简单，只要到[http://pmw.sourceforge.net/](http://pmw.sourceforge.net/)下载软件，然后用tar -zxvf命令解压文件，把解压出来的Pmw目录拷到python的模块目录下就可以了，如site-packages 目录。windows平台使用同一压缩包，安装方法也一样。安装完成后可登录进python的命令行界面运行“import Pmw”测试是否安装成功，如果没有出错信息，则安装成功，可以使用了。

## 2.2\. 模块功能演示

### 2.2.1\. ScrolledListBox(滚动列表框)

```
#ScrolledListBox used to select image.

from Tkinter import *
import Pmw

class ImageSelection( Frame ):
    """List of available images and an area to display them"""

    def __init__( self, images ):
        """Create list of PhotoImages and Label to display them"""

        Frame.__init__( self )
        Pmw.initialise()
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "Select an image" )

        self.photos = []

        #add PhotoImage object to list photos
        for item in images:
            self.photos.append( PhotoImage( file = item ) )

        #create scrolled list box with vertical scrollbar
        self.listBox = Pmw.ScrolledListBox( self, items = images,
                                            listbox_height = 3,
                                            vscrollmode = "static",
                                            selectioncommand = self.switchImage )
        self.listBox.pack( side = LEFT, expand = YES, fill = BOTH, padx = 5, pady = 5 )

        self.display = Label( self, image = self.photos[0] )
        self.display.pack( padx = 5, pady = 5 )

    def switchImage ( self ):
        """Change image in Label to current selection"""

        #get tuple containing index of selected list item
        chosenPicture = self.listBox.curselection()

        #configure label to display selected image
        if chosenPicture:
            choice = int( chosenPicture[0] )
            self.display.config( image = self.photos[ choice ] )

def main():
    images = [ "c:\python23\logo.gif", "c:\python23\china.gif", "c:\python23\canada.gif", "c:\python23\logo.gif" ]
    ImageSelection(images).mainloop()

if __name__ == "__main__":
    main()

```

![](images/ScrolledListBox.png)

### 2.2.2\. ScrolledText（滚动文本框）

```
#Copying selected text from one text area to another.

from Tkinter import *
import Pmw

class CopyTextWindow( Frame ):
    """Demonatrate ScrolledText"""

    def __init__( self ):
        """Create two ScrolledText and a Button"""

        Frame.__init__( self )
        Pmw.initialise()
        self.pack( expand = YES, fill = BOTH )
        self.master.title( "ScrolledText Demo" )

        #create scrolled text box with word wrap enable
        self.text1 = Pmw.ScrolledText( self, text_width = 25, text_height = 12,
                                       text_wrap = WORD, hscrollmode = "static",
                                       vscrollmode = "static" )
        self.text1.pack( side = LEFT, expand = YES, fill = BOTH, padx = 5, pady = 5 )

        self.copyButton = Button( self, text = "Copy >>>", command = self.copyText )
        self.copyButton.pack( side = LEFT, padx = 5, pady = 5 )

        #create uneditable scrolled text box
        self.text2 = Pmw.ScrolledText( self, text_state = DISABLED, text_width = 25,
                                       text_height = 12, text_wrap = WORD,
                                       hscrollmode = "static", vscrollmode = "static" )
        self.text2.pack( side = LEFT, expand = YES, fill = BOTH, padx = 5, pady = 5 )

    def copyText( self ):
        """set the text in the second ScrolledText"""

        self.text2.settext( self.text1.get( SEL_FIRST,SEL_LAST ) )

def main():
    CopyTextWindow().mainloop()

if __name__ == "__main__":
    main()

```

![](images/ScrolledText.png)

## Chapter 3\. PyXML


PyXML是一套用Python解析和处理XML文档的工具包，包中的4DOM是完全相容于W3C DOM规范的。它包含以下内容：

*   xmlproc: 一个符合规范的XML解析器。

*   Expat: 一个快速的，非验证的XML解析器。

*   sgmlop: a C helper module that can speed-up xmllib.py and sgmllib.py by a factor of 5.

*   PySAX: SAX 1 and SAX2 libraries with drivers for most of the parsers.

*   4DOM: A fully compliant DOM Level 2 implementation

*   javadom: An adapter from Java DOM implementations to the standard Python DOM binding.

*   pulldom: a DOM implementation that supports lazy instantiation of nodes.

*   marshal: a module with several options for serializing Python objects to XML, including WDDX and XML-RPC.

## 3.1\. 安装

到[http://sourceforge.net/project/showfiles.php group_id=6473](http://sourceforge.net/project/showfiles.php group_id=6473)下载最新版的模块，现在是PyXML-0.8.3。安装PyXML需要有python2.0以上及以上的版本。下载完成后用tar解压缩生成PyXML-0.8.3目录，进入该目录并运行python setup.py build和python setup.py install完成安装。测试方法是进入命令行交互界面运行“import xml.dom.ext"命令，如果没提示模块出错则说明安装成功。PyXML提供windows平台的安装包，下载后双击运行就可以了。

## 3.2\. 使用

由于该模块的内容较多，所以该模块的详细使用将我在“PyXML学习笔记”中单独讨论。

## Chapter 4\. PyGame

PyGame是一组用于多媒体开发和游戏软件开发的模块。

## Chapter 5\. PyOpenGL

PyOpenGL模块封装了“OpenGL应用程序编程接口”，通过该模块python程序员可在程序中集成2D和3D的图形。

## Chapter 6\. NumPy和Numarray

NumPy是Python的一个扩展库，主要用于处理任意维数的固定类型数组，它的低层代码使用C来编写，所以速度的优势很明显。Numarray是NumPy的一个改进版，用于取代NumPy。

## Chapter 7\. MySQLdb


MySQLdb模块用于连接MySQL数据库。源码位于[http://sourceforge.net/projects/mysql-python](http://sourceforge.net/projects/mysql-python)，这里还有用于zope的ZMySQLDA模块，通过它就可在zope中连接mysql数据库。

## 7.1\. 安装

安装的方法在解压目录的README文件中有详细说明。不难，这里就不详细讲了。要注意的一点是，如果你的mysql不是安装在默认的路径，而是安装在/usr/local/mysql这样的路径的话，libmysqlclient.so.12这个动态库python可能会找不到，造成import出错，解决方法是在/usr/lib下做一个符号连接，ln -s /usr/local/mysql/lib/mysql/libmysqlclient.so.12 libmysqlclient.so.12。最后在python中用import MySQLdb测试，如果没有出错信息就说明安装成功，可以连接mysql数据库了。

## 7.2\. 模块功能

*   connect()方法用于连接数据库，返回一个数据库连接对象。如果要连接一个位于host.remote.com服务器上名为fourm的MySQL数据库，连接串可以这样写：

    ```
    db = MySQLdb.connect(host="remote.com",user="user",passwd="xxx",db="fourm" )

    ```

    connect()的参数列表如下：

    *   host，连接的数据库服务器主机名，默认为本地主机(localhost)。

    *   user，连接数据库的用户名，默认为当前用户。

    *   passwd，连接密码，没有默认值。

    *   db，连接的数据库名，没有默认值。

    *   conv，将文字映射到Python类型的字典。默认为MySQLdb.converters.conversions

    *   cursorclass，cursor()使用的种类，默认值为MySQLdb.cursors.Cursor。

    *   compress，启用协议压缩功能。

    *   named_pipe，在windows中，与一个命名管道相连接。

    *   init_command，一旦连接建立，就为数据库服务器指定一条语句来运行。

    *   read_default_file，使用指定的MySQL配置文件。

    *   read_default_group，读取的默认组。

    *   unix_socket，在unix中，连接使用的套接字，默认使用TCP。

    *   port，指定数据库服务器的连接端口，默认是3306。

*   连接对象的db.close()方法可关闭数据库连接，并释放相关资源。

*   连接对象的db.cursor([cursorClass])方法返回一个指针对象，用于访问和操作数据库中的数据。

*   连接对象的db.begin()方法用于开始一个事务，如果数据库的AUTOCOMMIT已经开启就关闭它，直到事务调用commit()和rollback()结束。

*   连接对象的db.commit()和db.rollback()方法分别表示事务提交和回退。

*   指针对象的cursor.close()方法关闭指针并释放相关资源。

*   指针对象的cursor.execute(query[,parameters])方法执行数据库查询。

*   指针对象的cursor.fetchall()可取出指针结果集中的所有行，返回的结果集一个元组(tuples)。

*   指针对象的cursor.fetchmany([size=cursor.arraysize])从查询结果集中取出多行，我们可利用可选的参数指定取出的行数。

*   指针对象的cursor.fetchone()从查询结果集中返回下一行。

*   指针对象的cursor.arraysize属性指定由cursor.fetchmany()方法返回行的数目，影响fetchall()的性能，默认值为1。

*   指针对象的cursor.rowcount属性指出上次查询或更新所发生行数。-1表示还没开始查询或没有查询到数据。

## 7.3\. 模块功能演示

```
#!/usr/bin/python
import MySQLdb

try:
   connection = MySQLdb.connect(user="user",passwd="password",host="xxx",db="test")
except:
   print "Could not connect to MySQL server."
   exit( 0 )

try:
   cursor = connection.cursor()
   cursor.execute( "SELECT note_id,note_detail FROM note where note_id = 1" )
   print "Rows selected:", cursor.rowcount

   for row in cursor.fetchall():
       print "note : ", row[0], row[1]
   cursor.close()

```

## Chapter 8\. Tkinter模块


## 8.1\. Tkinter简介

Tkinter是Python默认的图形界面接口，Tkinter是一个和Tk接口的Python模块，Tkinter库提供了对Tk API的接口，它属于Tcl/Tk的GUI工具组。Tcl/Tk是由John Ousterhout发展的书写和图形设备。Tcl(工具命令语言)是个宏语言，用于简化shell下复杂程序的开发，Tk工具包是和Tcl一起开发的，目的是为了简化用户接口的设计过程。Tk工具包由许多不同的小部件，如一个按钮、一个滚动条等。通过Tk提供的这些小部件，我们就可快速地进行GUI开发。Perl、Scheme等语言也利用Tk库进行GUI开发。Tkinter是跨平台，在各种平台下都能使用。

## Chapter 9\. PyGTK


PyGTK是一个用于python GUI程序开发的GTK+库，当前版本的PyGTK需要GTK+ 2.0以上版本支持和Python 2.2以上版本支持才能运行。

## 9.1\. 安装

如果是在Debian系统中，则安装python2.3-gtk2软件包即可。如果要从源码安装，可到[http://www.pygtk.org](http://www.pygtk.org)下载最新的软件包。安装方法也很简单，和其它开源软件差不多，通过configure、make和make install三步操作就可完成。具体操作你可参考源码目录下的README和INSTALL文档，里面有详细的安装说明。注意，要成功安装PyGTK，要有相应版本的GTK+和Python支持。在源码目录下有一个examples目录，这是一个宝贵的资源，里面有很多有用的PyGTK示例代码，对我们学习PyGTK很有帮助。

## 9.2\. 示例

下面是一个PyGTK的示例，演示了PyGTK的基本概念。

```
#!/usr/bin/env python
#-*- encoding:utf-8 -*-

import pygtk
pygtk.require('2.0')
import gtk

class base:
#destroy信号的回调函数
        def destroy(self,widget,data=None):
                gtk.main_quit()

#clicked信号的回调函数
        def hello(self,widget,data):
                print 'hello ' + data + ' this is a button clicked() test'

#delete_event事件的回调函数
        def delete_event(self, widget, event, data=None):
                print "delete event occurred"
#如果delete_event事件返回假，则会触发destroy信号，从而关闭窗口。
#如果返回真，则不会关闭窗口。这个特性在当我们需要一个确认是否退出的选择对话框时是很有用。
                return gtk.FALSE

        def __init__(self):
                self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
#设置窗口的delete_event信号触发delete_event函数
                self.window.connect("delete_event", self.delete_event)
#设置窗口的destroy信号触发destroy函数
                handler1 = self.window.connect("destroy",self.destroy)
                print "handler1 is:%d" % handler1
                self.window.set_title('PyGTK 测试 window')
                self.window.set_default_size(200,200)
                self.window.set_border_width(100)
#控制窗口出现的位置
                self.window.set_position(gtk.WIN_POS_CENTER)
#生成按钮实例
                self.button1 = gtk.Button()
                self.button2 = gtk.Button()
                self.button1.set_label('label1')
                self.button2.set_label('label2')
#设置按钮的clicked信号触发hello函数，并传递‘pyGTK’字符串参数给hello函数
                handler2 = self.button1.connect("clicked",self.hello,"pyGTK")
                print "handler2 is:%d" % handler2
#设置按钮的clicked信号触发self..window对象的gtk.Widget.destroy方法
                self.button1.connect_object("clicked", gtk.Widget.destroy, self.window)
#取消handler2的功能
#               self.button.disconnect(handler2)
#设置一个不可见的横向的栏位self.box1
                self.box1 = gtk.HBox(gtk.FALSE, 0)
#把box1放到窗口中
                self.window.add(self.box1)
#把button1部件放到box1中
                self.box1.pack_start(self.button1,gtk.TRUE,gtk.TRUE,0)
                self.button1.show()
#把button2部件放到button1部件之后
                self.box1.pack_start(self.button2,gtk.TRUE,gtk.TRUE,0)
                self.button2.show()
                self.box1.show()
                self.window.show()

        def main(self):
                gtk.main()

print __name__
if __name__ == "__main__":
        base = base()
        base.main()

```

有关PyGTK的详细介绍请参考我整理的“PyGTK学习笔记”。

## Chapter 10\. PyQt

PyQt是一套用于python的Qt开发库，由一系列的模块组成，有qt, qtcanvas, qtgl, qtnetwork, qtsql, qttable, qtui and qtxml，包含有300个类和超过5750个的函数和方法。

PyQt还支持一个叫qtext的模块，它包含一个QScintilla库。该库是Scintillar编辑器类的Qt接口。

## 10.1\. 安装

到[http://www.riverbankcomputing.co.uk/pyqt/download.php](http://www.riverbankcomputing.co.uk/pyqt/download.php)下载最新的版本。安装PyQt需要先安装SIP，到以[这里](http://www.riverbankcomputing.co.uk/sip/download.php)下载。[SIP](http://www.riverbankcomputing.co.uk/sip/index.php)是一个把C\C++库转换成Python模块的工具。

*   安装SIP

    ```
    % tar -zxvf sip-4.1.1.tar.gz
    % cd sip-4.1.1
    % python configure.py -l qt          # -l qt 选项指定qt版本
    % make
    % make install

    ```

*   安装PyQt

    ```
    % tar -zxvf PyQt-x11-gpl-3.13.tar.gz
    % cd PyQt-x11-gpl-3.13
    % python configure.py
    % make 
    % make install

    ```

## Chapter 11\. PyMedia

PyMedia模块是一个用于多媒体操作的python模块。它提供了丰富而简单的接口用于多媒体处理(wav, mp3, ogg, avi, divx, dvd, cdda etc)。可在Windows和Linux平台下使用。

## Chapter 12\. Python-ldap


Python-ldap模块提供一组面向对象的API，可方便地在python中访问ldap目录服务，它基于OpenLDAP2.x。

## 12.1\. 示例

*   以下示例在python-ldap网站上有列出，这里作一下简要说明：

    ```
    #!/usr/bin/python
    #-*- coding:utf-8 -*-                          #设置源码文件编码为utf-8

    import ldap                        

    try:
       conn = ldap.open("server_name")             #server_name为ldap服务器名
       conn.protocol_version = ldap.VERSION3       #设置ldap协议版本
       username = "cn=admin,dc=company,dc=com"     #用户名
       password = "123"                            #访问密码
       conn.simple_bind(username,password)         #连接

    except ldap.LDAPError, e:                      #捕获出错信息
       print e

    baseDN = "dc=employees,dc=company,dc=com"      #设置目录的搜索路径起点
    searchScope = ldap.SCOPE_SUBTREE               #设置可搜索子路径

    retrieveAttributes = None                      #None表示搜索所有属性，['cn']表示只搜索cn属性
    searchFilter = "cn=test"                       #设置过滤属性，这里只显示cn=test的信息

    try:
       ldap_result_id = conn.search(baseDN,searchScope,searchFilter,retrieveAttributes)                                 
    #调用search方法返回结果id
       result_set = []
    while 1:
       result_type, result_data = conn.result(ldap_result_id, 0)       #通过结果id返回信息
       if result_data == []:
          break
       else:
          if result_type == ldap.RES_SEARCH_ENTRY:
             result_set.append(result_data)                  

       print result_set[0][0][1]['o'][0]       #result_set是一个复合列表，需通过索引返回组织单元(o)信息 

    except ldap.LDAPError, e:
       print e

    ```

    这里采用的是非同步方式，同步方式的连接和搜索命令后有“_s”后缀，如search_s。非同步方式需通过一个结果id来访问目录服务信息。

*   下面是一个修改目录信息的示例：

    ```
    #!/usr/bin/python
    # -*- coding:utf-8 -*-
    import ldap

    try:
       conn = ldap.open("server_name")
       conn.protocol_version = ldap.VERSION3
       username = "cn=admin,dc=company,dc=com"
       password = "123"
       conn.simple_bind_s(username,password)

    except ldap.LDAPError, e:
       print e

    try:
       dn = "cn=test,dc=employees,dc=company,dc=com"
       conn.modify_s(dn,[(ldap.MOD_ADD,'mail','test@163.com')])     #增加一个mail属性
    except ldap.LDAPError, e:
       print e

    ```

    ldap.MOD_ADD表示增加属性，ldap.MOD_DELETE表示删除属性，ldap.MOD_REPLACE表示修改属性。

*   下面是一个增加目录项的示例：

    ```
    #!/usr/bin/python
    # -*- coding:utf-8 -*-
    import ldap,ldap.modlist                 #ldap.modlist是ldap的子模块，用于格式化目录服务的数据项

    try:
            conn = ldap.open("server_name")
            conn.protocol_version = ldap.VERSION3
            username = "cn=admin,dc=company,dc=com"
            password = "123"
            conn.simple_bind_s(username,password)

    except ldap.LDAPError, e:
            print e

    try:
            dn = "cn=test,dc=card,dc=company,dc=com"
            modlist = ldap.modlist.addModlist({          #格式化目录项，除对象类型要求必填项外， 
            'cn': ['test'],                              #其它项可自由增减                       
            'objectClass': ['top', 'person', 'organizationalPerson', 'inetOrgPerson'], 
            'o': ['\xe5\xb9\xbf\xe5\xb7\x9e'],           #这些为utf-8编码的中文 
            'street': ['\xe5\xb9\xbf\xe5\xb7\x9e'],
            'sn': ['tester'],
            'mail': ['test@163.com', 'test@21cn.com'],
            'homePhone': ['xxxxxxxx'], 'uid': ['test'] })
    #       print modlist                                #显示格式化数据项，格式化后是一个元组列表
            conn.add_s(dn,modlist)                       #调用add_s方法添加目录项

    except ldap.LDAPError, e:
            print e

    ```

    其实我们也可按格式化后元组列表的形式把目录项直接写到add_s()里，省却转换的步骤。

*   下面是一个删除目录项的示例：

    ```
    #!/usr/bin/python
    # -*- coding:utf-8 -*-
    import ldap

    try:
            conn = ldap.open("server_name")
            conn.protocol_version = ldap.VERSION3
            username = "cn=admin,dc=company,dc=com"
            password = "123"
            conn.simple_bind_s(username,password)

    except ldap.LDAPError, e:
            print e

    try:
            dn = "cn=sale,dc=company,dc=com"
            conn.delete_s(dn)

    except ldap.LDAPError, e:
            print e

    ```

## Chapter 13\. ftplib -- FTP protocol client


ftplib模块定义了FTP类和一些方法，用以进行客户端的ftp编程。我们可用python编写一个自已的ftp客户端程序，用于下载文件或镜像站点。如果想了解ftp协议的详细内容，请参考[RFC959](http://www.faqs.org/rfcs/rfc959.html)。

## 13.1\. 示例

该模块是python的通用模块，所以默认应该已安装。ftplib模块使用很简单，暂时只有一个FTP类和十几个函数。下面用一个交互方式演示一下ftplib的主要功能。

```
>>> from ftplib import FTP
>>> ftp=FTP('ftp.python.org')
>>> ftp.login()
'230 Login successful.'
>>> ftp.dir()
drwxrwxr-x    7 1004     1004          512 Aug 13 01:35 pub
>>> ftp.cwd('pub')
'250 Directory successfully changed.'
>>> ftp.dir()
drwxrwxr-x    5 1000     1004         1024 Dec 24 11:04 docs.python.org
drwxrwsr-x    2 1002     1004          512 Oct 12  2001 jython
lrwx------    1 0        1003           25 Aug 03  2001 python -> www.python.org/ftp/python
drwxr-xr-x    9 1018     1004          512 Feb 02 03:44 pyvault
drwxr-xr-x    2 1005     1004          512 May 06  2003 tmp
drwxrwsr-x   59 1004     1004         3072 Feb 03 14:58 www.python.org
>>> ftp.quit()
'221 Goodbye.'

```

下面一个下载文件的示例

```
#!/usr/bin/env python

#author:Jims of www.ringkee.com
#create date: 2005/02/05
#description: Using ftplib module download a file from a ftp server.

from ftplib import FTP

ftp=FTP()

ftp.set_debuglevel(2)              #打开调试级别2，显示详细信息
ftp.connect('ftp_server','port')   #连接
ftp.login('username','password')   #登录，如果匿名登录则用空串代替即可

print ftp.getwelcome()             #显示ftp服务器欢迎信息
ftp.cwd('xxx/xxx/')                #选择操作目录
bufsize = 1024                     #设置缓冲块大小
filename='dog.jpg'                        
file_handler = open(filename,'wb').write              #以写模式在本地打开文件
ftp.retrbinary('RETR dog.jpg',file_handler,bufsize)   #接收服务器上文件并写入本地文件
ftp.set_debuglevel(0)                                 #关闭调试

ftp.quit()                                            #退出ftp服务器

```

下面一个上传文件的示例，要成功运行该脚本，需在ftp服务器上有上传文件的权限。

```
#!/usr/bin/env python

#author:Jims of www.ringkee.com
#create date: 2005/02/05
#description: Using ftplib module upload a file to a ftp server.

from ftplib import FTP

ftp=FTP()

ftp.set_debuglevel(2)
ftp.connect('ftp_server','port')
ftp.login('username','password')

print ftp.getwelcome()
ftp.cwd('xxx/xxx/')
bufsize = 1024
filename='dog.jpg'
file_handler = open(filename,'rb')
ftp.storbinary('STOR dog.jpg',file_handler,bufsize)   #上传文件
ftp.set_debuglevel(0)

file_handler.close()         #关闭文件
ftp.quit()

```

是不是很简单，其它功能可查询python的官方网站，网址是[http://docs.python.org/lib/module-ftplib.html](http://docs.python.org/lib/module-ftplib.html)。

## Chapter 14\. Psyco


Psyco是一个Python代码加速度器，可使Python代码的执行速度提高到与编译语言一样的水平。

## 14.1\. 安装

安装Psyco很简单，它有两种安装方式，一种是源码方式，一种是二进制码方式：

*   如果用源码方式安装，你需在源码的目录中调用python setup.py install命令编译生成psyco子目录，再把该子目录整个拷贝到python的site-packages目录下。

*   如果用二进制码方式安装，按[这个网址](http://psyco.sourceforge.net/psycoguide/binaries.html)列表中的python与psyco版本对应表下载合适的二进制文件，解压后会生成一个psyco-1.x的目录，把该目录下的psyco目录整个拷贝到python的site-packages目录下即可。

## Chapter 15\. smtplib


## 15.1\. 示例

smtplib模块以发送电子邮件。下面是一个示例，可发送附件。

```
#!/usr/bin/python
#-*- encoding:utf-8 -*-

import smtplib,mimetypes
from email import Encoders
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.MIMEMultipart import MIMEMultipart

msg = MIMEMultipart()                        #创建可包含附件的MIME对象
msg['Subject'] = 'this is title'
msg['From'] = 'yjnet@21cn.com'
msg['To'] = 'yjnet@21cn.com'

txt = MIMEText('这是邮件正文的中文测试。',_charset='utf-8')
msg.attach(txt)

filename = 'jdk15.tar'                      #附件名
fp = open(filename,'rb')
ctype,encoding = mimetypes.guess_type(filename)
if ctype is None or encoding is not None:
        ctype = 'application/octet-stream'
maintype,subtype = ctype.split('/',1)
m = MIMEBase(maintype,subtype)
m.set_payload(fp.read())
fp.close()
Encoders.encode_base64(m)                                             #把附件编码
m.add_header('Content-disposition','attachment',filename=filename)    #修改邮件头
msg.attach(m)                                                         #添加附件

s = smtplib.SMTP('smtp.21cn.com')                                     #连接邮件服务器
s.login('yjnet','****')                                               #登录邮件服务器
s.sendmail('yjnet@21cn.com','yjnet@21cn.com',msg.as_string())         #发送邮件
s.close()

```

## Chapter 16\. XMPPPY


Jabber服务器采用开发的XMPP协议，Google Talk也是采用XMPP协议的IM系统 。在Python中有一个xmpppy模块支持该协议。也就是说，我们可以通过该模块与Jabber服务器通信，是不是很Cool。

## 16.1\. 示例

下面是一个简单的示例，可使大家对该模块有一个大概的了解。

```
#导入xmpppy模块
>>> import xmpp
#建立Client实例，debian是我的jabber服务器名，jabber服务器的安装可参考我的Debian学习笔记。
>>> c=xmpp.Client('debian',debug=[])
#连接
>>> c.connect()
'tcp'
#验证
>>> c.auth('yangjing','12345')
'old_auth'
#登入
>>> c.sendInitPresence()
#向ringkee@debian
>>> c.send(xmpp.protocol.Message('ringkee@debian ','test message from yangjing'))
'20'
#下面测试信息接收功能，如果没有信息，则pending_data()为空
>>>c.TCPsocket.pending_data()
[]
#如果有信息，则pending_data()不为空
>>> c.TCPsocket.pending_data()
[<socket._socketobject object at 0xb795beb4>]
#接收信息
>>> c.TCPsocket.receive()
"<message type='chat' to='yangjing@debian/xmpppy' from='ringkee@debian/Gaim'><x xmlns='jabber:x:event'><composing/></x><body>message from ringkee@debian</body><html xmlns='http://jabber.org/protocol/xhtml-im'><body xmlns='http://www.w3.org/1999/xhtml'>message from <a HREF='mailto:ringkee@debian'>ringkee@debian</a></body></html></message>"
#登出
>>> c.disconnect()

```

## 16.2\. cjkcodecs

在python2.4版以前，python不能处理cjk（中国，日本和韩国）的编码，所以就有了cjkcodecs模块。安装该模块后Python就能处理cjk字符了。下载网址：[http://cjkpython.i18n.org/](http://cjkpython.i18n.org/)。