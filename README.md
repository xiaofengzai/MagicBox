# MagicBox
一、集合处理

    1.获取两集合的差集
    2.获取两集合的并集
    3.获取两集合的差集

二、配置文件读取（支持cfg,conf,ini配置文件）

    1.读取指定文件指定的section,返回对应字典
    2.读取配置文件指定section,key的值
    ---依赖configparser

三.文本文件处理

    1.读取文本中字符窜
    2.读取JSON字符窜文本文件为JSON对象
    3.分割文本文件中的字符串为列表

四、JSON相关处理

    1.读取JSON文件为JSON对象
    2.判断JSON对象是否存在指定KEY
    3.从JSON对象获取指定KEY的VALUE

五、Excel转CSV

    需要安装pandas

六、数据库工具（支持Mysql,SqlServer,Mongodb）

    [Mysql,SqlServer]
    1.查询单条记录
    2.查询多条记录
    3.执行update和insert
    4.导出Excel
    -- 需安装pymysql，pymssql，xlwt

    [Mongodb]
    5.查询当前数据库所有文件集合
    6.查询单个文档
    7.根据ID查询文档
    7.查询文档集的所有文档
    -- 需安装pymongo
