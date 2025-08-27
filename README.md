
### 消息通知变量

| Name |  归属 |  属性  | 说明 |
| :-----: | :----: | :----: | --- |
|-|-|-|-|
| `HITOKOTO` | `false/true` | 非必须 | 是否启用一言（随机句子）默认不启用 |
| `CONSOLE` | `false/true` | 非必须 | 是否控制台输出 |
|-|-|-|-|
| `PUSH_KEY` | 微信server酱推送 | 非必须 | server酱的微信通知[官方文档](http://sc.ftqq.com/3.version)，已兼容 [Server酱·Turbo版](https://sct.ftqq.com/)   |
|    `BARK_PUSH`    | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | IOS用户下载BARK这个APP,填写内容是app提供的`设备码`，例如：https://api.day.app/123 ，那么此处的设备码就是`123`, 再不懂看 [这个图](img/bark.jpg)（注：支持自建填完整链接即可） |
| `BARK_ARCHIVE`  | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | 推送是否存档 |
| `BARK_GROUP` | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | bark 推送分组 |
| `BARK_SOUND` | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | bark推送声音设置，例如`choo`,具体值请在`bark`-`推送铃声`-`查看所有铃声` |
| `BARK_ICON` | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | bark 推送图标 |
| `BARK_LEVEL` | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | bark 推送时效性 |
| `BARK_URL` | [BARK推送](https://apps.apple.com/us/app/bark-customed-notifications/id1403753865) | 非必须 | bark 推送跳转URL |
| `DD_BOT_TOKEN` | 钉钉推送 | 非必须 | 钉钉推送(`DD_BOT_TOKEN`和`DD_BOT_SECRET`两者必需)[官方文档](https://developers.dingtalk.com/document/app/custom-robot-access) ,只需`https://oapi.dingtalk.com/robot/send?access_token=XXX` 等于`=`符号后面的XXX即可 |
| `DD_BOT_SECRET` | 钉钉推送 | 非必须 | (`DD_BOT_TOKEN`和`DD_BOT_SECRET`两者必需) ,密钥，机器人安全设置页面，加签一栏下面显示的SEC开头的`SECXXXXXXXXXX`等字符 , 注:钉钉机器人安全设置只需勾选`加签`即可，其他选项不要勾选, 再不懂看 [这个图](img/DD_bot.png) |
|  `FSKEY`  |  飞书推送  | 非必须 | 飞书机器人的 `FSKEY` |
|  `GOBOT_URL`  |  go-cqhttp推送  | 非必须 | (1)推送到个人QQ：`http://127.0.0.1/send_private_msg` <br>(2)推送到群：`http://127.0.0.1/send_group_msg` |
|  `GOBOT_QQ`  |  go-cqhttp推送  | 非必须 | go-cqhttp 的推送群或用户 GOBOT_URL 设置 <br> /send_private_msg 时填入 user_id=个人QQ <br> /send_group_msg 时填入 group_id=QQ群 |
|  `GOBOT_TOKEN`  |  go-cqhttp推送  | 非必须 | go-cqhttp 的 access_token |
|  `GOTIFY_URL`   |  gotify推送  | 非必须 | gotify地址,如https://push.example.de:8080 |
|  `GOTIFY_TOKEN` |  gotify推送  | 非必须 | gotify的消息应用token |
|  `GOTIFY_PRIORITY` |  gotify推送  | 非必须 | 推送消息优先级,默认为0 |
|  `IGOT_PUSH_KEY`  |  iGot推送  | 非必须 | iGot聚合推送，支持多方式推送，确保消息可达。 [参考文档](https://wahao.github.io/Bark-MP-helper) |
|  `DEER_KEY`  |  PushDeer推送  | 非必须 | PushDeer 的 PUSHDEER_KEY  [官方文档](https://www.pushdeer.com ) |
|  `CHAT_URL`  |  synology chat推送  | 非必须 | synology chat url  [官方文档](https://www.synology.com/en-global/dsm/feature/chat) |
|  `CHAT_TOKEN`  |  synology chat推送  | 非必须 | synology chat token  [官方文档](https://www.synology.com/en-global/dsm/feature/chat) |
| `PUSH_PLUS_TOKEN` | pushplus推送 | 非必须 | 微信扫码登录后一对一推送或一对多推送下面的token(您的Token) [官方网站](https://www.pushplus.plus/) |
| `PUSH_PLUS_USER`  |  pushplus推送  | 非必须 | 一对多推送的“群组编码”（一对多推送下面->您的群组(如无则新建)->群组编码）注:(1、需订阅者扫描二维码 2、如果您是创建群组所属人，也需点击“查看二维码”扫描绑定，否则不能接受群组消息推送)，只填`PUSH_PLUS_TOKEN`默认为一对一推送 |
|  `PUSH_PLUS_TEMPLATE`  |  pushplus推送  | 非必须 | pushplus 发送模板(默认html)，支持html,txt,json,markdown,cloudMonitor,jenkins,route,pay |
|  `PUSH_PLUS_CHANNEL`  |  pushplus推送  | 非必须 | pushplus 发送渠道(默认wechat)，支持wechat,webhook,cp,mail,sms |
|  `PUSH_PLUS_WEBHOOK`  |  pushplus推送  | 非必须 | pushplus webhook编码，可在pushplus公众号上扩展配置出更多渠道 |
|  `PUSH_PLUS_CALLBACKURL`  |  pushplus推送  | 非必须 | pushplus 发送结果回调地址，会把推送最终结果通知到这个地址上 |
|  `PUSH_PLUS_TO`  |  pushplus推送  | 非必须 | pushplus 好友令牌，微信公众号渠道填写好友令牌，企业微信渠道填写企业微信用户id |
|  `NTFY_URL`  |  ntfy推送  | 非必须 | ntfy地址,如https://ntfy.sh   [官方文档](https://docs.ntfy.sh/publish/) |
|  `NTFY_TOPIC`  |  ntfy推送  | 非必须 | ntfy的消息应用topic |
|  `NTFY_PRIORITY`  |  ntfy推送  | 非必须 | 推送消息优先级,默认为3 |
|  `NTFY_TOKEN`  |  ntfy推送  | 非必须 | 推送token,可选 |
|  `NTFY_USERNAME`  |  ntfy推送  | 非必须 | 推送用户名称,可选 |
|  `NTFY_PASSWORD`  |  ntfy推送  | 非必须 | 推送用户密码,可选 |
|  `NTFY_ACTIONS`  |  ntfy推送  | 非必须 | 推送用户动作,可选 |
|  `WXPUSHER_APP_TOKEN`  |  wxpusher推送  | 非必须 | wxpusher 的 appToken [官方文档](https://wxpusher.zjiecode.com/docs/)   [管理后台](https://wxpusher.zjiecode.com/admin/) |
|  `WXPUSHER_TOPIC_IDS`  |  wxpusher推送  | 非必须 | wxpusher 的 主题ID，多个用英文分号;分隔 topic_ids 与 uids 至少配置一个才行 |
|  `WXPUSHER_UIDS`  |  wxpusher推送  | 非必须 | wxpusher 的 用户ID，多个用英文分号;分隔 topic_ids 与 uids 至少配置一个才行 |
|  `WE_PLUS_BOT_TOKEN`  |  微加机器人推送  | 非必须 | 微加机器人的用户令牌 [官方网站](https://www.weplusbot.com/personal/feature) |
|  `WE_PLUS_BOT_RECEIVER` | 微加机器人推送  | 非必须 | 微加机器人的消息接收者 |
|  `WE_PLUS_BOT_VERSION` | 微加机器人推送  | 非必须 | 微加机器人的调用版本(默认pro) |
|  `QMSG_KEY`  |  [qmsg酱推送](https://qmsg.zendee.cn)  | 非必须 | qmsg 酱的 `QMSG_KEY` |
|  `QMSG_TYPE`  |  [qmsg酱推送](https://qmsg.zendee.cn)  | 非必须 | qmsg 酱的 `QMSG_TYPE` |
| `QYWX_KEY` | 企业微信机器人推送 | 非必须 | 密钥，企业微信推送 webhook 后面的 key [详见官方说明文档](https://work.weixin.qq.com/api/doc/90000/90136/91770) |
| `QYWX_AM` | 企业微信应用消息推送 | 非必须 | corpid,corpsecret,touser,agentid,素材库图片id [参考文档1](http://note.youdao.com/s/HMiudGkb) [参考文档2](http://note.youdao.com/noteshare?id=1a0c8aff284ad28cbd011b29b3ad0191)<br>素材库图片填0为图文消息, 填1为纯文本消息 |
| `QYWX_ORIGIN` | 企业微信机器人推送 | 非必须 | 企业微信推送代理地址 |
| `TG_BOT_TOKEN` | telegram推送  | 非必须 | tg推送(需设备可连接外网),`TG_BOT_TOKEN`和`TG_USER_ID`两者必需,填写自己申请[@BotFather](https://t.me/BotFather)的Token,如`10xxx4:AAFcqxxxxgER5uw` , [具体教程](./TG_PUSH.md) |
|   `TG_USER_ID`    | telegram推送 | 非必须 | tg推送(需设备可连接外网),`TG_BOT_TOKEN`和`TG_USER_ID`两者必需,填写[@getuseridbot](https://t.me/getuseridbot)中获取到的纯数字ID, [具体教程](./TG_PUSH.md) |
| `TG_API_HOST` | telegram推送 | 非必须 | tg 代理 api |
| `TG_PROXY_AUTH` | telegram推送 | 非必须 | tg 代理认证参数 |
| `TG_PROXY_HOST` | Telegram 代理的 IP | 非必须 | 代理类型为 http。例子：http代理 http://127.0.0.1:1080 则填写 127.0.0.1 |
| `TG_PROXY_PORT` | Telegram 代理的端口 | 非必须 | 例子：http代理 http://127.0.0.1:1080 则填写 1080  |
| `AIBOTK_KEY` | 智能微秘书推送 | 非必须 | 智能微秘书 个人中心的apikey [文档地址](http://wechat.aibotk.com/docs/about)  |
| `AIBOTK_TYPE` | 智能微秘书推送 | 非必须 | 智能微秘书  发送群名 或者好友昵称和type要对应好  |
| `SMTP_SERVER` | SMTP邮件推送 | 非必须 | SMTP 发送邮件服务器，形如 smtp.exmail.qq.com:465  |
| `SMTP_SSL` | SMTP邮件推送 | 非必须 | SMTP 发送邮件服务器是否使用 SSL(默认false)，填写 true 或 false  |
| `SMTP_EMAIL` | SMTP邮件推送 | 非必须 | SMTP 收发件邮箱，通知将会由自己发给自己  |
| `SMTP_PASSWORD` | SMTP邮件推送 | 非必须 | SMTP 登录密码，也可能为特殊口令，视具体邮件服务商说明而定  |
| `SMTP_NAME` | SMTP邮件推送 | 非必须 | SMTP 收发件人姓名，可随意填写  |
| `PUSHME_KEY` | PushMe推送 | 非必须 | PushMe 的 PUSHME_KEY [官方文档](https://push.i-i.me/) |
| `PUSHME_URL` | PushMe推送 | 非必须 | PushMe 的 PUSHME_URL [官方文档](https://push.i-i.me/) |
| `CHRONOCAT_QQ` | QQ机器人推送 | 非必须 | qq号 [官方文档](https://chronocat.vercel.app/) |
| `CHRONOCAT_TOKEN` | QQ机器人推送 | 非必须 | CHRONOCAT 的token [官方文档](https://chronocat.vercel.app/) |
| `CHRONOCAT_URL` | QQ机器人推送 | 非必须 | CHRONOCAT的url地址 |
| `WEBHOOK_URL` | 自定义消息推送 | 非必须 | 自定义通知 请求地址 |
| `WEBHOOK_BODY` | 自定义消息推送 | 非必须 | 自定义通知 请求体 |
| `WEBHOOK_HEADERS` | 自定义消息推送 | 非必须 | 自定义通知 请求头 |
| `WEBHOOK_METHOD` | 自定义消息推送 | 非必须 | 自定义通知 请求方法 |
| `WEBHOOK_CONTENT_TYPE` | 自定义消息推送 | 非必须 | 自定义通知 content-type |


#### actions工作流文件示例  
 - 固定时间点运行，启用企业微信应用消息推送  
```yaml
name: test

on:
  schedule:
    # 每隔6天运行一次，运行时间点自行设置(此处北京时间8:14运行)
    - cron: '14 0 */6 * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@main

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        pip install -r requirements.txt

    - name: Run sendNotify
      run: python3 test.py
      env:
        QYWX_AM: ${{ secrets.QYWX_AM }}  ## 填写对应的平台通知变量名[此处使用企业微信应用消息推送]，若需要多平台同时推送，请按此格式填写多个平台对应的变量名即可

```

- 随机时间点运行，启用pushplus推送  
```yaml
name: test

on:
  schedule:
    - cron: '14 0 */6 * *'
  workflow_dispatch:

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout
      uses: actions/checkout@main

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install Dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run sendNotify
      run: python3 test.py
      env:
        PUSH_PLUS_TOKEN: ${{ secrets.PUSH_PLUS_TOKEN }}  ## 填写对应的平台通知变量名[此处使用pushplus推送]，若需要多平台同时推送，请按此格式填写多个平台对应的变量名即可
    
    - name: Random Cron
      env:
        PAT: ${{ secrets.PAT }}
      if: always() && env.PAT
      uses: grbnb/random-workflow-cron@v2
      with:
        github_token: ${{ secrets.PAT }}  # 务必添加具有workflow权限的Personal Access Token密钥 没有请自行创建 https://github.com/settings/tokens/new
        keep_history: true
        time_zone: "UTC+8"
        interval_count: 1
        cron_dmw: "*/6 * *"

```

##### 提醒：  
以上`secrets.XXX`变量请务必前往仓库`settings` -> `Secrets and variables` -> `New repository secret`处添加对应的XXX变量名和值

## 免责声明

* 本程序仅供学习了解, 非盈利目的，请于下载后 24 小时内删除, 不得用作任何商业用途, 文字、数据及图片均有所属版权, 如转载须注明来源。
* 使用本程序必循遵守部署免责声明。使用本程序必循遵守部署服务器所在地、所在国家和用户所在国家的法律法规, 程序作者不对使用者任何不当行为负责.
