---
title: XML 学习笔记
date: 2016-03-13 12:00:17
tags:
  - xml
---

整理：Jims of [肥肥世家](http://www.ringkee.com)

[jims.yang@gmail.com](mailto:jims.yang@gmail.com)

Copyright © 2004 本文遵从GNU 的自由文档许可证(Free Document License)的条款，欢迎转载、修改、散布。

发布时间:2004年12月03日

最近更新:2006年02月17日，新增CSS内容

<!--more-->

**Abstract**

XML技术是Internet技术的又一次革命。本笔记记录标记语言的历史和发展，还有我的学习历程。

**Table of Contents**

[1\. XML简介](#id2875121)
[2\. XML语法](#id2810081)
    [2.1\. 基本语法规则](#id2810137)
    [2.2\. 良构XML文档和有效XML文档](#id2810559)
    [2.3\. XML文档的组成](#id2810333)
    [2.4\. XML文档树](#id2810496)
[3\. DTD](#id2810509)
    [3.1\. 文档类型声明](#id2861409)
    [3.2\. 元素声明](#id2861485)
    [3.3\. 属性声明](#id2861808)
        [3.3.1\. 属性类型](#id2861852)
        [3.3.2\. 属性缺省值](#id2808545)
    [3.4\. 实体](#id2808624)
[4\. XML名称空间](#id2808845)
[5\. XHTML](#id2809084)
[6\. 样式表](#id2875593)
    [6.1\. CSS2](#id2875778)
    [6.2\. XSLT](#id2876470)
    [6.3\. XPath](#id2876923)
        [6.3.1\. 匹配模式](#id2877015)
        [6.3.2\. XPath轴](#id2877227)
        [6.3.3\. 谓词](#id2877462)
        [6.3.4\. XPath表达式](#id2877773)
        [6.3.5\. XPath函数](#id2877892)
    [6.4\. XLink](#id2877959)
[7\. 分析XML](#id2878164)
    [7.1\. 分析器工具](#id2878286)
    [7.2\. Unicode](#id2878314)
[A. 附录](#id2878622)
    [A.1\. 标记语言的历史](#id2878629)
    [A.2\. XML相关技术名词解释](#id2878688)
    [A.3\. XML应用](#id2878814)

## Chapter 1\. XML简介

XML(eXtensible Markup Language，可扩展标记语言)是SGML的一个子集，但比SGML简单，用以创建可相互转换的结构化文本文档和数据文档。下面说明一下与XML相关的一些概念。

*   SGML(Standard Generalized Markup Language，标准通用标记语言)，由于IBM公司的三位先驱者Charles GoldFarb、Edward Mosher和Raymond Lorie创立，主要作为大型文档的编制工具。DTD(Document Type Definition，文档类型定义)是SGML文档的核心，它定义了SGML文档必须遵循的一组语法规则。由于它很复杂，所以只是在一些大公司或大项目中使用。直到HTML面世，它还是默默无闻。

*   HTML(Hypertext Markup Language，超文本标记语言)，它是在SGML框架中通过DTD定义的标记语言，是SGML的一种应用。它由于结构简单，容易学习而迅速普及，每个人都能很快地建立自已的页面，HTML造就了现时Internet上无数的信息资源。HTML标记只描述文档的外观，而不描述文档的内容本身--里面有什么。HTML是不明白网页内容的，这样就造成了内容搜索的差异和不确定性。另一个问题是，HTML不是可扩展的，这意味着没有一种方便的途径来扩展标记。每一个新标记的引入都会造成系统的不一致性和对标准的修订。这就是为什么现在我们用不同的浏览器浏览同一个网站时表现效果会有差异。

*   XHTML(eXtensible Hypertext Markup Language，可扩展超文本标记语言)，它是按XML规则编写的HTML，由于有统一的规则约束，所以它不会出现如HTML一样的不规范、不一致性问题。

*   XML(eXtensible Markup Language，可扩展标记语言)，继承了SGML的优点，但又没有了SGML的复杂性。XML专门为WEB应用而设计，和HTML不同，它是一种元标记语言(meta-markup language)，也就是说它没有一套能够适用于各个领域中所有用户的固守的标签和元素，相反，它允许开发者根据自已的需要定义自已的元素，XML中的X(eXtensible)就是说明了这一点。它的特点有：

    *   XML使用Unicode字符集，可生成英文、中文、希腊文或梵文等多种语言。

    *   可将多个来源(包括其他XML文档和二进制文件)汇合进一个XML文档。

    *   可利用DTD或Schema(模式）管理一致性问题。DTD主要用于文档型文档，Schema主要用数据型文档。

    *   具有很好的扩展性，可定义自已的元素和属性。

    *   通过XML可从关系数据库管理系统中提取数据到结构化文档。它还被设计成可对各种数据对象进行操作。

    *   在一个设计良好的XML应用中，XML标记不涉及文档如何显示，只表示文档的结构。

    XML被设计用来存储、支持和交换数据，而不是用来显示数据的。通常，XML被用于数据交换，而不是数据存储。

*   元数据，定义数据的数据。

*   标记语言是一种定义文档的格式语言。SGML、XML、XHML、HTML都属标记语言。

XML文档是什么？它有时是一个文件，有时是关系数据库中的一条记录，有时是由Object Request Broker(对象请求代理程序)传送的一个对象，有时是到达网络接口的一个字节流。XML文档可使不同系统、不同平台的数据实现统一接口，这就是XML真正的威力所在。下面列举几个使用XML的领域：

*   文档设计和管理，可利用XML维护公司的文档资料。

*   Web开发，利用XHTML和XSLT实现的Web页面扩展性更好，更容易维护。

*   数据库应用和程序开发，可从数据库中提取数据并生成XML文档，实现信息的跨平台、跨系统沟通。

*   定义其它语言，WML和WAP就是用通过XML建立的。

XML不是什么？

*   XML只是一种标记语言，不是一种编程语言。不存在一种编译器，把XML文档转化成可执行二进制代码。

*   XML不是一种网络传输协议，但通过网络协议传输的数据格式则可以是XML格式的。

*   XML不是数据库，不能替代Oracle或MySQL这类的关系数据库管理系统。

## Chapter 2\. XML语法


创建一个简单的index.xml文档：

```
< xml version="1.0" >
< xml-stylesheet type="text/xsl" href="basic.xsl" >
<basic>Hello World</basic>

```

下面创建一个名为basic.xsl的XML样式表(XSL)，以便在浏览器中显示XML文档内容：

```
< xml version="1.0" >
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
        <html>
           <head>
           <title>a basic stylesheet</title>
           </head>
           <body>
           <xsl:value-of select="/" />
           </body>
        </html>
</xsl:template>
</xsl:stylesheet>

```

接着在浏览器中打开index.xml文档，则可显示“Hello World”。上面两个文档都是合法的XML文件，具体的语法规则下面会详细介绍，上例可先给大家一个感性的认识。

合法的XML文档可有种意思，一个是良构文档(well-format)，即符合XML规则书写的文档；另一种是有效文档，是已验证符合一个DTD的文档。

## 2.1\. 基本语法规则

*   XML是区分大小写的；

*   所有元素的起始和结束标注必须成对出现，且要正确嵌套；

*   如果使XML说明，则它必须是XML文档的第一行：

    ```
    < xml version="1.0" >
    ```

*   元素属性必须用引号引起来，单、双引号都可以，但必须成对出现。如：

    ```
    <basic attr="1.0">
    <basic attr='1.0'>
    ```

*   XML命名规则：

    *   XML名以下划线或字母开始；

    *   XML名可包含字母、数字、句点、下划线和冒号；

    *   XML名不能包含空格；

    *   XML名不能以数字开始，但可包含数字；

    *   XML名区分大小写。

*   保留标记字符，如果要在XML中显示&lt;或&之类的标记，就要使用字符的实体形式，XML中有五种预先定义了的实体：

    ```
    &lt;          表示&lt;字符
    &gt;          表示&gt;字符
    &amp;         表示&字符
    &apos;        表示'字符
    &quot;        表示"字符
    ```

    我们也可用ENTITY自定义实体：

    ```
    <!ENTITY linux "linux is a very good system">
    这样我们可用&linux;来调用。
    ```

*   XML文档内容中的空格是有意义的，在转换后会保留。

*   空元素以&lt;开始并以/&gt;结束，如&lt;br/&gt;。

## 2.2\. 良构XML文档和有效XML文档

符合XML语法规则的XML文档称为良构文档，这些规则如下：

*   应当只有一个父标志，由父标志派生所有其它子标志，在一个文档中不能存在多个父标志。

*   嵌套元素应按正确的顺序开始和结束。

*   子标志应在父标志完成前关闭。

*   属性值应放在双引号中。

通过某个DTD或Schema验证的文档称为有效XML文档。

## 2.3\. XML文档的组成

*   XML声明：

    *   version，定义XML规范的版本号，到现在为止，只有一个版本号1.0。

    *   encoding，指定文档的编码系统。

    *   standalone，定义文档是独立的还是需要装入其他元素才能正确分析。如果XML文档没有外部实体或DTD，则可以设置为no，否则设置为yes。可用该值提高性能：如果为no，则可提高处理速度；如果设置为yes，则首先要分析文档，确定需要其他哪些文件，然后才能完全分析文档。

*   根元素，每篇XML文档都需要有且只能有一个根元素。由元素是文档的第一个元素，包含其它所有元素。下例的portal就是根元素，如：

    ```
    <portal>
     <name>jims</name>
     <email></email>
     ...
    </portal>
    ```

*   属性，每个元素都可以设置一个或多个属性，如：

    ```
    <portal>
      <name id='1',sex="male">Jims</name>
    </portal>
    ```

    元素和属性都可以表示信息，什么时候使用元素，什么时候使用属性呢？属性信息表现能力有限，它只能表示字符串。所以当需灵活表示信息时应该使用元素。一般把信息主体放到元素中，属性只放一些注释或额外的信息。

*   CDATA部份，它用&lt;![CDATA[和]]&gt;表示，它们之间的数据作为原始字符显示，唯一不能出现的标志是]]&gt;。

*   注释，注释是很重要，不论是在编写程序和文档时，所以XML也提供了注释功能，以&lt;!--开头--&gt;结尾的一对区间为注释。在以--&gt;结束之前，不能出现“--”号，“---”更不允许。

*   处理指令，处理指令以&lt; 开头以 &gt;结尾。如PHP处理指令可写成，&lt; php ... &gt;。处理指令是标记，而不是元素。因此，与注释一样，处理指令可出现在XML文档的标签外的任何位置，包括根元素之前或之后。最常见的处理指令是，xml-stylesheet样式表指令，它会告诉浏览器在显示文档时应用什么样式表。如：

    ```
    < xml-stylesheet href="sample.css" type="text/css" >
    <portal>
      <name>...</name>
    ...
    </portal>
    ```

## 2.4\. XML文档树

XML文档是一种结构化的文档，可用树的形式表示出来。树是一种由节点和分支组成的简单结构，两个节点间由分支连接。上端的节点称为父节点，下端的节点称为子节点。一个节点如果没有父节点，则称为树的根节点(根)，每个树必须有且只能有一个根节点。一个节点如果没有子节点，则称为树的叶节点。只有一个节点的树也是允许的。

## Chapter 3\. DTD


由于XML可自定义标签，所以每个人定义的标签集都会不同，如果没有一套标准来规定标签的定义原则，则应用程序就不能对XML文档进行处理。解决该问题的方案采用DTD，DTD(Document Type Definition，文档类型定义)，用于定义XML文档的编写规则。如哪些元素可出现在文档中，及元素的内容和属性的要求等。应用程序会利用这个DTD对文档进行检验，符合DTD约束规则的XML文档称之为有效文档，可以进行下一步处理，否则会报错，应用程序可捕获该错误进行相应的异常处理。检验过程是可选，这要视具体应用而定。

## 3.1\. 文档类型声明

要使用DTD进行有效性检验，就要使用文档类型定义声明指定DTD。如：

```
< xml version="1.0" standalone="no" >
<!DOCTYPE portal SYSTEM "http://www.w3c.com/dtd/portal.dtd">
<portal>
  <name>Jims</name>
  <email>Jims@163.com</email>
  <email>Jims@21cn.com</email>
</portal>

```

文档类型声明位于XML声明之后，根元素之前。如果dtd文档位于本机，可用路径名直接指出dtd文档的位置。portal.dtd的内容如下：

```
<!ELEMENT portal (name,email*)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT email (#PCDATA)>

```

上面的内容也可直接写到XML文档内，这种dtd声明方式叫内部dtd子集，如：

```
< xml version="1.0" standalone="no" >
<!DOCTYPE portal [
<!ELEMENT portal (name,email*)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT email (#PCDATA)>
]>
<portal>
  <name>Jims</name>
  <email>Jims@163.com</email>
  <email>Jims@21cn.com</email>
</portal>

```

如果dtd位于XML文档外，则叫外部dtd子集。我们可以结合内外dtd，共同组成一个dtd来为XML文档作验证。如：

```
<!DOCTYPE portal SYSTEM "external.dtd" [
<!ELEMENT portal (name,email*)>
<!ELEMENT name (#PCDATA)>
<!ELEMENT email (#PCDATA)>
]>

```

注意，使用内外dtd时，这两个dtd要互相兼容，不能有冲突。

## 3.2\. 元素声明

上节文档类型声明中的每一项都是元素声明，定义了每个元素的约束。元素声明的格式为：

```
<!ELEMENT element_name (content_model)>

```

有效文档中使用的每个元素都必须在文档的DTD中用元素声明进行声明。element_name可是任何合法的XML名称，content_model(内容模型)指定元素可以或必须包含的子元素以及子元素的顺序。下面具体介绍内容模型的内容。

*   #PCDATA，规定元素只包含已析的字符数据。下面声明指出一个name元素可以包含文本，但不能划分为独立的area_code、number和extension元素：

    ```
    <!ELEMENT name (#PCDATA)>
    ```

*   子元素，可指明元素的子元素。下面声明表示name元素必须包含且只包含一个desc元素。

    ```
    <!ELEMENT name (desc)>
    ```

    也可用逗号为分隔符，指明多个子元素。并且子元素出现的次序必须按定义时的顺序。如：

    ```
    <!ELEMENT name (id,desc)>
    ```

    name元素的id子元素必须在desc子元素前面，否则验证会出错，该文档不是一个有效的XML文档。

    ```
    下面这个文档是有效的
    <name>
       <id>1</id>
       <desc>dtd test</desc>
    </name>
    下面这个文档是无效的，顺序颠倒了
    <name>
       <desc>dtd test</desc>
       <id>1</id>
    </name>
    下面的文档也是无效的，有多余的元素
    <name>
       <id>1</id>
       <desc>dtd test</desc>
       <date>2005/01/31</date>
    </name>
    ```

*   子元素的个数，我们可通过正则表达式来规定子元素的个数。

    *   ，允许零个或一个该元素

    *   \*，允许零个或多个该元素

    *   +，允许一个或多个该元素

    下面我们可利用这些符号规定id子元素必须出现，且只能出现一次，而desc子元素可选。

    ```
    <!ELEMENT name (id，desc*)>
    ```

    根据上面的声明，下面的name元素都是有效的。

    ```
    <name>
       <id>1</id>
       <desc>dtd test</desc>
    </name>
    <name>
       <id>2</id>
    </name>
    <name>
       <id>3</id>
       <desc>dtd test</desc>
       <desc>another test</desc>
    </name>
    ```

*   可选项(|)，选项是一个参数列表，每个参数间用“|”分隔，代表能且只能选一个子元素。

    ```
    <!ELEMENT choice (good | bad)>
    ```

    上例的choice元素可选一个good子元素，或bad子元素，且只能从选一个。可选的参数列可以多项，不限于两项。如：

    ```
    <!ELEMENT choice (one | two | three | four)>
    ```

*   小括号，可用小括号把选项括起来，以表达更丰富的意思，如我们想表示choice元素必须包含一个good子元素，并且必须包含ok子元素或bad子元素的一个。

    ```
    <!ELEMENT choice (good，(ok|bad))>
    ```

*   混合内容，在一些文档中，一个元素可能既包含子元素，也包含字符串，这些内容叫混合内容。可用以下方式表示：

    ```
    <!EMEMENT description (#PCDATA | term)* )>
    ```

    该声明表示description元素可包含已析的字符串和term子元素，且允许出现零次或多次，如：

    ```
    <description>
    this is a <term>dtd</term> test.
    </description>
    ```

    #PCDATA必须在第一位，可选的子元素可任意多项。

*   空元素，某些元素不用包含任何内容，称之为空元素。写成以/&gt;结束的独立标签。

    ```
    <!ELEMENT image EMPTY>
    ```

    示例：

    ```
    <image src="http://www.xml.com/dtd.jpg" />
    ```

*   ANY，允许元素内包含任意内容。该选项在dtd测试时很有用，在生产系统中尽量不要使用。

    ```
    <!ELEMENT page ANY>
    ```

## 3.3\. 属性声明

一个有效的XML文档，必须对元素的属性进行声明。使用ATTLIST声明来完成，一个ATTLIST可以为一个元素类型声明多个属性。

```
<!ATTLIST image src CDATA #REQUIRED>

```

上例声明image元素必须有一个src属性，该属性的值是字符数据。可用ATTLIST声明为一个元素声明多个属性，如：

```
<!ATTLIST image src    CDATA #REQUIRED
                width  CDATA #REQUIRED
                height CDATA #REQUIRED
                alt    CDATA #IMPLIED
>

```

上述声明指出src、width、height属性是必须的，alt属性是可选的。

### 3.3.1\. 属性类型

*   CDATA类型属性值可包含任意文本字符串。DTD不能指定属性为一个整数或一个日期，Schema能提供更为强大的数据类型。

*   NMTOKEN类型属性值是一个XML名称记号。XML名称记号与XML名称类似，但XML名称记号允许所有的字符作为名称的开始字符，而XML名称的第一个字母必须是字母、表意字符和下划线。因此10，.bashrc是合法的XML名称标记，但不是合法的XML名称。每个XML名称都是一个XML名称标记，然而XML名称标记不全是XML名称。如果属性包含1990，2005之类的整数，则应该指定其类型为NMTOKEN。如：

    ```
    <!ELEMENT person birthday NMTOKEN #REQUIRED>
    ```

*   NMTOKENS类型属性包含一个或多个用空白分隔的XML名称记号。如：

    ```
    <person dates="02-01-2005 03-01-2005 05-01-2005">person</person>
    ```

    对应的声明应为：

    ```
    <!ATTLIST person dates NMTOKENS #REQUIRED>
    ```

    另一方面，对01/02/2005这样的形式不能使用该声明，因为其中的正斜杠不是合法的名称字符。

*   枚举声明，枚举不用关键字。直接列举所有的值，中间用竖线分隔。如：

    ```
    <!ATTLIST date month(January | February | March | April | May | June | July | August | September | October | November | December) #REQUIRED>
    ```

    针对上述声明，date元素的month属性可选十二个月份的中一个。

*   ID类型的属性必须包含一个XML名称，而且该名称在文档中是独一无二的。ID属性可为元素分配一个唯一的标识符。

    ```
    <!ATTLIST name card_id ID #REQUIRED>
    ```

    由于数字不是合法的XML名称，所以ID编号不能以数字开头，解决办法是在前面加下划线或字母。

*   IDREF类型的属性指向文档中某元素的ID类型的属性。因此，它必须是一个XML名称，它的作用是当简单的包含关系不能满足要求时在元素间建立多对多关系。如：

    ```
    <project project_id="p1">
       <goal>deploy linux</goal>
       <team_member person_card_id="c123">
    </project>
    <person card_id="c123">
       <name>linuxsir</name>
       <assignment project_project_id="p1">
    </person>
    ```

    project元素的project_id属性和person元素的card_id属性应该是ID类型。team_member元素的person_card_id属性和assignment元素的project_project_id属性是IDREF类型。对应的声明如下：

    ```
    <!ATTLIST person  card_id    ID #REQUIRED>
    <!ATTLIST project project_id ID #REQUIRED>
    <!ATTLIST team_member person_card_id     IDREF #REQUIRED>
    <!ATTLIST assignment  project_project_id IDREF #REQUIRED>
    ```

*   IDREFS类型的属性包含一个XML名称列表。名称间用空白间隔，且每个名称都是文档中某个元素的ID。当某个元素需要引用多个其他元素时使用该元素。如：

    ```
    <!ATTLIST person card_id    ID     #REQUIRED
                     assignment IDREFS #REQUIRED>
    <!ATTLIST project project_id ID     #REQUIRED
                     team        IDREFS #REQUIRED>
    ```

    对应的文档可写成：

    ```
    <project project_id="p1" team="c123">
       <gold>deploy linux</gold>
    </project>
    <person card_id="c123" assignment="p1">
       <name>Linuxsir</name>
    </person>
    ```

*   ENTITY类型的属性包含在DTD的其它位置声明的未析实体的名称中。如movie元素可能有一个标识激活时播放mpeg或rm文件的实体属性：

    ```
    <!ATTLIST movie src ENTITY #REQUIRED>
    ```

    如果DTD声明了一个名为play的未析实体，则此movie元素可用于在XML文档中嵌入视频文件：

    ```
    <movie src="play" />
    ```

*   ENTITIES类型的属性包含在DTD的其它位置声明的多个未析实体名称，其间用空白隔开。

    ```
    <!ATTLIST slide_show slides ENTITIES #REQUIRED>
    ```

    如果DTD声明了未析实体slide1、slide2、slide3、...，则可使用slide_show元素在XML文档中嵌入幻灯片。

    ```
    <slide_show slides="slide1 slide2 slide3" />
    ```

*   NOTATION类型的属性包含在文档的DTD中声明的某个记法的名称。该属性类型较少用。理论上，可以使用该属性使某些特殊元素与类型相关联，下例声明为不同的图像类型定义了4个记法，然后规定每个image元素都必须从中选择一种type属性。

    ```
    <!NOTATION gif SYSTEM "image/gif">
    <!NOTATION tiff SYSTEM "image/tiff">
    <!NOTATION jpeg SYSTEM "image/jpeg">
    <!NOTATION png SYSTEM "image/png">
    <!ATTLIST image type NOTATION (gif | tiff | jpeg | png) #REQUIRED>
    ```

    每个image元素的type属性的值可以为gif，tiff，jpeg和png四个值中的一个。该属性比枚举类型稍具优势，因为记法的实际MIME媒体类型在理论上是可用的。由于斜杠在XML名称中不是一个合法字符，所以枚举类型不能指定image/png或image/jpeg作为允许值。

### 3.3.2\. 属性缺省值

每个ATTLIST声明除了要提供一种数据类型外，还要声明属性的缺省行为。

*   #IMPLIED，属性可选。

*   #REQUIRED，属性必须有。

*   #FIXED，属性是常量，不能更改。

    ```
    <!ATTLIST person name CDATA #FIXED "linuxsir"
    ```

*   Literal，作为一个引用字符串的实际缺省值。

    ```
    <!ATTLIST person name NMTOKEN "linuxsir"
    ```

    如果没有显示指明person元素的name属性，则该值为linuxsir。

## 3.4\. 实体

*   用ENTITY声明定义实体。如：

    ```
    <!ENTITY linux "linux is a very good system">
    用&linux;可引用该字符串
    ```

*   可定义一个外部实体，引用外部XML文档

    ```
    <!ENTITY linux SYSTEM "/home/linux/test.xml">
    使用&linux;可引用/home/linux/test.xml文档
    ```

    外部实体没有XML声明，但可以有文本声明，两者很类似，主要区别是文本声明必须有编码声明，而版本信息则是可选的。

    ```
    < xml version="1.0" encoding="gb2312" >    是一个合法的文本声明
    < xml encoding="gb2312" >                  也是一个合法的文本声明
    ```

*   不是所有的数据都是XML。如jpeg照片，mpeg电影等。XML建议使用外部未析实体作为在文档中嵌入这些内容的机制。DTD为包含非XML数据的实体指定一个名称和URI。

    ```
    <!ENTITY movie SYSTEM "/home/linux/test.avi" NDATA avi>
    ```

    由于数据不是XML格式，所以使用NDATA声明指定数据类型。avi是在NOTATION中定义的MIME媒体类型。在XML中嵌入未析实体很复杂且不规范，尽量不要使用。

*   参数实体可定义一组通用的实体，在文档中可通过该参数实体来引用实体。参数实体的定义与通用实体定义类似，只是中间多了一个%，引用时也是用%代码&。

    ```
    <!ENTITY % person "name,address,postcode">
    引用方法
    %person;
    这样会用name,address,postcode代替参数实体%person;
    ```

*   通常DTD都比较大，DocBook的DTD长达11000多行，如果把它存放在单一文件中，管理和维护起来都非常困难。我们可以使用外部DTD子集，把一个大的DTD按功能分成不同的功能块，存放在不同的文件中。再通过外部参数实体声明引入当前DTD中，如：

    ```
    定义参数实体引用外部names.dtd
    <!ENTITY % names SYSTEM "names.dtd">
    调用外部DTD子集
    %names;
    ```

*   使用IGNORE关键字可注释声明，如:

    ```
    <![IGNORE[
       <!ELEMENT note (#PCDATA)>
    ]]>
    ```

    当然了，使用&lt;!-- 注释 --&gt;的方式也是一样的。

*   INCLUDE关键字表示DTD中的确在使用给定的声明，如：

    ```
    <![INCLUDE[
       <!ELEMENT note (#PCDATA)>
    ]]>
    ```

    单从该声明来看，有没有使用INCLUDE效果都一样，但如果组合INCLUDE和IGNORE，可实现DTD功能的选择。我们可定义一个参数实体：

    ```
    <!ENTITY % note_allowed "INCLUDE" >
    ```

    然后使用参数实体引用而不使用关键字：

    ```
    <![%note_allowed;[
       <!ELEMENT note (#PCDATA)>
    ]]>
    ```

    按上述操作，元素声明是有效的，但我们也可以把参数实体%note_allowed重新定义为IGNORE，这样，该元素声明就无效了。

## Chapter 4\. XML名称空间

*   XML名称空间表示XML名称的使用范围，因为XML可自定义元素标签，所以有不同XML应用间XML名称重名的机会是很大的。如果没有一种方法来区分不应用的名称，就会造成混乱。XML名称空间就是为了解决这个问题而设计的。通过XML名称空间，我们可以区分来自不同的XML应用的具有相同名称的元素和属性。可以将来自单一XML应用的相关元素和属性集合在一起，方便软件识别和处理。

*   名称空间由前缀和本地部分组成，中间用冒号分隔。前缀标识元素或属性的所在名称空间，本地部分标识名称空间中的某个元素或属性。整个名称也称为限定名称(qualified name)。前缀可以用除XML(大小写任意组合)三个字母外的任何合法的XML名称字符组成。每个限定名称中的前缀都必须与唯一的一个URI关联。带有相同URI关联的前缀的名称属于同一名称空间。

    ```
    <rdf:RDF xmlns:rdf="http://www.w3.org/TR/REC-rdf-syntax#">
     <rdf:Description about="http://www.example.com/test.xml">
       <title>example</title>
       <author>linuxsir</author>
       ...
     </rdf:Description>
    </rdf:RDF>
    ```

    上例rdf:RDF元素的xmlns:rdf属性将前缀rdf绑定到名称空间 http://www.w3.org/TR/REC-rdf-syntax# 。属性xmlns:rdf为rdf:RDF元素及其子元素声明了前缀rdf。RDF处理器将把rdf:RDF和rdf:Description作为RDF元素，因为两个元素都具有与RDF规范定义的某个URI相绑定的前缀。处理器不会认为title，author等元素为RDF元素，因为它没有绑定到相同URI的rdf前缀。

    前缀一般在使用该前缀的最上层元素中定义。在下层元素中也可定义不同的前缀：

    ```
    <rdf:RDF xmlns:rdf="http://www.w3.org/TR/REC-rdf-syntax#">
     <rdf:Description xmlns:dc="http://www.w3.org/dc/"
                      about="http://www.example.com/test.xml">
       <dc:title>example</dc:title>
       <dc:author>linuxsir</dc:author>
       ...
     </rdf:Description>
    </rdf:RDF>
    ```

    不带前缀的属性，如about，不属于任何的名称空间。如xlink:type和xlink:href属性属于xlink名称空间，当然，前提是你要先把xlink绑定到一个URI。URI不必须是一定存在的http链接，它只是一种表示的方法，以区分不同的名称空间。

*   通过将无前缀的xmlns属性附加到根元素中，可以指定不带前缀的元素及所有不带前缀的子元素属于某个名称空间。

    ```
    <svg xmlns="http://www.w3.org/2000/svg">
       <ellipse rx="110" ry="130" />
       <rect x="4cm" y="1cm" />
    </svg>
    ```

    这里，虽然所有元素都没有前缀，但它都同属一个名称空间。但属性属不同名称空间，因为默认名称空间只应用于元素。默认名称空间在子元素中也用相同的方法重新设置。

*   如果名称空间只用来识别来自某种XML应用的元素和属性，而不是用来区分具有相同名称的不同元素，则可在DTD的元素中定义一个固定的xmlns属性，而不需要文档中定义。定义方法如下：

    ```
    <!ATTLIST svg xmlns CDATA #FIXED "http://www.w3.org/svg/">
    ```

*   在定义DTD时，需要使用名称空间前缀的在定义时也要把前缀写到DTD定义里，如：

    ```
    <!ELEMENT xlink:name (#PCDATA)>
    ```

*   使用参数实体引用来定义名称空间前缀可方便DTD文档的维护，如：

    ```
    <!ENTITY % prefix "xlink">
    <!ENTITY % colon ":">
    ```

    接着，利用该参数实体名称定义更多的参数实体引用，如：

    ```
    <!ENTITY % xlink-title "%prefix;%colon;title">
    <!ENTITY % xlink-author "%prefix;%colon;author">
    ```

    这样，如果需更改前缀，只需修改一个地方就可以了，不用整篇文档修改。

    ```
    <!ELEMENT %xlink-title;  (#PCDATA)>
    <!ELEMENT %xlink-author; (#PCDATA)>
    ```

    不能在ATTLIST和ELEMENT声明中直接使用%prefix;和%colon；，因为在另一个实体的外部使用这些参数实体时，XML解析器会在实体替换文本的两边添加额外的空格。

## Chapter 5\. XHTML

XHTML是W3C推荐的一种标准，它定义了一种与XML兼容的HTML版本。XHTML文档是一个有效的XML文档，所以编写格式比HTML严格。如果需从HTML文档转换成XHTML文档，需作以下更改：

*   在XHTML中不允许省略结束标签，所以需补齐缺少的标签。

*   元素需按正确的顺序嵌套。

*   所有元素和属性的名称都采用小写。

*   属性值需添加引号，如&lt;p align="center"&gt;。

*   所有属性都需有属性值。

*   采用&和&lt;等的实体形式表示这些字符。

*   确保文档有单一根元素，最好用html。

*   像&lt;hr&gt;这样的空元素要改成&lt;hr/&gt;或&lt;hr&gt;&lt;hr/&gt;。

*   注释应由&lt;! 注释 &gt;的形式改成&lt;!-- 注释 --&gt;。

*   文档编码应采用UTF-8或UTF-16，或者添加XML声明指定文档的编码方式。

*   需去掉非标准的元素。如：marguee。

*   添加一个DOCTYPE声明，用PUBLIC来指向XHTML的三种DTD中的一种。分别是Strict、Transitional和Frameset，一般使用Strict。

    *   Strict(严格型)，W3C推荐的XHTML形式。不包括一些非标准的元素和属性，如applet和center等。声明方式如下：

        ```
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                             "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
        ```

    *   Transitional(过渡型)，一种不太严格的XHTML格式，可使用一些非标准的元素和属性，如applet和bgcolor等。声明方式如下：

        ```
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                             "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
        ```

    *   Frameset(框架型)，与过渡型DTD类似，允许使用与框架相关的元素，如frameset和iframe。声明方式如下：

        ```
        <!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                             "http://www.w3.org/TR/xhtml1/DTD/xhtml1-frameset.dtd">
        ```

*   文档的根元素必须具有xmlns属性，标识缺省的名称空间提 http://www.w3.org/1999/xhtml 。

下面是一个标准的XHTML文档的示例：

```
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN"
                     "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns:"http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-type" content="text/html; charset=gb2312">
<title>xhtml example</title>
</head>
<body>
...
</body>
</html>

```

由HTML转到XHTML是一种枯燥而乏味的工作，现在有一种叫tidy的开源工具可帮我们完成大部份的工作，它是一个C程序，使用方法如下：

```
% tidy --output-xhtml yes test.html test.xml

```

XHTML 1.1把XHTML的三种DTD分成独立模块。我们可根据实际情况包含或省去某些模块。这些模块是：

*   Structure Module(结构模块)---&gt;%xhtml-struct.module;，包含HTML文档主要的元素，如：html、head、title和body。

*   Text Module(文本模块)---&gt;%xhtml-text.module;，包含文本的基本元素和其内联元素，如：h1、h2、...、strong、span等。

*   Hypertext Module(超链接模块)---&gt;%xhtml-hypertext.module;，包含用于链接的元素，如：a元素。

*   List Module(列表模块)---&gt;%xhtml-list.module;，包含用于列表的元素，如：dl、dt、dd、ul、ol和li。

*   Applet Module(applet模块)---&gt;%xhtml-applet.module;，Java所需要元素，如：applet和param。

*   Presentation Module(表示模块)---&gt;%xhtml-pres.module;，面向表示的标记：b、big、hr、I、small、sub、sup和tt。

*   Edit Module(编辑模块)---&gt;%xhtml-edit.module;，用于修正的元素，如：del和ins。

*   Bidirectional Text Module(文本方向模块)---&gt;%xhtml-bdo.module;，用于指定文本阅读的方向，如bdo元素。

*   Basic Forms Module(基本表单模块)---&gt;%xhtml-basic-form.module;，用于HTML 3.2的表单元素，如：form、input、select、option和textarea。

*   Forms Module(表单模块)---&gt;%xhtml-form.module;，用于HTML 4.0的表单元素，如：form、input、select、option、textarea、button、fieldset、label、legend和optgroup。

*   Basic Tables Module(基本表格模块)---&gt;%xhtml-basic-table.module;，基本的表格元素，如：table、caption、th、tr和td。

*   Table Module(表格模块)---&gt;%xhtml-table.module;，安全功能的表格支持，如：table、caption、th、tr、td、col、colgroup、tbody、thead和tfoot。

*   Image Module(图像模块)---&gt;%xhtml-image.module;，包含img元素。

*   Client-side Image Map Module(客户端图像映像模块)---&gt;%xhtml-csismap.module;，包含map和area元素以及支持客户端图像映像所需要的元素的属性。

*   Server-side-Image Map Module(服务器端图像映像模块)---&gt;%xhtml-ssismap.module;，该模块没有添加新元素，但对img元素添加了一个ismap属性。

*   Object Module(对象模块)---&gt;%xhtml-object.module;，用于在网页中嵌入可执行内容，如：java程序。

*   Param Module(参数模块)---&gt;%xhtml-param.module;，网页中可执行内容中传递参数的param元素。

*   Frames Module(框架模块)---&gt;%xhtml-frames.module;，包含实现框架所需的元素，如：frame、frameset和noframes。

*   Iframe Module(内联框架模块)---&gt;%xhtml-iframe.module;，包含内联框架的iframe元素。

*   Intrinsic Events(固有事件模块)---&gt;%xhtml-events.module;，支持如onSubmit和onFocus等脚本的属性。

*   Meta-information Module(元信息模块)---&gt;%xhtml-meta.module;，包含meta元素。

*   Scripting Module(脚本模块)---&gt;%xhtml-script.module;，支持JavaScript等脚本。

*   Stylesheet Module(样式表模块)---&gt;%xhtml-style.module;，用于定义CSS的style元素。

*   Link Module(链接模块)---&gt;%xhtml-link.module;，指定外部文件，如样式表、库等关系的link元素。

*   Base Modue(基模块)---&gt;%xhtml-base.module;，包含base元素，指定解析相对URL所参照的基URL。

*   Target Module(目标模块)---&gt;%xhtml-target.module;，用于指定目标框架或框架中某个窗口的target属性。

*   Style Attribute Module(样式属性模块)---&gt;%xhtml-inlstyle.module;，将CSS样式应用于文档中单个元素的style属性。

*   Name Identification Module(名称标识模块)---&gt;%xhtml-nameident.module;，name属性是id属性的早期版本，现在不推荐使用。

*   Legacy Module(传统模块)---&gt;%xhtml-legacy.module;，不推荐使用的元素和属性，如：basefont、center、fonts、strike和u元素。

*   Ruby Module(Ruby模块)---&gt;%xhtml-ruby.module;，东亚文本中用于将少量文本放于正文文本旁边的ruby、rbc、rtc、rb、rt和rp元素，一般用来指示发音。

## Chapter 6\. 样式表


样式表可帮我们解释XML文档中各元素的具体意思，所以通过样式表可直接在浏览器上显示XML文档。目前主要的样式表语言有：

*   CSS1(Cascading Stylesheets Level 1，层叠式样式表1)

*   CSS2(Cascading Stylesheets Level 2，层叠式样式表2)

*   XSLT(XSL Transformations 1.0 XSL 转换 1.0)

在XML文档在序言部分通过xml-stylesheet处理指令可指定关联的样式表。xml-stylesheet指令必须有一个href属性和type属性。href指向样式表的URL，type指定样式表的MIME类型：对CSS为text/css，对于XSLT为text/xml或application/xml。下面是一个简单的使用样式表的XML文档：

```
< xml version="1.0" >
< xml-stylesheet href="test.css" type="text/css" >
...

```

除以上两个必须的属性外，还有4种可选属性：

*   media，标识该样式应用于什么媒体，如报纸(paper)、计算机监视器(screen)、电视(tv)或所有(all)。

*   charset，指明样式表采用字符集编码方式，如：utf-8。

*   alternate，指明是否有可选的样式表，默认为no，表明是主样式表，如果为yes，则是备用样式表。

*   title，在有alternate的前提下，title用于指定不同样式表的标题。如：

    ```
    < xml-stylesheet href="big.css" type="text/css" alternate="yes" title="Large fonts" >
    < xml-stylesheet href="small.css" type="text/css" alternate="yes" title="Small fonts" >
    < xml-stylesheet href="medium.css type="text/css" title="Normal fonts" >       #默认的主样式表
    ```

样式表现在已成为Web应用中的一个关键技术，它的作用主要体现在以下三个方面：

*   设计一个样式表可以应用于多个文档。样式表可以存在于XML文档外，XML文档可通过链接使用样式表。这意味着如果你有几千个文档，都可以链接到同一个样式表中，改变一个样式表等于改变几千个文档的显示效果。

*   实现内容和表现的分离，增强文档的一致性和可维护性。通过单一的样式表，实现所有文档显示的一致。如果显示样式有变动，我们只需维护有限的几个样式表就可以了。

*   实现一个文档，多个样式。通过样式表，可把一篇文档以HTML形式、PDF形式或文本形式显示出来。

## 6.1\. CSS2

CSS2是层叠样式表，它是一种排版技术，能让元素按特定的样式显示，如字体大小，颜色、布局等。在网页中有三种使用方法：

*   用&lt;style&gt;标记声明，如

    ```
    <style>
    div {font-size: 12pt;}
    div {color: blue;}
    </style>
    ```

*   在元素中用style属性指定，如：

    ```
    <div style="font-size: 12pt;color: blue">CSS测试</div>
    ```

*   用LINK标记链接一个外部CSS文件，如：

    ```
    <link rel="stylesheet" type="text/css" href="mycss.css">
    ```

按作用域来分，有三类的样式表，分别是网页解释器样式表、作者样式表和浏览者样式表。网页解释器样式表也叫默认的样式表，当没有另外的样式表加载时使用。作者样式表就是网页设计师设计的样式表。浏览者样式表是浏览网页的用户在浏览器上另外设置的样式表。

CSS的基本数据类型

*   integer，表示整数，可取正负值。如：12，-24。

*   number，表示数字，可取正负值和小数。如：12.1，-14.3。

*   lenght，表示距离长度，可取正负值和小数，后跟一个单位，如:12em，12cm。单位又分相对单位和绝对单位，相对单位有：em，ex，px。绝对单位有：in(英寸)，cm(公分)，mm(公厘)，pt(等于1/72英寸)，pc(等于12pt)。

*   percentage，表示百分比值，可取正负和小数。如：20%，-40%。

*   uri，表示网络资源。如： http://www.ringkee.com 。

inherit参数值

```
<style>
body {width: 600px;}
.div1 {width: 120%;}
.div2 {width: inherit;}
说明：
div1的宽度是600px*120%
div2的宽度继承父元素body的参数，是600px

```

选择符的作用是指定哪些元素使用哪些样式。选择符可以分为简单选择符和复合选择符两类，简单选择符是类型选择符、通用选择符加上零个或多个属性选择符、ID选择符、伪类等组成。复合选择符是用"&gt;"和"+"号结合多个简单选择符组成。"&gt;"和"+"号两边要加上空格。下面介绍各种选择符：

*   通用选择符，用"*"号表示，可用于所有标记。如：

    ```
    <style>
    * {font-size: 14pt;}
    *.EM {color: red;}
    </style>
    <div>应用字体样式</div>
    <em class="EM">应用红色样式</em>
    ```

*   类型选择符，与标记名一样，只作用已该标记上。如：

    ```
    <style>
    div {font-size: 14pt;}
    </style>
    <div>应用样式</div>
    ```

*   子代选择符，HTML标记是可嵌套的，子代选择符可把样式表应用于子嵌套的子标记上，如：

    ```
    <style>
    div p b {font-size: 14pt;}
    </style>
    <div>
    <p>没有应用样式</p>
    <p><b>应用样式</b></p>
    </div>
    ```

*   子选择符，与子代选择符类似，但它只调用第一层子元素。如：

    ```
    <style>
    div > b {color: red;}
    div p > em {color: green;}
    </style>
    <div><b>当b标记是div标记的子标记时应用红色样式</b></div>
    <div><p><em>当em是p的子标记且p是div的子标记时应用绿色样式</em></p></div>
    ```

*   邻近选择符，当两个元素位于同一层且在位置是前后关系时，可以使用邻近选择符。两个选择符用"+"号分开，如果A位于B之前，则B可应用样式。如：

    ```
    <style>
    div + p {color: red;}
    </style>
    <div>没有应用样式</div>
    <p>应用红色样式。</p>
    ```

*   属性选择符，HTML标记有属性，我们可为特定的属性指定样式。有四种写法，分别是：

    *   [属性]，样式只应用于指定的属性。

    *   [属性=值]，样式只应用于指定的属性与值都相同的情况

    *   [属性~=值]，样式只应用于指定的属性且属性值包含指定值的情况，属性值是用空格分隔的字符串。

    *   [属性|=值]，样式只应用于指定的属性且属性值是的第一个字符串是指定值的情况，属性值是用"-"分隔的字符串。

    ```
    <style>
    [href] {color: red;}
    A[href="http://www.ringkee.com"] {color: green;}
    table[summary~="table"] {color: black;}
    table[summary|="this-is-a-table"] {color: blue;}
    </style>
    <a href="http://www.python.org">应用红色样式</a>
    <a href="http://www.ringkee.com">应用绿色样式</a>
    <table summary~="This is a table>
     <tr>
      <td>应用黑色样式</td>
     </tr>
    </table>
    <table summary|="This-is-a-table>
     <tr>
      <td>应用蓝色样式</td>
     </tr>
    </table>
    ```

*   类选择符，与属性选择符类似，但它只指对class属性应用样式。类选择符用"."语法，如.value与[class~=value]是一样的。

    ```
    <style>
    .myid {color: red;}
    </style>
    <div class="myid">应用红色样式</div>
    ```

*   ID选择符，与属性选择符类似，但它只指对ID属性，用"#"语法。

    ```
    <style>
    #myid {color: red;}
    </style>
    <div id="myid">应用红色样式</div>
    ```

*   :first-child伪类，当标记是另一个标记的第一个子标记时，应用样式。

    ```
    <style>
    p:first-child {color: red;}
    </style>
    <p>p是body的第一个子标记，应用红色样式</p>
    <div>测试</div>
    <p>p标记是body的第三个子标记，不应用红色样式</p>
    ```

*   :link和:visited伪类只作用于a标记，在指定href属性的前提下，:link表示a标记还没被点击时的样式，:visited表示被当点后的样式。

    ```
    <style>
    a:link {color: blue;}
    a:visited {color: red;}
    </style>
    <a href="http://www.ringkee.com">链接没点击前是蓝色的，点击后是红色的</a>
    ```

*   :hover，:active和:fouce伪类也只能作用于a标记，且也要指定href属性。:hover指定当用户把鼠标移到a标记上并且指针变成手型时应用的样式。:active指定点击a链接并放开鼠标时所显示的样式。:fouce指定用户点击a标记瞬间，即链接成为焦点时所显示的样式。:hover要放在:link和:visited之后，否则:hover的样式会覆盖:link和:visited的样式。

    ```
    <style>
    a:link {color: blue;}
    a:visited {color: red;}
    a:haover {color: green;}
    a:focus {color: black;}
    a:active {color: white;}
    </style>
     <a href="http://www.ringkee.com">应用样式</a>
    ```

*   :left及:right伪类只作用于页面内容。当页面在左边时应用:left指定的样式，当页面在右边时应用:right指定的样式。

*   :first-line只对div和p标记不效，样式只应用于这两个标记内的第一行内容。

    ```
    <style>
    :first-line {color: red;}
    </style>
    <div width:50px;>
    该元素内的第一行内容应用红色样式。
    </div>
    ```

*   :first-letter伪类也只能作用于div和p标记，与:first-line不同的是它只作用于标记内的第一个字符。如果我们想要每一行的开头字符大一点就可使用该伪类。

    ```
    <style>
    :first-letter {font-size: 40pt;}
    </style>
    <p>这行文字开头第一个字符的大小是40pt</p>
    ```

*   :before和:after伪类可在内容的前面或后面增加特定的内容或指定样式。

    ```
    <style>
    p:before {content: "("; color: red;}
    p:after {content: ")"; color: green;}
    </style>
    <p>这行文字前后会增加一对括号，前括号为红色</p>
    <p>这行文字前后会增加一对括号，后括号为绿色</p>
    ```

*   层叠选择符是指当有多个选择符的样式都应用于同一个标记时的选择规则。该规则利用一个三位数来确定，数字最大的就可选中。这三位数的确定规则的这样的，如果选择符中有ID选择符，则百位数加1,否则为0。如果有属性选择符、类选择符或伪类选择符，则十位数加1，否则为0。如果有类型选择符，则个位数加1，否则为0。如果选择符是#div div，这三位数则是101。让我们分析一下，#div是ID选择符，所以在百位数上加1，div是类型选择符，所以个位数上加1变成101。"*"表示0，优先级最低。

样式表的主要功能是指定同一个文件在不同媒体上按不同的样式显示。通过在种方式可指定不同媒体

*   @media方式

    ```
    <style>
    @media screen {div{color:red;}}
    @media print {div{color:green;}}
    </style>
    <div>不同媒体显示不同颜色</div>
    ```

*   @import是另一种指定不同媒体的方式，它可引入外部的css文档。它的语法格式是：

    ```
    <style>
    @import url("simple.css") screen;
    </style>
    ```

*   在HTML4.0中，可以用LINK标记的media属性为不同媒体类型指定样式表。

    ```
    <LINK rel="stylesheet" href="import.css" type="text/css" media="print">
    ```

!important规则会改变应用样式的优先级，有!important参数样式的优先级最高，会优先显示。

```
<style>
h1 {color:red;}
h1 {color:green !important;}
</style>

<h1>字体为绿色</h1>

```

## 6.2\. XSLT

XSLT是XSL的一部份，它是XML的一种应用，指定将一篇XML文档转换成另一种XML文档的规则。XSLT文档即是一篇XML文档，也是一个样式表，里面包含一系列的模板。XSLT处理器对输入XML文档中的元素和样式表中的模板进行比较，如果匹配，则将该模板的内容写入一个输出树中。完成处理后，将输出树串行化成一篇XML文档或其它格式的文档，如HTML或者rtf。

XSLT几个关键术语

*   源树，原始文档中的元素和元素内容的树。

*   结果树，转换之后中文档中的元素和元素内容的树。

*   模板规则，XSLT样式表的基础，分为模式和模板两部份。整个xsl:template元素。

*   模式，表示源树中的元素与模式规则匹配的条件集合。xsl:template中的match的值。

*   模板，表示当应用模板规则时，结果树中要实例化的部份。xsl:template元素中的内容。

XSLT定义了35个元素，分为三类：

两个根元素

*   xsl:stylesheet根元素，XSLT也是一个XML文档，该文档的根元素就是xsl:stylesheet。XSLT元素都属于名称空间`xmlns:xsl="http://www.w3.org/1999/XSL/Transform"`，所以所有的XSLT元素都有xsl前缀。一个最小化XSLT文档：

    ```
    < xml version="1.0" >
    <xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
    </xsl:stylesheet>
    ```

*   xsl:transform元素，作用同上。

13个顶级元素，可直接作为根元素的子元素，包括：

*   xsl:apply-imports

*   xsl:attribute-set

*   xsl:decimal-format

*   xsl:import

*   xsl:include

*   xsl:key

*   xsl:namespace-alias

*   xsl:output

*   xsl:param

*   xsl:preserve-space

*   xsl:strip-space

*   xsl:template模板元素，用于匹配XML文档中的元素。如：&lt;xsl:template match="person"&gt;，匹配XML文档中的person元素。

*   xsl:variable

20个指令元素

*   xsl:apply-imports

*   xsl:apply-template应用模板元素，用于显示指定的元素值(内容)。如：&lt;xsl:apply-template select="name"&gt;，显示name元素的值。

*   xsl:attribute

*   xsl:call-template

*   xsl:choose

*   xsl:comment

*   xsl:copy

*   xsl:copy-of

*   xsl:element

*   xsl:fallback

*   xsl:for-each

*   xsl:if

*   xsl:message

*   xsl:number

*   xsl:otherwise

*   xsl:processing-instruction

*   xsl:text

*   xsl:value-of选择元素，用于计算元素的值(内容)。如：&lt;xsl:value-of select="name"&gt;，获得XML文档中name元素的值(内容)。

*   xsl:variable

*   xsl:when

XSLT函数

## 6.3\. XPath

XPath是一种用来从文档树中选择节点和节点集的语言。从XPath的角度来看，共有七种节点：

*   根节点

*   元素节点

*   属性节点

*   文本节点

*   注释节点

*   处理指令节点

*   名称空间节点

CDATA部份，实体引用和文档类型声明不包括在内，XPath在所有这些项都并入文档之后才起作用。根节点和根元素是不同的两个概念，根节点包含整篇文档，包括根元素。

### 6.3.1\. 匹配模式

匹配模板的通用模式



**Table 6.1\.**

| 模式 | 描述 |
| --- | --- |
| match="E" | 匹配元素E |
| match="*" | 匹配任意元素 |
| match="E&#124;F" | 匹配元素E和F |
| match="E/F" | 匹配以E为父元素的元素F |
| match="E//F" | 匹配以E为根元素的元素F |
| match="/" | 匹配根节点 |
| match="text()" | 匹配文本节点 |
| match="comment()" | 匹配注释节点 |
| match="processing-instruction()" | 匹配处理指令 |
| match="node()" | 匹配除属性节点和根节点外的节点 |
| match="id(test)" | 匹配具有唯一ID test的元素 |
| match="E[@CLASS="foo"] | 匹配元素E，其类属性为foo |
| match="E[F]" | 匹配元素包含有F元素的E元素 |

### 6.3.2\. XPath轴

XPath提供了选择节点的机制，两个较有用的是轴选择和谓语选择，轴指定上下文节点和要选择的节点的关系。共有十三种轴，最常用的有四种，分别是子轴(child)、属性轴(attribute)、自已(self)、双亲(parent)。



**Table 6.2\. XPath轴描述**

| 轴 | 描述 |
| --- | --- |
| child | 包含当前节点的儿子 |
| descendent | 包含当前节点的后代，后代不包含属性(attribute)或名称域(namespace)节点 |
| parent | 包含当前节点的父亲 |
| ancestor | 包含当前节点的祖先，祖先总是包含根节点 |
| following-sibling | 包含当前节点随后的所有节点树，但不包含attribute或namespace节点 |
| preceding-sibling | 包含当前节点之前的所有节点树，但不包含attribute或namespace节点 |
| following | 包含当前节点随后的所有节点，following轴排除了当前节点的后代和attribute或namespace节点 |
| preceding | 包含当前节点之前的所有节点，following轴排除了当前节点的后代和attribute或namespace节点 |
| attribute | 包含当前节点的所有属性 |
| namespace | 包含当前节点的所有namespace节点 |
| self | 只包含当前节点 |
| descendent-or-self | 包含当前节点和当前节点的后代 |
| ancestor-or-self | 包含当前节点和当前节点的祖先 |

### 6.3.3\. 谓词

XPath表达式可以匹配多个节点，如需对匹配的节点进行进一步的筛选，可以使用谓词。



**Table 6.3\. 选择节点常用谓词**

| 谓词 | 描述 |
| --- | --- |
| select="E" | 选择是当前节点的孩子的E元素 |
| select="" | 选择当前节点的孩子的所有元素 |
| select="text()" | 选择当前节点的文本节点孩子 |
| select="@name" | 选择当前节点的name属性 |
| select="@*" | 选择当前节点的所有属性 |
| select="E[1]" | 选择当前节点的孩子的第一个E元素 |
| select="E[last()]" | 选择当前节点的孩子的最后一个E元素 |
| select="*/E" | 选择当前节点的孙了的所有E元素 |
| select="E//F" | 选择从当前节点的孩子的E元素派生而来的元素F |
| select="//" | 选择根元素 |
| select="//E" | 选择从根节点派生而来的E元素 |
| select="//E/F" | 选择所有是从根节点派生而来的E元素的孩子的F元素 |
| select="." | 选择当前节点 |
| select=".//E" | 选择从当前节点派生而来的所有E元素 |
| select=".." | 选择当前节点的父节点 |
| select="../@name" | 选择当前节点的父节点的name属性 |
| select="E[@name='foo']" | 选择所有是当前节点的孩子，并且其name属性具有foo值的E属性，除等号外，还可用&lt;，&gt;，&lt;=，&gt;=和!= |
| select="E[@foo and @bar]" | 选择所有包含foo和bar属性的E元素 |

home/person/@id这种定位路径的写法叫简写定位路径，该写法简洁，容易理解，是XSLT匹配模式中最常用的写法。还有一种称为非简写定位路径的写法，它把节点测试和轴结合在一起，如child::home/child::person/attribute::id。该写法在实际使用中不常用，但它具有非常重要的性能因此有必要了解。

### 6.3.4\. XPath表达式

位置路径是XPath的一个最常用的表达式，用以标识XML文档的节点集。除此之上，XPath表达式还可返回数字、布尔和字符串。非节点集的XPath表达式不能用于xsl:template元素的match属性中。它们用于xsl:value-of元素的select属性值或用于位置路径的谓词中。

每个XPath位置路径可分为一步名多步，每步以“/”号分隔，如：

```
room[\@name=$root]/date[year=$year and month=$month]/meeting

```

上下文节点即当前正在处理的节点，也就是位置路径定位的当前节点。上下文在XPath表达式计算前被创建，由XSLT处理器创建。处理每一步后，上下文都会改变。

位置路径中的步可分为三部份：轴(axis)、节点测试(note test)和谓词(predicate)，它的写法如下：

```
axis::note-test[predicate]

```

轴和节点测试之间用“::”分开，每个谓词由括号［］括起来。

要设计好一个位置路径，需确保在每一步选择最少的节点，使用最严格的轴，用最严格的节点测试。避免使用谓词，因为由轴和节点测试选择的节点集的每个节点都会用作谓词的上下文节点。对于位置路径的三步，最节省的是节点测试。

XPath中的所有数字都是8个字节的IEEE754浮点双精度类型，与java的double类型相同。可表示正无穷大、负无穷大和NaN(零除零)值。支持五种运算符，分别是加(+)、减(-)、乘(*)、除(div)、取余(mod)。

XPath中的字符串是Unicode字符，用单引号或双引号定界。可以使用=和!=对字符进行比较，也可用&lt;，&gt;，&lt;=，&gt;关系运算符，但比较的两个字符必须是数字，否则比较结果没有意义。

XPath中的布尔值常用于位置路径的谓词中，如/person[name="debian"]。布尔值还常用于xsl:if和xsl:when元素的test属性中。如：

```
<xsl:template match="home">
   <xsl:if test = ".='debian' or .='redhat'">
      <xsl:value-of select = "." />
   </xsl:if>
</xsl:template>

```

### 6.3.5\. XPath函数

XPath还提供很多函数，用于表达式和谓词。XPath函数的返回值有四种类型，分别是：

*   布尔值，如：true()返回ture(真)，false()返回false(假)，not()对布尔值取反。

*   数字，如：number()把任意类型转化数字，celing()返回大于或等于参数的最小整数。

*   节点集，如：position()返回当有节点在上下节点列表中的位置，count()可统计节点数。

*   字符串，如：string()转化任意类型为字符串，string-length()返回字符串长度。

## 6.4\. XLink

XLink是一种基于属性的语法，用来在XML文档中添加链接。XLink链接可以是单向的，如HTML中的A元素，它也可以是双向的，在两个方向上链接两篇文档，因此能够从A到B或从B到A。每个XLink元素必须具有一个xlink:type属性，指出连接类型。属性xlink:href指向所链接的资源URI。下面是一个简单链接的示例：

```
<test xmlns:xlink = "http://www.w3.org/1999/xlink"
      xlink:type = "simple"
      xlink:href = "http://www.ringkee.com/xml.html">
<author>Jims</author>
<date>2005/02/18</date>
</test>

```

xlink:type属性类型共有六种，分别是：simple，extended，locator，arc，title，resource。

xlink:show属性可告诉浏览器或应用程序在激活链接时应该做什么，它有五种可能的动作，分别是：

*   new，在新窗口中显示链接内容。

*   replace，在当前窗口显示链接内容。

*   embed，在当前链接元素的位置嵌入内容。

*   other，动作不确定，由应用程序指定。

*   none，无动作。

xlink:actuate属性可告诉浏览器何时显示链接，它有四种可能值：

*   onLoad，一旦发现链接，马上显示。

*   onRequest，当用户提出请求时才显示。

*   other，由文档中的其它标记，而不是xlink，来决定何时显示。

*   none，不指定。

一个和HTML中的A元素作用一样的示例：

```
<test xmlns:xlink = "http://www.w3.org/1999/xlink"
      xlink:type = "simple"
      xlink:href = "http://www.ringkee.com/xml.html"
      xlink:actuate = "onRequest" 
      xlink:show = "replace" >
<author>Jims</author>
<date>2005/02/18</date>
</test>

```

一个在页面嵌入图像的示例：

```
<image xlink:type = "simple"
       xlink:actuate = "onLoad"
       xlink:show = "embed"
       xlink:href="http://www.ringkee.com/flower.png"
 width = "320" height = "240" />

```

xlink:actuate和xlink:show是可选的。

xlink:title和xlink:role属性可指定资源之间的描述，xlink:title包含少量描述远程资源的文本，xlink:role包含URI，指向资源的较长描述。

## Chapter 7\. 分析XML


分析XML文档可通过程序来做，分析器有两大类，一种是事件驱动的，一种是基于树模型的。

*   使用事件驱动的分析器时，每遇到一个元素就会触发一个事件，由事件处理器进行处理。事件分析器按顺序读取XML文档，而不把整个文档读入内存，所以处理速度很快。但缺点是由于要从头到尾读取XML文档，因此无法在XML文档中移动位置。事件驱动分析器适合处理其它地方使用的XML数据，如转换成HTML文档或从文件中读取数据并插入数据库中。它的优点有：

    *   文件搜索，从XML文档中搜索需要的标志或数据；

    *   格式转换，如转换成HTML。任何需将原始XML转换成另一种格式的工作都最好使用事件驱动分析器来完成，因为它可动态将信息转换成新格式。

    *   少量修改，你可用事件驱动分析器读取和重新生成XML。在分析过程中，可以改变少量的单语、字符数据内容或重新构造XML。事件驱动分析器特别适合整理和重新格式化XML文档。

    *   简单验证，由于整个文档不在内存中，所以无法进行完整验证，但可检查拼写错误和一般良构XML文档之类的简单问题；

    *   建立内部结构，可以使用事件驱动分析器建立XML文档的复杂内部表示，如基于树的接口使用的树式结构。

    事件驱动分析器不能在XML文档间交叉引用文档内容，但它使用简单，速度快。

*   基于树的分析器把整个XML文档读入内存，并生成树状结构。分析器可随机访问树中的任意节点，并能修改树结构和内容。

## 7.1\. 分析器工具

现有的分析器种类有上百种，但常用的是两个标准的工具库，一个是XML简单API(SAX，Simple API for XML)和文档对象模型(DOC，Document Object Model)。SAX是事件驱动分析器的标准，而DOM是基于树的分析器标准。另外，Expat虽然不是标准，但它是脚本语言中处理XML时最常用的分析器。Expat由James Clark编写，是事件驱动分析器。

## 7.2\. Unicode

计算机并不能正真理解文本内容，它无法识别诸如a,b,c这类的字母，更不用说中文了。计算机所能理解的只有数字，如60，80等。字符集(character set)规定了字母到数字的映射关系，如65代表大写字母A。65称为码点(code point)，字符编码(character encoding)决定码点如何用字节表示。是用多了节还是单字节，高字节位表示什么，低字节位表示什么。

不同国家使用不同的语言，不同程序使用不同的编码规范，在进行世界范围内的数据交换就要统一表示数据的字符编码规范。传统的ASCII字符集只定义了127个字符，其中前31个是控制符。127位之后的字符随平台不同而不同。大多数平台只能表示前127位，单字节(8位)，使得字符集中最多只能提供256个字符。这些标准字符称为罗马或拉丁字符集，用ASCII来表示中文、日文是远远不够的。

为了解决字符集问题，出现了Unicode字符集。它可用多字节格式编码字符，目前标准允许2字节字符，支持65536个不同字符。标准的Unicode字符集为Latin-1(或ISO-8859-1)。有关Unicode的介绍可访问Unicode的官方网站：<http://www.unicode.org>。

Unicode字符集为字符分配码点，即编号。这些编号可以用多种模式编码，如UCS-2、UCS-4、UTF-8、UTF-16。

*   UCS-2，也叫ISO-10646-UCS-2。每个字符用一个0~65535之间的两个字节的无符号整数表示。如A的Unicode码点为65，用两个字节00和41(十六进制)表示。B的Unicode码点为66，用两个字节00和42表示。UCS-2有两种形式：高字节(#x0041)在前和低字节(#x4100)在前。为区发高低位不同表示形式，采用UCS-2编码文档通常以Unicode字符#xFEFF(零宽度无间断空格)开头，一般称为字节顺序标记(byte order mark)。这个字符是不可见的。如果两个字节交换位置，得到的字符#xFFFE实际是不存在的。因此中通过查看UCS-2文档的前两个字符是#xFEFF还是#xFFFE，就可确定该文档是否是高字节在前。UCS-2的缺点：如果文本字符主要是拉丁文，由于采用两个字节，字符集编码是单字节字符编码的两倍；UCS-2不能与ASCII向前或向后兼容，用于单字节字符集的工具常常不适用于处理UCS-2编码文件。

*   UTF-8是一种可这长度的Unicode编码。0~127为ASCII码字符集，与ASCII编码完全兼容，每个字符采用一个字节编码。UTF-8用两个字节表示128~2047，该范围覆盖了最常见的非表意字母。其余的字符，主要来自汉语、日语和韩语，每个都用3个字节表示。如果Unicode的码点超过65535个字符，那么这些字符就会用4个字节编码。对于以拉丁文为主的文件，使用UTF-8比UCS-2可减少一半的文件大小。对于汉语、日语和韩语的文件，其大小会增加百分之五十。对于其它语言，文件大小相差不大。UTF-8是最常用的Unicode编码方式。

在Unicode流行以前，出现了一系列处理特定语言的单字节字符集，ISO将14种这样的字符集标准化成ISO 8859标准，分别是ISO-8859-1~14。ISO-8859-15是ISO-8859-1的修订版本。这些字符集统称ISO字符集。

Cp1252是依赖于Windows平台的一种编码，是Windows的缺省字符集。该种编码不支持跨平台特性，尽量不要使用。

MacRoman是Mac OS使用的一种非标准、单字节编码。在非Mac平台下使用也会有问题，尽量不要使用。

在XML文档中，如果需输入编辑器不支持的字符，我们可用字符引用的方式，以十进制或十六进制给出它所代表的Unicode字符编号，如&#1114;(十进制)或者&#x45A(十六进制)。字符引用可用于元素内容、属性和注释，不能用于元素名和属性名、处理指令或XML关键字。如果有一些字符需经常使用，则我们可为这些字符定义实体，这样，在文档中就可方便地引用该实体了。专门定义字符实体的DTD我们可独立出来，形成以.ent为后缀的外部DTD。在需要时使用外部参数实体引用将这些定义引入文档的DTD中。

XHTML 1.0 DTD包含有三个有用的字符引用实体可在文档中使用。

*   Latin-1字符，http://www.w3.org/TR/xhtml1/DTD/xhtml-lat1.ent

    ISO-8859-1中自160以上的非ASCII码字符。

*   特殊字符，http://www.w3.org/TR/xhtml/DTD/xhtml-special.ent

    ISO-8859-2中不在Latin-1中的字母。

*   标点符号，http://www.w3.org/TR/xhtml-symbol.ent

    希腊字母表(不包含带重音的字符)和各种标点符号、数学运算符及其他数学中常用的符号。

在XML文档中可以使用xml:lang属性规定元素内容采用的语言。这样就可在一篇文档中同时使用多种语言，这是XML跨平台和跨语言的重要特性之一。如：xml:lang="CN-CHN"。语言代码是一个两个字母的语言代码，语言代码后还可跟一个子代码，语言代码可在这里找到[http://ftp.ics.uci.edu/pub/ietf/http/related/iso3166.txt](http://ftp.ics.uci.edu/pub/ietf/http/related/iso3166.txt)。下面是xml:lang属性声明的示例：

```
<!ELEMENT test (#PCDATA)>
<!ATTLIST test xml:lang NMTOKEN #IMPLIED>

```

由于所有语言代码都是有效的XML名称标记，所以使用NMTOKEN类型。

## Appendix A. 附录


## A.1\. 标记语言的历史

*   1974年，IBM的Charles F.Goldfarb、Ed Mosher和Ray Lorie发明了一种最终发展成为标准的通用标记语言(SGML，Standardized General Markup Language)。1986年，SGML被ISO采用为8879号标准。

*   1991年，Tim Berners-Lee利用SGML提供的基本机制定义了超文本标记语言(HTML，Hypertext Markup Language)，把Internet带进了一个多姿多彩的世界。HTML是SGML最成功的一种应用。

*   1998年2月10日，W3C的XML 1.0标准正式发布，为异构平台的数据交换提供了一个可行的标准。

## A.2\. XML相关技术名词解释

*   XLink，一种基于属性的用于XML和非XML文档之间超链接的语法，可以提供与HTML相似的简单、单向的链接，多文档之间的多向链接，以及没有写入权限的文档间的链接。

*   XSLT(XSL Transformation,XSL转换)，一种XML文档，用于描述具有相同或不同XML词汇表的两个文档之间的转换。

*   XSL-FO(XSL Formatting Object,XSL格式化对象)，一种用于描述打印和网页布局的XML应用。

*   Dsssl(Document Style Sheet and Semantics Language,文档样式表和语义语言)，用于描述XML打印和在Web上的样式，源自SGML。

*   XPointer，标识XML文档中由URI指定的特殊部分，通常与XLink结合使用。

*   XPath，用于标识XML文档中的路径。

*   Namespace，区分来自不同的XML语汇表但名称相同的元素和属性的一种方式。

*   SAX，Simple API for XML，一种事件驱动的XML文档处理器。

*   DOM，Document Object Model，一种面向树的API，它把XML文档解释成具有多属性和嵌套的对象树。

## A.3\. XML应用

XML可自定义标签，为了增强互操作，个人或组织可约定只使用某种标签。这些标签集被称为XML应用。XML应用不是使用XML的软件应用程序，如IE或Word，而是XML在矢量图形或数学公式这些特殊领域的一种应用。

*   SVG，可缩放矢量图形(Scalable Vector Graphic)，是W3C推荐的XML中矢量图的编码标准。

*   MathML，数学标记语言(Mathematical Markup Language)，用于表示数据公式。

*   CML，化学标记语言(Chemical Markup Language)，描述化学、物理学、分子生物学和其它分子科学。

*   RDF，资源描述框架(Resource Description Framework)，用于描述资源，特别是图书馆分类卡上的元数据。

*   CDF，通道定义格式(Channel Definition Format)，微软公司定义的一种非标准XML应用，用来向IE发布可离线浏览的网页。