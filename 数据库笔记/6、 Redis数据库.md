

# Redis数据库

simple			简单的

delete			删除

find				查找

macros			宏指令

column    row	列



selection		选择

complete		结束，完成

current			当前

extend			扩展，扩大，延伸，继承

shrink			收缩

#### 一、NoSQL

是对于不同于传统的关系型数据库的统称。

特点：

 - 不支持sql     nosql 的世界里，没有通用的语言
 - 读写性能上非常高
 - 灵活的数据模型



#### 二、Redis简介

REmote DIctionary Server(Redis) 是一个由Salvatore Sanfilippo写的key-value存储系统。

开源，C语言，基于内存也可以持久化的日志型，key-value数据库。

特性：

 	1. 支持数据持久化  memcache  字符串的 key-value
 	2. 数据结构丰富
 	3. 性能高，存储速度快，一般用来做缓存。



#### 三、Redis的基本使用

1.连接redis：

​	`redis-cli`

2.退出redis:

​	`exit`

3.切换数据库：

​	redis的数据库没有名称，默认16个，通过0-15来标识，连接的时候默认选择第一个

​	`select n`



#### 四、五大数据类型的使用

#### 1. key的全局操作

对redis所有的数据类型适用：

1. 查看所有的key `keys *`
2. 删除 `del key`
3. 检查是否存在  `EXISTS 'key'`   存在返回1，不存在返回0
4. 改名 `rename oldkey newkey`
5. 设置过期时间： `expire key seconds`
6. 查看过期时间：`ttl key`  不存在返回 -2，永久存在返回-1，否则返回整数秒
7. 移除过期时间： `persist key`
8. 返回数据类型 `type key`

#### 2.五大数据类型

1. 字符串（string)

   是redis的最基本的数据类型

   - 设置数据： `set key value`  没有key就添加，有key就修改
   - 查看：`get key`
   - 追加：`append key value` 追加到原有的数据后面，字符串的拼接
   - 删除：

2. 哈希表（hash)

   Redis hash 是一个string 类型的field和value的映射表，hash特别适用存储对象

   理解为，键值都是字符串的字典

   ```
   key  ->  {
       field: value,
   }
   ```

   - 添加数据：`hmset key field value [field1  value1 ....] `一次性添加多值, 没有就创建，有就修改

     ```
     {'name': '心蓝', 'age': '18'}
     hmset person 'name' '心蓝' 'age' '18'
     ```

   -  查看hash表中某个字段的值：`hget key field ` 
   - 查询hash表中所有的字段和值：`hgetall key`
   - 查看所有的value:`hvals key`
   - 查看所有的field：`hkeys key`
   - 删除某个字段：`hdel key field`

3. 列表（list)

   简单的字符串列表，按照插入顺序排序。

   - 添加数据

     1. 头部添加（左边）

        `lpush key value [value1 ...]`

     2. 尾部添加（右边）

        `rpush key value [value1 ...]`

     3. 指定的值前/后插入数据：`linsert key before|after value new_value`

   - 查看数据：`lrange key start end` 获取列表指定范围的元素，包含start，和end，start从0开始

   - 查看指定索引数据：`lindex key index`

   - 修改指定索引数据：`lset key index value`

   - 删除

     - 左删除：`lpop key`
     - 有删除：`rpop key`

   - 获取列表长度：`llen key`

4. 集合（set)

   string类型的无序集合。集合的成员是唯一的，没有重复数据。

   - 添加数据：`sadd key member [member1 ...]` key存在则修改，不存在则创建
   - 查询所有成员：`smemebers key`
   - 指定删除：`srem key member [member1 ....]` 移除key中的一个或多个元素
   - 随机删除：`spop key`

5. 有序集合（sorted set)

   有序集合和集合一样也是string类型元素的集合，且不允许重复成员

   不同的是每个元素都会关联一个double类型的score。redis正是通过score来为集合中的成员进行从小到大的排序。

   有序集合的成员是唯一的，但是score却是可以重复的。score可以是整数，也可以是双精度的小数

   - 添加数据：`zadd key score member [score1 member1 ...]`将一个或者多个元组及其值加入到有序集合，key不存在则创建，member存在则修改socre

   - 通过索引查看：`zrange key star stop`
   - 通过score查看：`zrangebyscore key min max` 返回指定socre区间的集合元素
   - 返回成员的score: `zscore key member`
   - 返回集合长度：`zcard key `
   - 指定删除：`zrem key member [member1 ...]`
   - 通过索引删：`zremrangebyrank key start stop` 移除有序集合key中，区间为索引start到stop的，包含start和stop在内。
   - 通过score删：`zremrangebyscore key max min`移除有序集合key中，区间为score, min到max的的值，包含min和max在内。



文档：http://redisdoc.com/