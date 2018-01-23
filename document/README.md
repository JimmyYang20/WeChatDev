# 目录说明
document目录包含了一个完整的mkdocs工程和搜索引擎的文档

** mkdocs工程包括的文件如下: **
- `mkdocs.yml`配置文件
- `Docs`文档源文件
- `sites`编译好的网页文件存放目录

** 搜索引擎包含的文件如下: **
- `searchDocs`

# mkdocs工程配置
它与标准版的mkdocs工程不同，这个工程支持时序图、甘特图等等一系列图像绘制，需要额外安装一些扩展才能够运行起来。

## 安装依赖
```
pip install mkdocs-material pymdown-extensions
pip install Pygments==2.2.0
```

## 构建运行
```
mkdocs build
mkdocs serve
```

# 搜索引擎

1. 创建集群

```
[solrusr@VM_0_11_centos solr-7.1.0]$ ./bin/solr start -e cloud
```

2. 输入节点数量：1， 以及输入节点端口：8983

```
Welcome to the SolrCloud example!

This interactive session will help you launch a SolrCloud cluster on your local workstation.
To begin, how many Solr nodes would you like to run in your local cluster? (specify 1-4 nodes) [2]: 
1
Ok, let's start up 1 Solr nodes for your example SolrCloud cluster.
Please enter the port for node1 [8983]: 

Creating Solr home directory /data/release/solr-7.1.0/example/cloud/node1/solr

Starting up Solr on port 8983 using command:
"bin/solr" start -cloud -p 8983 -s "example/cloud/node1/solr"

Warning: Available entropy is low. As a result, use of the UUIDField, SSL, or any other features that require
RNG might not work properly. To check for the amount of available entropy, use 'cat /proc/sys/kernel/random/entropy_avail'.
```

3. 等待节点启动

```
Waiting up to 180 seconds to see Solr running on port 8983 [/]  
Started Solr server on port 8983 (pid=5947). Happy searching!

INFO  - 2017-12-27 22:06:30.620; org.apache.solr.client.solrj.impl.ZkClientClusterStateProvider; Cluster at localhost:9983 ready

Now let's create a new collection for indexing documents in your 1-node cluster.
```

4. 输入collection名称`exuntong`, `shards`和`replicas`

```
Please provide a name for your new collection: [gettingstarted] 
exuntong
How many shards would you like to split exuntong into? [2]

How many replicas per shard would you like to create? [2] 
```

5. 输入`configuration`模板`sample_techproducts_configs`

```
Please choose a configuration for the exuntong collection, available options are:
_default or sample_techproducts_configs [_default] 
sample_techproducts_configs
Created collection 'exuntong' with 2 shard(s), 2 replica(s) with config-set 'exuntong'

Enabling auto soft-commits with maxTime 3 secs using the Config API

POSTing request to Config API: http://localhost:8983/solr/exuntong/config
{"set-property":{"updateHandler.autoSoftCommit.maxTime":"3000"}}
Successfully set-property updateHandler.autoSoftCommit.maxTime to 3000


SolrCloud example running, please visit: http://localhost:8983/solr 
```

## 文档建索引

当前的搜索引擎不支持json格式的文档，但是对xml,pdf，html等格式的文档支持得很好，固需要调用`tools/create_xml_file.py`工具把json格式的文档转换为xml文档，再执行一下命令。

```
./bin/post -c exuntong searchDocs/*
```


