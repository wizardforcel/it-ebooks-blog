title: PHP Security Cheatsheet 中文版
date: 2016-02-17 22:39:32
tags:
  - 渗透
---

# 介绍

这篇博客是翻译自OWSAP的<a href ="https://www.owasp.org/index.php/PHP_Security_Cheat_Sheet">PHP Security Cheat Sheet</a>，你可以查看原文。

本文章的目的是提供基本的PHP安全建议，主要针对开发者和系统管理员。需要注意的是这里提到的安全建议可能并不足已支撑安全的网络应用，而只是一个组成部分。<!--more-->

## PHP介绍

根据W3 Techs的统计，PHP是最流行的Server端编程语言，大约81.8%的Web Server用PHP部署(任何语言都要为自己吹一把的)。

与其它语言不同，PHP即是一门语言，也是一个web框架，在PHP语言中内嵌了典型的web框架的特性。跟其它语言一样，PHP背后也有庞大的社区软件库，贡献了PHP安全和其它各个方面的特性。所有的这三个方面（语言、框架和开源库）都是在构建安全的web应用中需要考虑的因素。

PHP一直在发展中，而不是固定的设计，因此你很可能写出了不安全的PHP程序。为了让应用更安全，你需要了解所有的陷阱。

### 语言相关

#### 弱类型

PHP是弱类型的，意味着不正确的数据类型会被自动转换。这个特性经常会隐藏开发中的错误信息或者不规范数据的注入，导致系统风险性增加。(例子在下面的输入处理部分)。

尽量使用非类型转换的函数和操作符(例如用===替换==)。但并非所有的操作符都有严格类型检查的版本（例如<=和>=），另外很多内置的函数(例如in_array)默认进行类型转换，给编写安全的代码带来了挑战。

#### 异常和错误处理

几乎所有的PHP内置函数很多PHP库，不支持异常，而是用其它的报警机制(例如notice)，允许出错的代码继续运行。这也会隐藏很多bug。很多其它的语言、大部分高级语言，相对于PHP，开发者代码错误或者开发者未处理的运行时错误，都会导致程序停止执行，从而保护程序。

考虑下面的程序，程序的目的是检查一个username是不是在数据库的黑名单中，以限制访问。

    $db_link = mysqli_connect('localhost', 'dbuser', 'dbpassword', 'dbname');

    function can_access_feature($current_user) {
       global $db_link;
       $username = mysqli_real_escape_string($db_link, $current_user->username);
       $res = mysqli_query($db_link, "SELECT COUNT(id) FROM blacklisted_users WHERE username = '$username';");
       $row = mysqli_fetch_array($res);
       if ((int)$row[0] > 0) {
           return false;
       } else {
           return true;
       }
    }

    if (!can_access_feature($current_user)) {
       exit();
    }
    // Code for feature here

上面的代码可能产生各种各样的运行时错误，例如由于用户名和密码错误或者数据库server宕机可能导致的数据库连接失败、或者连接可能被server断开。在上述情况下，`mysqli`函数会抛出notice或者warnings，但不会抛出异常或者fatal error，代码会继续执行。变量`$row`会成为`NULL`，基于若类型转换`(int)$row[0]`会成为0，最终`can_access_feature`会返回`true`，用户会获得访问权限，不管用户是否在黑名单中。

如果使用native的数据库API，需要在各个地方添加错误检查。然而由于这需要额外的工作、又如此容易被忽略，所以它是'默认不安全的'。这就是为什么访问数据库通常要采用<a href="https://secure.php.net/manual/en/intro.pdo.php">PHP Data Objects (PDO)</a>和其错误处理<a href="https://secure.php.net/manual/en/pdo.error-handling.php"> ERRMODE_WARNING or ERRMODE_EXCEPTION flags </a>，除非有特殊的原因，不会使用native API和错误检查工作。

使用<a href="http://www.php.net/manual/en/function.error-reporting.php">error_reporting</a>函数将错误优先级设置越高越好，修复warnings，让系统越鲁棒越好。

#### php.ini

PHP代码的行为经常强依赖于很多配置文件的设置，例如基本的错误处理配置等。这使得很难写出在所有场景下正常运行的代码。不同的库依赖不同的设置，使得很难使用第三方的代码，这在后面的'配置'部分也会提到。

#### 无用的buildin函数

PHP提供了大量的内嵌函数，例如`addslashes`、`mysql_escape_string`、`mysql_real_escape_string`等。这些试图提供安全的特性的函数经常是有bug的，并不能解决安全性的问题。许多内嵌的函数已经被弃用或者迁移，但由于向下兼容的规则，这些函数会保留很长时间。

PHP会提供`array`的数据结构，在各种代码中随意使用，但由于混合了数组和字典，经常导致混淆。这种混淆经常导致甚至是有经验的程序员引入重大的安全隐患，例如<a href="https://www.drupal.org/SA-CORE-2014-005">Drupal SA-CORE-2014-005</a> 和 <a href="http://cgit.drupalcode.org/drupal/commit/?id=26a7752c34321fd9cb889308f507ca6bdb777f08">the patch</a>。

### 框架相关

#### URL路由

PHP默认的路由机制是使用文件目录中`.php`的后缀，这带来很多风险

* 文件上传没有进行文件名过滤导致的远程执行风险（换句话说，服务化器执行了外部的代码）。在接收远程文件上传时，请确保文件名和内容经过过滤。

* 源代码和配置文件存储在公共可访问的目录中，可以被下载。误配置或者缺少配置可能会导致源代码或者包含密码等信息的配置文件被攻击者随意下载（换句话说，服务器暴露了私密的信息）。你可以使用`.htaccess`来限制访问，但这并不是最完美的方案，因为它是'默认不安全的'，也没有可替代的方案。

* URL路由机制只是模块系统。这意味着攻击者可能可以使用非法的文件名作为进入点，带来认证机制可能被完全绕过的风险。这在PHP中极其容易，因为有全局可访问的请求信息（例如`$_GET`），所以文件层面的代码即可操作整个请求、而不是在固定的函数中进行请求处理。

* URL路由机制的缺失导致开发者开发各自的路由方法。这往往是不安全的，容易导致请求处理函数未进行合适的请求限制。

#### 输入处理

PHP将HTTP的输入转换成了数组、而不是简单字符串。这会导致对于数据的混淆，容易导致安全风险。例如下面的代码是一个密码重置的一次性机制判断

    $supplied_nonce = $_GET['nonce'];
    $correct_nonce = get_correct_value_somehow();

    if (strcmp($supplied_nonce, $correct_nonce) == 0) {
        // Go ahead and reset the password
    } else {
       echo 'Sorry, incorrect link';
    }

如果攻击者使用如下的查询字符串

     http://example.com/?nonce[]=a

会导致`$supplied_nonce`成为数组、`strcmp()`函数会返回NULL（连异常都不会抛出），由于若类型转换和没有使用`===`操作符，校验成功，攻击者可以在不提供原密码的情况下进行密码修改。

相似的case和`array`结构导致的混淆事故，可以在<a href="https://www.drupal.org/SA-CORE-2014-005"> Drupal SA-CORE-2014-005 </a>，参见<a href ="http://www.zoubi.me/blog/drupageddon-sa-core-2014-005-drupal-7-sql-injection-exploit-demo"> example exploit</a>。

#### 模板语言

PHP本质上是一门模板语言，但它默认并没有提供HTML转义，在web应用中带来极大使用困难，可以参见下面的XSS部分。

#### 其它不足

另外有很多web框架应该支持的重要特性，例如默认开启CSRF的保护机制。因为PHP只是提供了一个基本的、功能足够的特性来创建web站点，很多不了解CSRF保护机制的人就仅使用了PHP基本的功能。

### 第三方PHP代码

由于上述原因，PHP项目和开源库经常是不安全的，特别是没有使用恰当的框架时。不要轻易相信你在网络上发现的PHP代码，看起来没问题的代码可能隐藏了很多的安全隐患。

书写不规范的代码会导致warning信息被隐藏，无法及时暴露问题。通常人们会关闭notice信息，但绝不要这么做，这带来更严重的后果。

## 定期升级PHP

要定期升级生产环境的PHP版本。因为每天都有新的PHP漏洞被暴露出来，攻击者经常会用这些漏洞攻击网络上任意的服务器。

# 配置

配置文件对PHP的行为影响极大，包括`php.ini`文件、Apache配置命令和<a href="http://www.php.net/manual/en/configuration.php">运行时机制</a>。

有很多不安全的设置，下面是一部分。

## setHandler

setHandler命令可以配置PHP代码，在很多场景中，它被用`addHandler`指令错误的替代，`addHanler`可以正常工作，但也会使很多其它文件像PHP一样执行，例如一个文件名为`foo.php.ini`的文件也会被当做php来执行。这会带来严重的远程执行的风险，如果该文件是被恶意上传。

# 不可信的数据

All input is evil，所有用户的输入都不值得信任。输入必须被用合适的方式校验、或者过滤。

`$_SERVER`、`$_GET`、`$_POST`、`$_REQUEST`、`$_FILES`和`$_COOKIE`这些超全局变量也不应该被信任。尽管`$_REQUEST`中并非所有的数据都可以被用户伪造，但还是有相当部分的可能被伪造，特别是处理HTTP header的那部分(以HTTP_开头的)。

## 文件上传
来自用户上传的文件会带来巨大的安全隐患，特别是该文件可以被其他用户下载时。例如：

* 任何HTML文件可能会导致xss攻击。
* 任何PHP文件可能会带来远程代码执行的风险。

由于PHP对于代码执行的检查并不严格（带上合适的扩展名即可），对于使用PHP搭建的web服务器一定要确保上传进行合适的文件名过滤后再进行保存。

## 处理$_FILES数组的常见错误

如下的代码片段、或者类似功能的代码是很常见的：

    if ($_FILES['some_name']['type'] == 'image/jpeg') {  
       //Proceed to accept the file as a valid image
    }
然而`type`并不是启发式的去校验的，而仅仅是接收了HTTP请求中的数据，这很容易被客户端伪造。一个更好的去校验文件类型的方法是使用`finfo`库，尽管这种方法也并不完美。

    $finfo = new finfo(FILEINFO_MIME_TYPE);
    $fileContents = file_get_contents($_FILES['some_name']['tmp_name']);
    $mimeType = $finfo->buffer($fileContents);
    
尽管这会占用服务器的计算资源，但`$mimeType`是更好的判断文件类型的方式，会阻止一些用户上传危险的文件，并伪装成image等形式，来造成攻击行为。

## 使用$_REQUEST

强烈不建议使用`$_REQUEST`。这个超全局变量不仅包含了GET和POST，还包含了用户请求的cookies等信息，所有的这些数据被组合在了一个数组里，导致很难检测数据的来源，很容易导致混淆、易于犯错、容易导致安全风险。

# 数据库
单个mysql注入就会直接操纵整个网站，所以每个黑客都会首先尝试mysql注入，防止mysql注入也是PHP安全站点中最应该考虑的，遵循如下规则：

## 不要在SQL中连接或者插入数据

### 不要直接使用用户数据的string构造SQL
     
    $sql = "SELECT * FROM users WHERE username = '" . $username . "';";

或者使用如下SQL：

     $sql = "SELECT * FROM users WHERE username = '$username';";

如果`$username`来自不可信任的来源，它可以包含类似于`'`这样的字符，从而可以执行其它命令，甚至删除数据库命令。使用prepare语句和绑定参数是更好的解决方案。PHP的<a href="http://php.net/mysqli">mysqli</a>和<a href="https://secure.php.net/pdo">PDO</a>提供了相关的特性。

### 转义是不安全的

`mysql_real_escape_string `这种转义是不安全的。不要依赖这个函数来防止SQL注入。

当你使用`mysql_real_escape_string `来校验每个变量然后放入查询语句中，你难保一次都不会忘记，只要忘记一次就会是灾难。你无法保证一次都不会忘记。而且，你要保证你使用了引号，如果输入是数字的话，这会很不自然，容易忘记。使用prepare语句或者相似的API，它们会帮你做正确的转义和过滤。（大部分ORM框架也会做这种转义、帮你创建SQL）
### 使用prepare语句
prepare语句非常安全。在prepare语句中，SQL命令和数据是分开的，每个用户输入都会认为是数据，进行处理。

相关的内容可以参考PHP的<a href="https://secure.php.net/manual/en/mysqli.quickstart.prepared-statements.php">mysqli prepare statement</a>和<a href="https://secure.php.net/manual/en/pdo.prepare.php">PDO prepare statement</a>

#### prepare语句失效的场景

进行动态的查询、不支持prepare的变量，或者数据库引擎不支持prepare语句会是问题。例如，PDO MySQL不支持`？`作为限制符。而且限制符不能作为表名或者列名用于`select`语句中。在此类的场景中，尽量使用框架提供的query builder，如果框架没有功能，使用Composer和Packagist安装几个第三方包，不要自己做。

### ORM
ORM(Object Relational Mappers)，即对象关系映射，是非常好的安全手段。如果你使用ORM（例如<a href="http://www.doctrine-project.org/">Doctrine</a>），仍然可能会遭受SQL攻击。尽管ORM中注入攻击比较困难，不过串联ORM查询和串联SQL查询具有相同的问题。ORM也支持prepare语句。

### 编码事宜
#### 尽量使用UTF-8编码
许多新型攻击模式依赖于编码。使用UTF-8作为数据库和应用的字符集，除非你有对其它字符集的强依赖。

     $DB = new mysqli($Host, $Username, $Password, $DatabaseName);
     if (mysqli_connect_errno())
        trigger_error("Unable to connect to MySQLi database.");
     $DB->set_charset('UTF-8');

# 其它注入
除了SQL以外，还有PHP中别的注入的可能性
## 脚本注入
一些PHP函数例如：

* shell_exc
* exec
* passthru
* system
* 反引号(`)

上面的函数或者命令将字符串作为脚本和命令名。基于配置，脚本命令泄露可以导致应用设置和配置文件泄露，这是非常严重的风险，会导致整个网站被控制。

不要向这些函数传入未经过滤的输入，除非你确认它们一定是安全的。转义和其他对策是无效的，攻击者会尝试各种测试向量，不要相信新手程序员。

## 代码注入
所有的解释型语言，例如PHP，具有将字符串转换成命令并执行的能力。PHP中这个函数是`eval()`，使用`eval()`是不安全的，并不建议使用，除非你确认除了`eval`以外没有别的选择。`eval()`性能比较差。

不要轻易在`preg_replace()`中输入未经过滤的输入，因为payload会被<a href ="https://stackoverflow.com/questions/4289923/in-which-languages-is-it-a-security-hole-to-use-user-supplied-regular-expression/4292439#4292439">`eval()'ed`</a>

    preg_replace("/.*/e","system('echo /etc/passwd')");

Reflection也有代码注入的风险。这属于高级的话题，请参考相关文档。

## 其它注入
LDAP、XPath和其他一些使用数组作为输入的第三方库，也容易被注入攻击。时刻记住有些数组不仅仅是数据，而是命令，所以在输入第三方库之前要进行检查。

# XSS
提到XSS时，主要指两个场景，分别可以通过如下方式缓解：

## 没有tags
大部分时候，用户不会提供未经转义的HTML标签。例如在一个cell或者textbox中输出用户数据。

如果需要使用标准的PHP来输出(echo)模板，你可以通过对数据进行`htmlspecialchars `（或者下面的函数，对htmlspecialchars的封装）缓解XSS。尽管这并不推荐，因为需要开发者在每个使用场景都要调用。如果开发者忘记了，就存在XSS的风险。我们认为默认不安全的方法就是不安全的。

除此之外，你可以使用默认进行HTML转义的模板引擎。所有需要输出到模板的HTML都需要经过HTML模板。

如果你的项目不能转换到一个安全的模板引擎，你可以使用下面的函数来过滤数据。

需要注意的是下面的函数对于`style`、`script`、`image`、`src`、`a`等等不安全的元素是无效的。所有输出到浏览器的数据，都要经过下面函数的过滤。

    //xss mitigation functions
    function xssafe($data,$encoding='UTF-8')
    {
        return htmlspecialchars($data,ENT_QUOTES |ENT_HTML401,$encoding);
    }
    
    function xecho($data)
    {
        echo xssafe($data);
    }
    
    //usage example
    <input type='text' name='test' value='<?php xecho ("' onclick='alert(1)");?>' />
    
## 不可信的tags
当你需要用户在你输出时提供HTML tags时（例如富文本博客评论、博客等等），但不是很信任使用者时，你需要使用安全编码库。这很困难，迁移过程也很慢，所以大量的网络应用有XSS注入攻击的风险。OWASP ESAPI对于不同类型数据的编码具有大量的编解码器，也有PHP的OWASP AntiSammy和HTMLPurifier。这需要一定的配置和学习的成本，但对于一个好的网络应用，是必不可少的。
## 模板引擎
有一些模板引擎可以帮助开发者或者设计者输出数据，防止XSS攻击。尽管模板引擎的初衷并不是安全、而是增加设计的体验，但大部分引擎输出时自动转义了变量，或者要求开发者显式的指定不需要转义的变量。这使得输出数据默认是安全的。类似的引擎包括twig、Smarty、Haanga和Rain TPL。

模板引擎是很好的安全实践，因为它提供了开发者容易忘记的特性，默认的进行XSS保护的转义。对于安全很看重的系统应该使用默认安全的引擎。

## 其它建议

* 在web应用中，没有可信任的区域。很多开发者会留着网站的admin部分不进行XSS过滤，事实上大部分攻击者都会对admin的cookie的XSS感兴趣。任何需要输出的变量都要用上面提到的方案进行处理。删除每个`echo`，`print`和`printf`，替换成安全的模板引擎。
* HTTP-Only cookies是很好的实践，很快每个浏览器都会支持。建议现在就开始使用。
* 上面提供的函数只支持HTML语法。如果你put your Element Attributes without quotation，你就死定了。
* <a href="https://www.owasp.org/index.php/Reflected_XSS">反射型XSS</a>和普通的XSS一样危险，可能出现在应用中任何部分。找到并解决它们。
* 并不是所有的PHP都安装了mhash扩展，如果要做hash，需要先检查一下。否则你不能用SHA-256
* 并不是所有的PHP都安装了mcrypt扩展，如果没安装，你没法做AES，使用前请先进行检查。

# CSRF
CSRF是修复理论上比较简单，但正确的修复确并不容易。首先提几个关于CSRF的tips：

* 每个请求都是有用的，都要做CSRF的修复。不仅仅包括修改的请求、还包括执行时间较长的读请求。
* CSRF容易发生在GET，也不要忽略POST。不要认为POST是安全的。

<a href="https://www.owasp.org/index.php/PHP_CSRF_Guard"> OWASP PHP CSRFGuard</a>这是一个代码片段，讲了如何进行CSRF的修复。仅仅复制粘贴是无效的，后面会发布一个拷贝粘贴版本。当前，使用上面代码结合如下建议：

* 对于重要的操作（修改密码、修改邮箱等）使用二次认证。
* 如果你不清楚你的请求是否能够免于CSRF，使用验证码（尽管验证码会让用户体验变差）
* 如果你的请求依赖于其它请求的部分内容（例如其它请求的cookies或者http header等部分），你也要对那些请求添加CSRF tokens。
* AJAX的请求需要重建CSRF tokens。使用上面提供的代码，不要只依赖javscript。
* CSRF会导致不便，结合你的设计和架构来使用。


# 认证和SESSION管理
PHP并没有提供一个真正可用的认证模块，你需要基于自身的框架自行实现。然而用这种方式，很多PHP框架在这方面并不完美，因为它们都是被开源社区的开发者而不是安全专家开发出来的。下面有几个建议：
## session管理
PHP默认的session机制是安全的，生成的PHPSessionID足够随机，但是存储未必是安全的：

* Session文件默认存储在temp目录(/tmp)，除非安装了suPHP，否则全局可访问。所有任何的LFI或者泄露都可以操作他们。
* 默认配置下Session是存储在文件中的，这对于高访问量的网站来说，太慢了。你可以存储在memory文件中。
* 你可以自己实现session机制，不再依赖PHP本身。可以将session存储在数据库，利用全部、部分或者直接不用php的session功能。

### session劫持预防
将session绑定到IP地址是好的习惯，这将很大程度上解决session劫持的场景。很多用户如果使用匿名工具（例如TOR），访问你的系统就可能出问题。

在session第一次创建时，存储客户端的IP地址，确保后面的请求都是相同来源。下面的代码返回了客户端的IP地址

    $IP = getenv ( "REMOTE_ADDR" );

在本地环境下，无法获得有效的IP地址，可能是`:::1`或者`:::127`，调整你的IP检查逻辑。另外要注意使用`HTTP_X_FORWARDED_FOR`变量的相似代码，因为该数据可以被用户随意修改，易于被欺骗。（<a href="http://www.thespanner.co.uk/2007/12/02/faking-the-unexpected/">这里</a>和<a href="http://security.stackexchange.com/a/34327/37">这里</a>）

### 将sessionid失效
当发生异常时，需要将session相关信息失效（删除cookie、删除session存储、删除其他痕迹），记录日志是很好的做法。很多系统还会通过邮件通知用户。

### session重置
当替换行为发生时，需要将session进行重置（例如当用户登录时）。

### 暴露的session
sessonid应该是机密的，应用不应该在任何场合将它暴露在外面。不要讲sessionid用在url中的一部分。当sessoin传递机密数据时，使用TLS，否则可能发生session劫持。

### Session Fixation
使用` session_regenerate_id()`来替换sessonid，当用户登录时（甚至每个请求以后）

### session过期

session应该在一定时间后失效，无论是活动还是静止状态。超时的操作包括在活动状态下重置sessionid和静止状态下删除session信息。

当退出登录发生时，完成所有的工作，包括清空相关的所有sesson记录。

#### 不活动状态的超时
如果当前的请求在上次请求以后已经经过了超过X秒，将其超时。这种清空需要在每次请求的时候进行判断，通常这个时间是30分钟，但也要根据具体应用来确定。

这种超时使得用户在一台公共的机器登录后忘记登出时获得一定的安全退出机制。也一定程度上预防了session劫持。

#### 正常的超时
如果当前的session已经经过了一定的时间，即使处于活跃状态，也将其超时。超时时间通常在一天和一周之间不等。实现该特性需要记录session的开始时间。

### Cookies
处理PHP的cookie有一些tricks：
#### 不要序列化
不要序列化cookie中的数据，因为很容易被操作篡改，增加攻击数据。
#### 恰当删除
要安全的删除cookie，使用如下的代码：

    setcookie ($name, "", 1);
    setcookie ($name, false);
    unset($_COOKIE[$name]);
    
第一行保证了浏览器过期了cookie数据，第二行是标准的删除cookie的方法，第三行从脚本中删除了cookie信息。很多手册中使用了`time()-3600`来做超时，但在浏览器时间不准确的情况下会无效。

可以使用`session_name()`来获得php默认session cookie名。
#### HTTP only
现代的浏览器支持HTTP-Only的cookies，这种cookie只可以通过HTTP(s)请求访问，不能被javascript访问，所以XSS的代码无法访问。这是很好的安全实践，但是并不能很令人满意，因为很多主流的浏览器发现了很多Http-Only的cookie暴露给JavaScript的bug。

PHP5.2+版本支持Http-Only cookie，你要手动设置http session cookie（不是使用session_start）

    #prototype
    bool setcookie ( string $name [, string $value [, int $expire = 0 [, string $path [, string $domain [, bool $secure = false [, bool $httponly = false ]]]]]] )
    
    #usage
    if (!setcookie("MySessionID", $secureRandomSessionID,$generalTimeout, $applicationRootURLwithoutHost, NULL, NULL,true))
        echo ("could not set HTTP-only cookie");
        
`$path`参数指定了cookie的有效范围，例如，如果你的网址是`example.com/some/folder`，`$path`应该是`/some/folder`，否则所有在`example.com`的应用都可以读取你的cookie。如果你使用全域名，可以忽略。域名参数强制了可访问域名，如果需要在多个域和IP访问，忽略该参数，否则老老实实设置。 如果安全参数设置，cookie可以通过HTTPs传递，例如：

    $r=setcookie("SECSESSID","1203j01j0s1209jw0s21jxd01h029y779g724jahsa9opk123973",time()+60*60*24*7 /*a week*/,"/","owasp.org",true,true);
    if (!$r) die("Could not set session cookie.");

#### 浏览器相关
很多浏览器都有cookies的问题，大部分可以通过设置超时时间为0来解决。

## 认证
### Remember me
很多浏览器在Remember me特性上存在风险。通常的方式是生成一次性的token，存储在用户cookie中，另外在服务端也要存储用于校验。这个token应该和用户名密码没有任何关系，一个长随机数是推荐的做法。

如果能够做到防止蛮力破解Remember me的token，增加锁定措施，是更好的做法。

* 不要在cookie中存储和用户名、密码相关的任何数据


# 配置和部署
配置请参见<a href="https://www.owasp.org/index.php/PHP_Configuration_Cheat_Sheet">PHP配置安全手册</a>

# 来源相关
本博客来源于对OWSAP的<a href ="https://www.owasp.org/index.php/PHP_Security_Cheat_Sheet">PHP Security Cheat Sheet</a>的翻译，翻译权所有，转载请注明。

其它安全相关

* <a href="https://www.owasp.org/index.php/OWASP_Cheat_Sheet_Series">OWASP Cheat Sheet Series</a>

