# MongoDB

select						选择

statement				语句

join							连接

line							行，线

fill								填充



paragraph				段落

duplicate				复制，副本

indent					缩进

unindent				取消缩进

toggle					开关，切换

## 一、认识MongoDB

#### 一、认识MongoDB

#### 1.MongoDB简介

由C++编写，基于分布式文件存储的开源数据库系统

旨在为WEB应用提供可扩展的高性能数据存储方案

将数据存储为文档，数据结构由键值对组成，类似于JSON对象。

```
{
	name: "xinlan"，
	age： 26，
	hobby： ['ball', 'meizi']
}
```

#### 2.数据模型

mongodb基本概念，文档，集合，数据库

| MongoDB                       | MySQL               |
| ----------------------------- | ------------------- |
| 数据库（database）            | 数据库（database）  |
| 集合（collection）            | 表（table）         |
| 文档（document）              | 行（row）           |
| 字段/域（field）              | 列（column）        |
| 主键，自动将_id字段设置为主键 | 主键（primary key） |



#### 二、库，集合操作

#### 1.连接服务端

1. 进入：`mongo`

   为了上手方便，默认没有用户名和密码

2. 退出：`exit`

#### 2.库级操作

1. 显示所有的库：`show dbs`

   系统库的介绍

   - admin：root数据库，管理用户
   - local：本地数据库，永远不会被复制，用来存储仅限本台服务器的数据
   - config：用于分片设置

2. 切换/创建数据：`use db_name`

   不存在则创建，插入数据才显示，默认进入test数据库

3. 查看当前数据库：`db`
4. 删除当前数据库：`db.dropDatabase()`

#### 3.集合操作（collection) 

1. 显示当前数据库的所有集合：`show collections`

2. 创建集合：`db.createCollection(name)`

   切换到当前数据库运行，`db.createCollection('student')`

3. 删除集合：`db.collection.drop()`  # collection 是集合名称

   `db.student.drop()`

注意：在MongDB中，集合只有在内容插入之后才会创建

注意：命令大小写敏感

#### 三、文档（数据）操作

每条数据，就是一个document，就是一条json

#### 1.添加文档

1. 添加单条：`db.collection.insert(document)`

   案例：

   ```
   db.student.insert({
   name:'张三',
   age:18,
   sex:'男',
   course:['python', 'english', 'java']
   })
   ```

   

2. 添加多条：`db.collection.insertMany([doc1,doc2,...])`

   案例：

   ````
   db.student.insertMany([
   {'name': '李四'},
   {'name': '王五', 'length': 170},
   {'name': '赵六', 'married': true},
   ])
   ````

#### 2.查询

语法：`db.collection.find(query, porjection)`

​	query：可选，使用查询操作符指定查询条件

​	porjection：可选，指定返回的键，省略代表返回所有的键

1.查看集合中全部数据：`db.collection.find()`

2.格式化显示：`db.collection.find().pretty()`

3.查看满足条件的数据：查询student集合中name=‘张三’的文档

`db.student.find({name:'张三'})`

4.projection 参数的用法

若不指定，默认返回所有的键

1. inclusion（包含）模式

   `db.collection.find(query, {filed1:1， field2:1})` 指定返回 field1，field2

   案例

   `db.student.find({name:'张三'},{name:1,age:1})`

2. exclusion（排除）模式

   `db.collection.find(query, {filed1:0， field2:0})` 排除指定的field1，field2

   案例：

   `db.student.find({name:'张三'},{_id:0})`

总结：

1. _id主键，默认返回，需要主动指定_id：0 才会隐藏

2. 两种模式不能混用（除了_id字段)

   `db.student.find({name:'张三'},{age:0, name:1})`  错误的用法

#### 3.条件

1. 比较条件

   1. 大于 `$gt`:	`db.collection.find({field: {$gt: value}})`

      案例：查询年龄大于18的学生数据

      `db.student.find({age: {$gt: 18}, sex: '男'})`

   2. 大于等于 `$gte`

   3. 小于 `$lt`

   4. 小于等于 `$lte`

   5. 不等于 `$ne`

2. 逻辑操作符

   条件和条件直接的关系

   1. `$and`：`db.collection.find({$and:[condition1, codition2,...]})`

      查询年龄大于18，性别为男的学生信息

      ```
      db.student.find({
      $and:[
      	{age: {$gt:18}},
      	{sex: '男'}
      ]
      })
      ```

   2. `$or`： `db.collection.find({$or:[condition1, codition2,...]})`

      查询年龄大于18，或者性别为男的学生信息

      ```
      db.student.find({
      $or:[
      {age: {$gt:18}},
      {sex: '男'}
      ]
      })
      ```

      

#### 4.更新

语法：

```
db.collection.update(
<query>,
<update>,
{
	upsert: <boolean>,
	multi:<boolean>,
}
)
```

参数说明：

- query：查询条件
- update：update的对象和一些更新操作符
- upsert：可选，当设置为true时，如果不存在则插入，默认是false，不插入
- multi：可选，默认false，只更新找到的数据的第一条，如果设置为true，所有结果全部更新

1.全文档替换：`db.collection.update(query, document, ...)`

​	案例：`db.student.update({sex:'男'},{xxx: 'xxxxx'})`  # 这条命令，会将查到的第一条数据，更新为`{xxx: 'xxxxx'}`

2.指定修改：`db.collection.update(query, {$set:{field1:value, field2:value}}, ....)`

案例：

```
db.student.update(
{name: '王五'},
{$set:{length:180}},
)
```

#### 5.删除

语法：

```
db.collection.remove(
<query>,
{
	justOne: <boolean>,
}
)
```

参数说明：

- query： 查询条件

- justOne,可选，设置为true或者1，只删除查询结果的第一条数据，默认false则删除匹配到的所有数据

  1. 删除集合中的所有文档： `db.collection.remove({})`

  ```
  db.student.remove(
  {},
  {justOne: true}
  )
  ```

#### 6.其他操作

1. 排序：`db.collection.find().sort({field:1/-1})`

   使用sort方法对数据进行排序，sort方法可以通过参数指定排序字段，1，升序，-1，降序

   案例：学生安装年龄升序排列

   `db.student.find().sort({age:1})`  

   当然可以有多字段

2. limit与skip

   1. limit

      `db.collection.find().limit(num)`

   2. skip

      `db.collection.find().skip(num)` 当然可以和limit一起使用

3.分组与聚合

MongoDB中聚合的方法是`aggregate()`

1. 求和 `$sum`

   案例：统计男女分别多少人

   ```
   db.student.aggregate([
   {$group: {_id:'$sex', num: {$sum:1}}}
   ])
   
   => select sex, sum(id) as num from student group by sex;
   ```

   统计总人数

   ````
   db.student.aggregate([
   {$group:{_id:null, num:{$sum:1}}}
   ])
   => select count(id) as num from student;
   ````

2.求平均值 `$avg`

​	案例：统计学生平均年龄

```
db.student.aggregate([
{$group:{_id:null, avg_age:{$avg:'$age'}}}
])
=> select avg(age) as avg_age from student;
```

统计男生的平均年龄

```
db.student.aggregate([
{$match: {sex:'男'}},
{$group:{_id:null, avg_age:{$avg:'$age'}}}
])
=> select avg(age) as avg_age from student where sex='男';
```

3. 最大值 `$max`

   案例，学生中的最大年龄

   ```
   db.student.aggregate([
   {$group: {_id:null, max_age:{$max: '$age'}}}
   ])
   
   => 
   select max(age) as max_age from student;
   ```

4. 最小值`$min`



官方文档：https://docs.mongodb.com/manual/crud/

#### 四、python操作MongDB

paragraph					段落

duplicate					复制，副本

indent						缩进

unindent					取消缩进

toggle						开关，触发



case

convent					转换

next						下一个

previous				上一个

encode				  编码



python连接MongoDB的驱动，使用得最多的是PyMongo。

支持：python2.7,3.4+

安装：`pip install pymongo`

为了学习方便需要作如下设置：

1. 设置端口映射，虚拟机27017端口映射到物理机27017

2. 修改，`sudo vim /etc/mongodb.conf` 配置文件中的

   `bind-ip = 0.0.0.0`

3. 重启mongo服务`service mongodb restart`

#### 2. 连接

```python
import pymongo
# 套路
# 1.创建连接
client = pymongo.MongoClient(host='127.0.0.1', port=27017)
# 2.选择/创建数据库   不存在则创建
# 获取所有数据库
databases = client.list_database_names()       # 返回一个列表
print(databases)
db = client['tanzhou']  # => client.tanzhou
# 3.选择/创建集合    => db.student
collection = db['student']
# 获取所有的集合
cols = db.collection_names()
print(cols)
```

#### 2.文档操作

1. 添加数据

   ```python
   # 1.插入一个文档
   doc = {'name': '心蓝', 'age': 18}
   
   insert_id = collection.insert_one(doc).inserted_id
   # 2.插入多个文档
   docs = [
       {'name': '心蓝', 'age': 18},
       {'name': '句号', 'age': 19},
       {'name': '王福鑫', 'age': 20},
       {'name': '李慧旺', 'age': 21},
       {'name': '张伟', 'age': 22},
   ]
   insert_ids = collection.insert_many(docs).inserted_ids
   print(insert_ids)
   ```

2. 查询数据

```python
# 2.查询文档
# 1.查询一条，只想取匹配到的第一条
one = collection.find_one({'age': {'$gt': 18}})
# print(one)
# 2.查询所有
all_docs = collection.find()
# for doc in all_docs:  # all_docs是一个游标对象，需要迭代取出数据
#     print(doc)
# docs = [x for x in all_docs]
# print(all_docs)

# 3查询指定字段
docs = collection.find({}, {'name': 1, 'age': 1})

# for doc in docs:
#     print(doc)

# 4limit,skip

docs = collection.find().limit(3).skip(3)
# for doc in docs:
#     print(doc)

# 5排序
# 1.单字段排序
docs = collection.find({}, {'age': 1}).sort('age', -1)
# for doc in docs:
#     print(doc)
# 2.多字段排序
docs = collection.find({}, {'age': 1, 'name': 1}).sort([
    ('age', -1),
    ('name', 1)
])
for doc in docs:
    print(doc)
```

3. 更新

   ```
   # 更新
   # 1.全文档替换
   # doc = {'name': '心蓝', 'age': 16}
   # res = collection.replace_one({}, doc)  # upsert参数可选，如果设置为True,匹配不到数据就插入
   # print(res.matched_count, res.modified_count, res)
   
   # 2.修改一条
   # res = collection.update_one({}, {'$set': {'name': 'xinlan'}})
   # print(res.matched_count, res.modified_count, res)
   
   
   # 3.修改多条
   # res = collection.update_many({'name': '心蓝'}, {'$set': {'name': 'xinlan'}})
   # print(res.matched_count, res.modified_count, res)
   
   ```

   4. 删除文档

      ```python
      
      # 删除
      # 1.删一条
      # res = collection.delete_one({})
      # print(res.raw_result, res.deleted_count)
      
      # 2.删多条
      # res = collection.delete_many({'name': 'xinlan'})
      # print(res.raw_result, res.deleted_count)
      ```

   5.聚合与分组

   ```
   ## 聚合与分组
   
   pipline = [
       {'$group': {'_id': '$sex', 'count': {'$sum': 1}}},
       {'$sort': {'count': -1}}
   ]
   res = collection.aggregate(pipline)
   
   for item in res:
       print(item)
   ```

   









