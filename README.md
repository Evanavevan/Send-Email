# email-sender

<!-- TOC -->

- [email-sender](#email-sender)
  - [1.介绍](#1%e4%bb%8b%e7%bb%8d)
  - [2.使用规范](#2%e4%bd%bf%e7%94%a8%e8%a7%84%e8%8c%83)
    - [构建docker镜像](#%e6%9e%84%e5%bb%badocker%e9%95%9c%e5%83%8f)
    - [运行镜像](#%e8%bf%90%e8%a1%8c%e9%95%9c%e5%83%8f)
  - [3.邮件格式](#3%e9%82%ae%e4%bb%b6%e6%a0%bc%e5%bc%8f)
    - [3.1mq发送带有模板的邮件](#31mq%e5%8f%91%e9%80%81%e5%b8%a6%e6%9c%89%e6%a8%a1%e6%9d%bf%e7%9a%84%e9%82%ae%e4%bb%b6)
    - [3.2mq发送自定义的邮件](#32mq%e5%8f%91%e9%80%81%e8%87%aa%e5%ae%9a%e4%b9%89%e7%9a%84%e9%82%ae%e4%bb%b6)
    - [3.3http指定发送邮件](#33http%e6%8c%87%e5%ae%9a%e5%8f%91%e9%80%81%e9%82%ae%e4%bb%b6)

<!-- /TOC -->

## 1.介绍

email-sender是一个邮件发送服务。可以从消息队列中读取需要发送的邮件内容，或者指定邮件的模板发送模板邮件。

## 2.使用规范

### 构建docker镜像

```shell
make email
```

### 运行镜像

```shell
docker run registry.jiangxingai.com:5000/base/email-sender:email-0.1.0
```

## 3.邮件格式

### 3.1mq发送带有模板的邮件

```json
// 邮件的格式由type和info组成，type类型根据需求不同，info也不同
{
    // 邮件的类型
    "type": "operator_inform_email",
    "info": {
        "desc": "向操作员发送通知邮件",
        // 发送邮件的目标地址列表
        "email_addresses": [],
        // 邮件模板中的填入的公司名
        "company": "",
    }
}
```

### 3.2mq发送自定义的邮件

```json
{
    "type": "normal_email",
    "info": {
        // 接收人邮件地址
        "email_addresses": ["xxx.com"],
        // 文本内容
        "content": "xxx",
        // 待发送的附件
        "files": [
            "file1": {
                "name": "xxx.zip",
                // bytes
                "body": "xxx",
            }
        ],
        // 待发送的附件，为图片格式
        "images": [
            "image1": {
                "name": "xxx.jpg",
                "body": "xxx",
            },
        ]
    }
}
```

### 3.3http指定发送邮件

[接口文档地址](http://zentao.jiangxingai.com/zentao/doc-view-124.html)
