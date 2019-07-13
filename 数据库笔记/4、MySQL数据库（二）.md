# MySQL数据库（二）

准备数据：

```sql
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) CHARACTER SET utf8 NOT NULL,
  `age` smallint(6) NOT NULL DEFAULT '0',
  `sex` tinyint(4) NOT NULL DEFAULT '1',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `student` VALUES ('1', 'zs', '17', '1');
INSERT INTO `student` VALUES ('2', 'ls', '18', '1');
INSERT INTO `student` VALUES ('3', 'ww', '19', '1');
INSERT INTO `student` VALUES ('4', 'zl', '20', '0');
INSERT INTO `student` VALUES ('5', 'zmz', '22', '1');

-- ----------------------------
-- Table structure for enroll
-- ----------------------------
DROP TABLE IF EXISTS `enroll`;
CREATE TABLE `enroll` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `course` varchar(20) NOT NULL,
  `pay` float NOT NULL DEFAULT '0',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4;

-- ----------------------------
-- Records 
-- ----------------------------
INSERT INTO `enroll` VALUES ('1', '1', 'python_spider', '6880');
INSERT INTO `enroll` VALUES ('2', '2', 'python_web', '9288');
INSERT INTO `enroll` VALUES ('3', '3', 'english', '4980');
INSERT INTO `enroll` VALUES ('4', '4', 'java', '4000');
INSERT INTO `enroll` VALUES ('5', '5', 'english', '4980');
INSERT INTO `enroll` VALUES ('6', '2', 'english', '4980');
INSERT INTO `enroll` VALUES ('7', '4', 'french', '4880');


```





## 一、条件查询

####  1.where子句

1. 语法

`where condition [and [or]] condition`

2. 比较运算符

   `> >= < <=`

   案例：

   `select * from student where age>18;`

3. 逻辑运算符 and  or  not

   1. and:年龄大于18的男生

      `select id, name, age ,sex from student where age>18 and sex=1`;

   2. or:报名了英语，或者python的数据

      `select * from enroll where course='english' or course='python';`

4. 模糊查询 like

   1. `%`:匹配多个字符

      `select * from enroll where course like 'python%';`

   2. `_`:匹配单个字符

      查询姓名为两个字的学生

5. 范围查询

   1. 年龄 介于16-24之间的学生  `between and`

      `select * from student where age between 16 and 24;`

   2. 年龄 在 [16,18,20,22]  `in `

      `select * from student where age in (16,18,20,22);`

#### 2.其他操作

1. 排序

   `order by field`

   `select * from student order by age desc;` 倒序

   多个字段排序

   `select * from enroll order by course asc, pay desc;`

2. limit 

   `select ... limit start, count`

   `select ... limit count`

3. 去重 `distinct`

   `select distinct field,... from table；`

   `select distinct course, student_id from enroll;`

## 二、聚合与分组

#### 1.聚合函数

1. 统计数量：count

   `select count(id) as total from student where sex=1;`

2. 求和：sum

   `select sum(pay) from enroll where id=1;`

   `select sum(pay) from enroll where course='english';`

3. 最大值：max

   `select max(age) from student;`

4. 最小值：min

   `select min(age) from student where sex=0;`

5. 平均值：avg

   `select avg(age) from student;`

#### 2.分组

- 统计男生女生的数量（按性别分组，统计人数）

  `select sex, count(id) as num from student ` group by sex;

- 统计男女生的平均年龄（按性别分组，统计平均年龄）

  `select sex, avg(age) as age from student group by sex;`

- 统计每个课程的报名金额（按课程分组，统计报名总金额）

  `select course, sum(pay) as total from enroll group by course;`

- 统计总报名金额大于5000的课程（按课程分组，统计报名总金额，过滤掉小于5000的数据）

  `select course, sum(pay) as total from enroll group by course having total > 5000;`

总结，

1. 在分组的时候，查询字段，只可能是分组字段和聚合字段
2. where子句是筛选分组之前的数据，它必须在group语句之前
3. 分组后通过having关键字进行筛选

## 三、子查询

当一个查询是另一个查询的条件时，称为子查询。（select 中嵌套select)

案例：

- 查询大于平均年龄的学生

  `select * from student where age > (select avg(age) from student);`

## 四、连接查询

#### 1.内连接

1. 无条件内连接，又名交叉连接

   `select student.name ernoll.course from student inner join enroll;`

2. 有条件内连接，在无条件的基础上加上on子句

   学生分别报名了什么课程，交了多少钱

   `select name,course,pay from student join enroll on student.id=ernoll.student_id;`

####  2.外连接

1. 左连接  条件不匹配，留左表数据

   `select name,course,pay from student left join enroll on student.id=ernoll.student_id;`

2. 右连接 条件不匹配，留右表数据

   `select name,course,pay from student right join enroll on student.id=enroll.student_id;`

| mode      |            |
| --------- | ---------- |
| exit      |            |
| structure |            |
| copy      |            |
| cut       |            |
| save      | 保存       |
| as        | 当做，作为 |
| recent    | 近来的     |
| close     | 关闭       |
| rename    | 重命名     |

