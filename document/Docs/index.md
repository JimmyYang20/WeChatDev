<h1 style="color:blue;">DocServer系统文档</h1>

# 接口说明

采用json格式报文通信，成功返回对应的业务报文，失败返回HTTP201

## 调查问卷提交接口

**请求方式**

url: http://srv:port/submit_question_naire
method: post

**请求报文:**

```
{
  naireid:1,
  choices:{1:2, 2:3, 3:4,...,29:3},
  answers:{'question4':'35岁', 'question8':'我还有其它建议'}
}
```

|标识           |说明       |类型   |备注 |
|---            |---        |---    |---  |
|naireid        |问卷id     |       |     |
|choices        |选择对象   |       |     |
|-questionid0   |问题0 id   |int    |     |
|-choiceid0     |选项0 id   |int    |     |
|-questionid1   |问题1 id   |int    |     |
|-choiceid1     |选项1 id   |int    |     |
|-questionidn   |问题n id   |int    |     |
|-choiceidn     |选项n id   |int    |     |
|answers        |填空对象   |       |     |
|-question0     |问题0 标识 |string |     |
|-answer0       |选项0 id   |string |     |
|-question1     |问题1 标识 |string |     |
|-answer1       |选项1 id   |string |     |
|-questionn     |问题n 标识 |string |     |
|-answern       |选项n id   |string |     |


**响应报文:**

```
{
  success: True
}
```

## 轮播图获取接口

**请求方式**

url: http://srv:port/wx/slide

method: post

**请求报文**
```json
{

}
```
**响应报文**
```json
{
    img: /slide_images/001.jpg   //图片路径
    title： string               //图片标题
}
```
## 医疗知识获取接口

**请求方式**

url: http://srv:port/wx/video_list

method: post

**请求报文**
```json
{

}
```
**响应报文**
```json
{
  id: 1                                      //响应数据id
  img: "/video_images/001.jpg"               //视频相关图片路径
  src: "videos/001.mp4"                      //视频播放路径
  time: "00:59:00"                           //视频播放时间
  title:"医疗小视屏的标题"                      //视频标题
  content:"这个小视频介绍的内容，希望对你有帮助！"  //视频内容简介
}
```
## 微信用户登录

**请求方式**
url: http://srv:port/wx/wxlogin

method: post

**请求报文**
```json
{
  encryptedData : "Oi2gn1x..."          //从微信服务器端获取到的用户加密数据
  iv : "jkQKyGxJYgMRcjobmoSLow=="       //从微信服务器端获取到的iv，解密时用到
}
```

**响应报文**
```json
{
  nickName: 李四,
  gender: 女,
  city: 东莞,
  province: 广东,
  country: 中国,
  avatarUrl: string,
  groups: ['patient', 'doctor', 'chronic']       // 用户的身份,
                                                 // patient表示普通用户身份,doctor表示医师身份,chronic表示慢性病患者身份
}
```

## 用户身份申请

用户使用该接口可以申请成为慢病患者身份或者医师身份

首先通过微信的`wx.uploadFile()`函数把资源上传到服务器，然后再发送以下请求。

```sequence
Title: 请求流程 
小程序->服务器: 发起upload_file
服务器-->小程序: 返回资源url 
小程序->服务器: 发起identity_apply
服务器-->小程序: 返回申请结果 
```

**请求方式**
`wx.uploadFile()`

**请求报文**
```
{

  url: 'https://srv:port/wx/upload_file',
  ...
  name: 'resource',
  formData: { type: 'identity' },
  ...
}
```

**响应报文**
```
{
  data: { 
    success: True,
    uri: '/resource/image_001.png',       
    resource_id: 1                        // 保留，未使用
  },
  statusCode: 200
}
```

url: http://srv:port/wx/identity_apply

method: post

**请求报文**
```json
{
  catelog: 'chronic' | 'doctor',         // 申请类别，chronic or doctor
  reason: string,                        // 申请理由:医师填入管理人员下发的邀请码,患者随意填入
  resource: [
    {
      type: 'image',                     // 资源类型，图像、pdf或者文本, 只支持图像
      resource_id: 1,                    // (预留，目前未使用)
      uri: '/resource/image_001.png',    // uploadFile返回的id
      data: blob,                        // 资源数据，用base64编码,(预留，目前未使用)
    },
    ...
  ]
}
```

**响应报文**
```json
{
  success: boolean                   //结果调用结果
}
```

## 智能诊断

```sequence
Title: 智能影像诊断 
小程序->服务器: 发起upload_file,上传影像
服务器-->小程序: 返回资源影像url 
小程序->服务器: 发起prediction
服务器-->小程序: 返回智能诊断结果 
```

- 上传文件

**请求方式**
`wx.uploadFile()`

**请求报文**
```
{

  url: 'https://srv:port/wx/upload_file',
  ...
  name: 'resource',
  formData: { type: 'xray' },
  ...axios.js 文档
}
```

**响应报文**
```
{
  data: { 
    success: True,
    uri: '/aiimage/image_001.png',       
    resource_id: 1                // 保留，未使用
  },
  statusCode: 200
}
```

- 智能诊断

url: http://srv:port/wx/prediction

method: post

**请求报文**
```json
{
  catelog: 'xray' | 'imagenet',          //上传图像类别，xray表示x光胸透图像
  content: string,                       //文字信息(预留，目前未使用)
  resource: [
    {
      type: 'image',                     //资源类型，图像、pdf或者文本, 只支持图像
      resource_id: 1,                    // (预留，目前未使用)
      uri: '/resource/image_001.png',    // 上传uploadFile()接口返回的值
      data: blob,                        //资源数据，用base64编码,(预留，目前未使用)
    },
    ...
  ]
}
```

**响应报文**
```json
{
  success: boolean,                       //结果调用结果
  result: {
      resource: image uri,
      label: string,                      //智能诊断标签, 多标签用逗号分隔
      date: yyyy-MM-dd hh:mm:ss,          //诊断时间
      user: String,                       //用户别名
      description: string
  },
  similarity: {                             //相似案例，（预留，目前未使用）
    total: number,                          //相似案例数量
    case:[
      {
        resource: image uri,
        label: string,                      //智能诊断标签, 多标签用逗号分隔
        date: yyyy-MM-dd hh:mm:ss,          //诊断时间
        user: String,                       //用户别名
        description: string
      },
      ...
    ]
  }
}
```
