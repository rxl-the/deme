# python操作数据库

selection 			选择		名词

complete			完成，结束

current				当前

shrink				收缩

extend				扩大，延伸，继承				



statement			语句

select				选择		动词

join					连接

line					行

fill					填充



## 一、python操作MySQL

socket

cs架构  client 客户端    server 服务端

连接前的准备工作：

1. 设置端口映射                                       mysql服务默认监听3306

   设置虚拟机3306端口映射物理机的3306端口  (这个决定了你能否在物理机连上你的mysql)

2. 使用develop 用户  `develop    QWEqwe123`

#### 1.PyMySQL介绍

是一个纯python的MySQL客户端库。它大多数API都兼容了`mysqlclient`, `MySQLdb`

1. 支持：

​	python 2.7 ，3.5+

​	MySQL server  5.5 +

2. 安装：

   `pip install PyMySQL`



#### 2.简单使用

```python
import pymysql

# 套路，步骤
# 1. 创建连接
conn = pymysql.connect(
    host='127.0.0.1',           # 主机
    port=3306,                  # 端口
    user='develop',             # 用户名
    password='QWEqwe123',       # 密码
    db='tz',                    # 数据库
    charset='utf8'              # 字符编码
)

# 2. 创建游标
# 通过指定cursor的构造类，返回字典形式的结果
cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

# 3. 执行sql语句
cursor.execute('select name as aa from student')

# 4.获取结果
res = cursor.fetchall()

print(res)

# 5.关闭游标
cursor.close()

# 6.关闭连接
conn.close()

```

#### 3. 使用pymysql进行查询

````python
# 4.获取结果
res1 = cursor.fetchone()        # 获取一条  返回的是 一条数据 字典，元组
print('获取一条')
print(res1)
res2 = cursor.fetchmany(3)      # 获取多条  返回的是 多条数据  列表
print('获取三条')
print(res2)
res = cursor.fetchall()         # 获取多条
print('获取剩下所有的')

print(res)

res3 = cursor.fetchone()        # cursor 中的数据流，只能被读一次
print(res3)
````

#### 4.使用pymysql进行增删改

```python
import pymysql

# 套路，步骤
# 1. 创建连接
conn = pymysql.connect(
    host='127.0.0.1',           # 主机
    port=3306,                  # 端口
    user='develop',             # 用户名
    password='QWEqwe123',       # 密码
    db='tz',                    # 数据库
    charset='utf8',              # 字符编码
    cursorclass=pymysql.cursors.DictCursor
)

# 2. 创建游标
# 通过指定cursor的构造类，返回字典形式的结果
# pymysql 默认支持事务
try:
    with conn.cursor() as cursor:
        # 3.构建 sql语句  动态
        from_name = input('请输入转账账户名>>>>：')
        to_name = input('请输入转入账户名>>>>:')
        money = int(input('请输入转账金额>>>>>:'))
        # 直接拼接的方法不推荐，会发生sql注入
        sql1 = 'update account set money=money-%s where name=%s'

        sql2 = 'update account set money=money+%s where name=%s'
        # 4.执行sql语句
        cursor.execute(sql1, args=(money, from_name))
        cursor.execute(sql2, args=(money, to_name))
        # 5. 提交事务
        conn.commit()
except Exception as e:
    # 有异常
    print(e)
    # 6.处理异常，并回滚
    conn.rollback()         #  回滚
finally:
    # 7. 关闭连接
    conn.close()

```





## 二、python操作redis

#### 1.redis-py介绍

redis-py是键值数据库redis的python实现接口。

两个大版本，2.x， 3.0  3.0有很多新特效，使用的时候需要做兼容处理

1. 支持：

   3.0：

   - python2.7，python3.4+

2. 安装

   `pip install redis`

   不要`sudo`安装,推荐安装在`virtualenv`

连接前的准备工作：

1. 设置端口映射                                       redis服务默认监听6379

   设置虚拟机6379端口映射物理机的6379端口  (这个决定了你能否在物理机连上你的redis)

#### 2.redis-py 操作redis

python 操作redis的命令和命令行几乎一致，除了`del`,因为和关键字重名，用delete代替。

```python
import redis

# 套路
# 1.建立连接
# conn = redis.Redis(
#     host='127.0.0.1',  # localhost
#     port=6379,
#     db=0
# )

conn = redis.StrictRedis(  # 兼容旧版本（推荐使用）
    host='127.0.0.1',  # localhost
    port=6379,
    db=0,
    decode_responses=True   # 设置为True返回的数据格式就是str类型
)

# key 的操作
res = conn.keys('*')
print(res)
print(conn.delete('Name'))
print(conn.keys('*'))

```

1. 字符串
   1. 新建数据：`conn.set(key, value)` 设置字符串数据，成功返回 `True`

#### 3.piplines

管道是redis类的子类, 它支持在一个请求中缓冲多个命令到服务器

