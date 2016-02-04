# Hexo Theme: LandFarz

LandFarz（蓝得发紫）是一个在 Hexo 默认主题 [Light](https://github.com/hexojs/hexo-theme-light) 基础上二次开发的主题。

该主题的名称来源于哈尔滨工业大学（未来的宇宙工业大学）2009年操作系统期末试题。

## 安装

```
git clone https://github.com/wizardforcel/hexo-theme-landfarz.git themes/landfarz
```

修改 Hexo 的 `_config.yml` 中的 `theme` 为 `landfarz`。

## 升级

```
cd themes/lanfarz
git pull
```

## 配置

默认的`_config.yml`文件：

``` yaml
menu:
  Home: /
  Archives: /archives

sidebar: right

widgets:
- search
- category
- recent_posts
- tag
- tagcloud

# Duoshuo
duoshuo_shortname: fl-it-ebooks

fancybox: true

google_analytics:
rss: 
google_site_verification: 
baidu_site_verification: 
icon: 
```

+ `menu` - 导航栏的菜单，键值对形式，键为文字，值为连接
+ `sidebar` - 侧栏的位置
+ `widgets` - 侧栏上的小工具，一行一个
+ `duoshuo_shortname` - 站点的多说ID，可选
+ `fancybox` - 是否开启 jQuery 弹出层效果
+ `google_analytics` - Google Analytics ID ，可选
+ `rss` - rss 订阅链接，可选
+ `google_site_verification` - 用于谷歌站长工具验证所有权的ID，可选
+ `baidu_site_verification` - 用于百度站长工具验证所有权的ID，可选
+ `icon` - 用于在浏览器标签上显示的图标，可选，如果不指定则会加载默认图标

## 协议

[MIT License](LICENSE)