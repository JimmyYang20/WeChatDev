<h1 style="color:blue;">小程序前端通过json格式报文与搜索引擎通信</h1>

# 请求url
```
https://e讯通/search
```

# 请求报文
```
{
    q: content,          //content表示要搜索的内容
    start: int,          //返回结果起始数
    rows: int,           //返回结果条数
    fl: string,		 //非必填，需要高亮的字段名，默认是content
    h.pre: string,	 //非必填, 高亮的前字符,默认是<span style="color:red;">
    h.post: string,	 //非必填，高亮的后字符，默认是</span>
}
```

# 响应报文

响应报文由通用报文框架和业务报文组成，通用的报文框架如下所示:

```
{
    response:{
        numFound: int,       //找到的匹配文档数量
        start: int,          //文档结果开始坐标
        maxScore: float,     //最大匹配分数
        docs: [
            bussinessObj0,   //业务报文对象0
            bussinessObj1,   //业务报文对象1
            ...
        ]
    }
    highlighting:{
   	"doc-id": {
	    "content": [....]
    	}, 
   	"doc-id": {
	    "content": [....]
    	}, 
	...
    }
}
```

## 主页按钮报文

```
{
    name: string,           //按钮的标题
    cat: "button",          //button表示按钮
    content: string,        //按钮对应的功能说明
    pageUrl_s: string,      //点击按钮需要调整的页面地址
    iconClass_s: string,    //按钮的css class name
    id: string              //索引id

}
```
