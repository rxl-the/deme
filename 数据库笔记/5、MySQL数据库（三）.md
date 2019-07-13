# 在·MySQL数据库（三）

#### 一、字段约束 条件

```
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT ,
  `name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `age` smallint(6) NOT NULL DEFAULT '0',
  `sex` tinyint(4) NOT NULL DEFAULT '1',
  `num` int(11) DEFAULT NULL unique,
  PRIMARY KEY (`id`),
  UNIQUE KEY `num` (`num`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4
```

##### 1. 默认约束

关键字：`default`

##### 2.非空约束

关键字：`not null`

##### 3.唯一约束

关键字：`unique key`

##### 4.主键

关键字：`primary key`

##### 5.自增长

关键字：`auto_increment` 自动编号 和主键组合使用

##### 6.外键

关键字：`foreign key`

保持数据一致性，从表有的，主表一定有，主表没有的，从表一定没有

A表中的 某个字段 Foreign key 指向了B表中的 pirmary key,B表就叫主表，A表就叫从表。

级联操作：

外键约束用于预防破坏表之间的连接动作。

1. 限制

   默认情况，当从表中的数据引用了主表中的某条数据，那么主表中的数据不能被删除。

2. 删除

   当主表中的数据删除时，从表中引用这条记录的数据都会被删除

   `foregin key(college_id) references college(id) on DELETE CASCADE`

3. 设置为null

   当主表中的数据删除时，从表中的外键字段设置为Null

#### 二、表结构修改

##### 1.修改表名

语法：

`alter table 表名 rename to 新的表名;`

##### 2.修改字段名

语法：

`alter table 表名 change 字段名 新的字段名 新的字段类型;`

`alter table Student change name Name varchar(20);`

##### 3.修改字段类型和约束

语法：

`alter table 表名 modify 字段名 新的字段类型`

alter table account modify money int unsigned 

##### 4.添加字段

语法：

`alter table 表名 add 字段名 字段类型 [first, after 字段名]；`

可选参数 first，代表插入第一行

after 字段名，代表插入到某个字段的后面

##### 5.删除字段

语法：

`alter table 表名 drop 字段名`

#### 三、表关系

学生选课系统：

学院表，

学生表，

课程表，

报名表，



#### 1. 多对一

一个学院可以有多个学生，一个学生只会属于一个学院，name学生表和学院表之间就形成了一对多的关系。

```sql
# 创建学院表
-----------------------
create table college (
	id int not null primary key auto_increment,
    name varchar(20) not null
);

insert into college values 
(0, 'python'),
(0, 'java'),
(0, 'c++');
-----------------
# 创建学生表
------------------
create table student (
    id int not null primary key auto_increment,
    name varchar(20) not null,
    college_id int not null,
    foreign key(college_id) references college(id) on DELETE CASCADE
);

insert into student (name, college_id) values
('jh', 3),
('zjw', 1),
('zw', 1);

insert into student (name, college_id) values ('xinlan', 10);

```

为了保证数据的一致性，可以建立外键来约束，一般，外键建立在多的一方

#### 2.多对多

学生可以报名多个课程，一个课程也可以被多个学生报名

学生表和课程表形成了多对多的关系

多对多关系需要通过中间表来实现

```sql
-------------
# 创建课程表
-------------
CREATE TABLE `course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `title` varchar(20) NOT NULL,
  PRIMARY KEY (`id`)
);

INSERT INTO college (title) values
('python_web'),
('python_spider'),
('python_data_analysis');

---------------------
# 创建选课表 中间表
------------------
CREATE TABLE `student_course` (
  `stu_id` int(11) NOT NULL,
  `cou_id` int(11) NOT NULL ,
  PRIMARY KEY (`stu_id`,`cou_id`),
  unique key (stu_id, cou_id),					# 联合唯一
  FOREIGN KEY(`stu_id`) REFERENCES student(id) ON DELETE CASCADE,
  FOREIGN KEY(`cou_id`) REFERENCES course(id) ON DELETE CASCADE
);

INSERT into student_course (id_stu, id_cou) values
(1, 1),
(1, 2),
(1, 3),
(2, 1),
(3, 2),
(4, 4),
(5,5);

# 需求，查询学生报名课程表，
学生姓名，报名课程
学生表， 课程表
报名表中
先查 表名表中的学生姓名
select s.name, c.title from student_course as sc left join student as s on sc.stu_id = s.id left join course as c on sc.cou_id = c.id;
```

#### 3.一对一

用于一张表的字段过多，我们进行分表处理

通过外键 + 唯一

```
CREATE TABLE `student_detail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stu_id` int(11) NOT NULL unique,
  `hobby` varchar(20) ,
  PRIMARY KEY (`id`),
  FOREIGN KEY(`stu_id`) REFERENCES student(id) ON DELETE CASCADE
);
```

#### 四、事务

事务的作用时保证操作的一致性。

在mysql中，只有使用了`InnoDB`数据库引擎的数据库，或表才支持事务。

事务处理用来维护数据库的完整性，保证批量的SQL语句要么全部执行，要么全部不执行。

事务用来管理，insert，update，delete语句，对数据又更新操作的



默认情况下，mysql客户端对修改数据库的命令，自动触发事务。

1. 特性（ACID）

   1. 原子性

      一个事务必须被视为一个不可分割的最小工作单元，整个事务的所有操作要么全部成功，要么全部回滚，对于一个事务来说，不可能执行其中的某一部分操作

   2. 一致性

      事务如果失败，数据库一定会恢复到执行前的状态，如果成功一定会转换成目标状态。

   3. 隔离性

      一个事务所做的修改再最终提交以前，对其他事务是不可见的。

      事务的隔离性是为了保证不同事务的操作冲突。

      事务隔离性有高低级别：

      - 事务串行化执行，级别最高，牺牲了系统的并发性。
      - repeated Read，开始一个事务后，对数据的读取结果总是相同，无论其他事务是否进行了操作，以及是否提交。
      - read committed,只有事务提交后，期更新结果才会被其他事务看见。
      - read uncommitted，最低级别，什么都不做，一个事务可以读到另外一个事务未提交的结果。所有的并发事务问题都会发生。

   4. 持久性

      一旦事务提交，所有修改永远保存到数据库，即使系统崩溃，修改的数据也不会丢失。

2. mysql操作事务

   通过关键字`begin, rollback, commit`



   ```
   begin;
   #批量 sql 语句
   #如果都成功
   commit;		# 提交到数据库
   
   # 如果有执行失败的
   rollback;   # 回滚
   
   
   一旦，提交了，或者回滚了，当前事务就结束。
   # 来一个银行转账的案例
   create table account (
   id int primary key auto_increment,
   name varchar(20) not null,
   money float
   );
   insert into account values (0, 'A', 200), (0, 'B', 100), (0, 'C', 0);
   
   A 转账 100 给 B
   1. A 账上扣掉100
   update account set money=money-100 where name='A';
   2. 给B账上加上100
   update account set money=money+100 where name='B';
   
   A 300   -100      200 -100   100
   B 100 
   ```
