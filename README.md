# email-sender

## 1.介绍

email-sender是一个邮件发送服务。可以从消息队列中读取需要发送的邮件内容，或者指定邮件的模板发送模板邮件。

## 2.使用规范

### 运行项目

```shell
cd email-sender && python3 run.py
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

## 4.http指定发送邮件

### 4.1接口名称

邮件发送接口

### 4.2接口说明

请求地址：/api/v2/email/send

请求方式：POST
	
参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| subject | str | 是 | 无 | 邮件主题 |
| receivers | array | 是 | 无 | 邮件接收者列表 |
| content | str | 是 | 无 | 邮件内容 |

### 4.3接口示例

```json
{
	"subject": "备份gitlab",
	"receivers": ["xxxxxx@qq.com"],
	"content": "<h1>Heading</h1><p>contetn</p>"
}
```

## 5.账户审核接口

### 5.1接口名称

账户审核接口

### 5.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/account`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| is_success | bool | 是 | 无 | 账户是否审核成功 |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |
| reason | str | 取决于is_success，is_success为false为必填 | 无 | 审核失败时候的原因 |

### 5.3接口示例

```json
{
    "receivers": ["2712222225@qq.com"],
    "subject": "test email",
    "content": "<h1>Heading</h1><p>contetn</p>"
}
```

## 6.应用审核接口

### 6.1接口名称

应用审核接口

### 6.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/application`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| is_success | bool | 是 | 无 | 应用是否审核成功 |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |
| application_name | str | 是 | 无 | 应用名称 |
| application_version | str | 是 | 无 | 应用版本 |
| reason | str | 取决于is_success，is_success为false为必填 | 无 | 审核失败时候的原因 |

### 6.3接口示例

成功：

```json
{
    "is_success": false,
    "receivers": ["2712222225@qq.com"],
    "verify_link": "http://www.baidu.com",
    "application_name": "cube",
    "application_version": "1.0.0",
    "reason": "您的信用极差"
}
```

## 7.注册账户验证接口

### 7.1接口名称

注册账户验证接口

### 7.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/register`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |

### 7.3接口示例

成功：

```json
{
    "receivers": ["222222245@qq.com"],
    "verify_link": "http://www.baidu.com"
}
```

## 8.重置密码通知接口

### 8.1接口名称

重置密码通知接口

### 8.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/pwd`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |
| reset_time | str | 是 | 无 | 重置密码时间 |
| email_address | str | 是 | 无 | 修改密码的使用者的邮箱 |

### 8.3接口示例

成功：

```json
{
    "reset_time": "2019/9/15 18:00:00",
    "receivers": ["2222281245@qq.com"],
    "email_address": "evan@qq.com",
    "verify_link": "http://www.baidu.com"
}
```

## 9.子账户验证通知接口

### 9.1接口名称

子账户验证通知接口

### 9.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/subaccount`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |
| company | str | 是 | 无 | 通知的公司名字 |

### 9.3接口示例

```json
{
    "company": "XiHa",
    "receivers": ["2722221245@qq.com"],
    "verify_link": "http://www.baidu.com"
}
```

## 10.转交管理员通知接口

### 10.1接口名称

转交管理员通知接口

### 10.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/manager`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |
| company | str | 是 | 无 | 通知的公司名字 |

### 10.3接口示例

```json
{
    "company": "XiHa",
    "receivers": ["222222245@qq.com"],
    "verify_link": "http://www.baidu.com"
}
```

## 11.操作员账户验证接口

### 11.1接口名称

操作员账户验证

### 11.2接口说明

请求地址：`http://192.168.6.200:30995/api/v2/email/inform/operator`

请求方式：POST

参数说明：

| 名称 | 类型 | 是否必填 | 取值范围 | 备注 |
| ---- | --- | -------- | ------- | ---- |
| receivers | array | 是 | 无 | 收件人邮箱列表 |
| verify_link | str | 是 | 无 | 验证链接 |
| company | str | 是 | 无 | 通知的公司名字 |

### 11.3接口示例

```json
{
    "company": "XiHa",
    "receivers": ["222222245@qq.com"],
    "verify_link": "http://www.baidu.com"
}
```
