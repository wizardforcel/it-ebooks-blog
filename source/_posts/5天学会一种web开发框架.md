title: 5天学会一种 web 开发框架
date: 2016-1-1 21:16:15
tags:
  - 入门指南
---

作者：[lutaf](http://lutaf.com/)

来源：[5天学会一种 web 开发框架](http://lutaf.com/148.htm)

<!--more-->

web framework层出不穷，特别是ruby/python,各有10+个,php/java也是一大堆 根据我自己的经验写了一个to do list,按照这个清单，一条一条的学习，事半功倍，很快就能掌握 一共25条，即便很磨蹭，2小时也能搞定一条，25*2=50。只需要50小时就能掌握任意一种web框架

各类web框架大同小异:[现代web开发框架的6大元素](http://lutaf.com/50.htm)，把握主线，就不会迷路

建议把本文打印到一张A4纸，搞定一条打个勾

### web框架学习列表

*   如何定义 url route
*   如何组织 request handler 函数

    *   写一个最简单的request handler 函数
    *   如何从get/post请求中取出参数
    *   如何定义全局url 拦截函数
    *   如何获取/修改/存储 cookie,session数据
    *   如何修改/输出 http header 数据
*   如何部部署app 程序

    *   服务器部署可以参考[读python web 程序的9种部署方式](http://lutaf.com/141.htm)
    *   如何配置开发环境
    *   如何配置静态文件访问
*   如何访问数据库

    *   是否支持ORM

        *   支持orm

            *   如何维护表结构的变更
            *   如何定义/组织/初始化 数据表
            *   如何对接orm系统和现有的表结构
            *   掌握最基本的add/delete/按字段查询/count/slice/order by
            *   如何直接使用sql 访问数据库
        *   不支持orm (这样的web框架，不用也罢)

*   如何使用模板系统

    *   如何组织/访问 模板文件的目录结构
    *   如何在模板中嵌入代码
    *   模板是否支持继承结构
    *   模板之间如何include
    *   如何自定义模板函数
*   如何通过http get/post 获取远程数据

*   如何parse json
*   如何parse xml
*   如何输出为 json
*   如何处理状态码:404和50x
*   如何处理文件上传

### 可选的学习项目

*   发送email
*   log
*   图片处理

### 误区

*   表单验证辅助函数，**很多框架的表单验证部分实现的特别复杂**，初学者完全不需要，手写代码处理就够用
*   ORM中的hasone,manytomany,onetomany关系,概念很复杂，其实只是多写/少写一个查询字段的关系，学习成本太高，初学者完全不需要理会，直接跳过