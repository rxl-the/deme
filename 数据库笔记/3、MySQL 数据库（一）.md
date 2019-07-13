# MySQL 数据库（一）

## 一、数据库概述

#### 1.概述

特指计算机软件的一种

#### 2.数据库分类

- 关系型数据库（SQL），由多张互相连接的二维行列表格组成的数据库。

  优点：

  - 容易理解
  - 使用方便
  - 易于维护

  缺点：

  - i/o瓶颈
  - 扩展性不够

- 非关系型数据库 NoSQL

  分类：

  - 列式存储
  - key-value 键值型  高性能并发读写  cache
  - 文档存储  mongodb

缺点：学习成本高，不同数据库操作完全不同

## 二、MySQL介绍

#### 1.简介

MySQL是一个关系型数据库管理系统。

在WEB应用方面

特点：

- 开源
- 支持大型数据库
- 标准的SQL
- 兼容，支持多种语言

#### 2.MySQL中的数据结构

库

表

表结构：

- 表头：每一列的名称
- 列：具有相同数据类型的数据的集合
- 行：一条记录
- 值：
- 键：

#### 3.数据类型

三大类：

1. 数值
2. 时间日期
3. 字符串

## 三、MySQL的常用操作

#### 1.MySQL的进入与退出

- mysql -uroot -pqwe123     登录
- exit  退出

#### 2.MySQL库级操作

1. 显示所有的库 `show databases;`
2. 创建数据库 `create database 数据库名 charset=utf8;`
3. 删除数据库 `drop database 数据库名；`

4. 选择数据库 `use 数据名；`

#### 3.表级操作

1. 显示所有的表 `show tables;`

2. 创建表 `create table 表名 (字段名 字段类型，字段2 类型， ...)`

   ```
   create table student (
   id int unsigned primary key auto_increment,
   name varchar(20) not null,
   sex tinyint unsigned default 1,
   age tinyint unsigned 
   );
   ```

3. 显示创表信息 `show create table 表名;`

4. 显示表结构`desc 表名;`

5. 删除表 `drop table 表名;`

语法总结：

- 大小写：关键字不严格区分大小写，但是表名，库名大小写敏感

- 语句结束符：默认情况下每个语句以分号结尾`;`
- 类型：强制数据类型
- 逗号：创建表的时候，最后一个字段后面别加逗号

#### 4.数据操作

crud  操作  create  read  update delete

1. 插入数据

   ```sql
   # 指定字段插入
   insert into 表名 (字段1， 字段2，.....)
   				values
   				(value1, val2,...);
   # 全字段插入
   insert into 表名 values (all_values);
   
   # 多行插入
   insert into 表名 (字段1， 字段2，.....)
   				values
   				(value1, val2,...),	
   				(value1, val2,...),	
   				(value1, val2,...);
   ```

2.  查询数据

   ```
   select 字段1，字段2，.. from 表名 [where 子句]；
   ```

   案例：
   - 指定字段查询
     `select name, age from student;`

   - 全字段查询

     `select * from student;`

   - 带条件的查询

     查询年龄等于18的学生

     `select * from student where age=18;`

3. 更新数据

   `update 表名 set 字段=新值， 字段2=新值2，... [where 子句]；`

   - 修改所有数据

     `update student set sex=1;`

   - 修改满足条件的数据

     `update student set sex=1 where name='ww';`

   - 修改多字段

     `update student set sex=0, age=16 where id=2;`

   总结：

   - 可以更新一个或多个字段
   - 可以在where子句中指定任意条件，不加条件慎用。

4. 删除数据

   `delete from 表名 [where 子句]；`

   - 删除满足条件的数据

     `delete from student where id = 1;`

   - 删掉所有数据

     `delete from student;`

   总结；

    	1. 如果你没有指定where子句，表中所有的数据都会被删除
    	2. where子句可以指定任何条件