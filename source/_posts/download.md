---
title: 本站下载方式
date: 9999-12-2 23:59:59
categories:
  - 公告
---

![](../img/repo-deployed.svg) ![](../img/cdn-deployed.svg) ![](../img/northpole-preparing.svg) ![](../img/blockchain-preparing.svg)

### Docker

```
docker pull wizardforcel/it-ebooks-blog
docker run -tid -p <port>:80 wizardforcel/it-ebooks-blog
# 访问 http://localhost:{port} 查看文档
```

### PYPI

```
pip install it-ebooks-blog
it-ebooks-blog <port>
# 访问 http://localhost:{port} 查看文档
```

### NPM

```
npm install -g it-ebooks-blog
it-ebooks-blog <port>
# 访问 http://localhost:{port} 查看文档
```
