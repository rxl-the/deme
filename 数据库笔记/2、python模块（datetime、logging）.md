# python常用模块（datetime、logging）



## 每日单词

| 单词     | 解释 |
| -------- | ---- |
| settings | 设置 |
| default  | 默认 |
| sync     | 同步 |
| import   | 导入 |
| export   | 导出 |

## 一、datetime模块

#### 1.概述

datetime是python处理时间和日期的标准库，它由一下几个模块组成：

| 类名      | 功能说明                                 |
| --------- | ---------------------------------------- |
| date      | 日期对象，year,month,day                 |
| time      | 时间对象，hour,minute,second,microsecond |
| datetime  | 时间日期对，                             |
| timedelta | 时间间隔，两个时间点之间的长度           |

#### 2.时间表示知识普及

1. 时区 

2. 格林威治时间，UTC，国际标准时间

   就是零时区的时间。

3. 时间戳（timestamp)

   是指某个时间距离格林威治时间1970，1，1，00：00：00 的总秒数。

#### 3.模块接口

1. datetime.now()===>获取当前时间（东八区）  datetime.utcnow()===>得到标准时间

```python
a = datetime.now()  # 获取当前时间
```

2. 时间日期对象.timestamp()===>日期转换为时间戳。

```python
s = datetime.now().timestamp()  # 获取时间戳
```

3. datetime.fromtimestamp(时间戳)===>时间戳转换成日期 

```python
datetime.fromtimestamp(s)
```

4. `datetime`.strftime('%Y %m %d %H %M %S')===>日期时间转换字符串

```python
datetime.strftime('%Y %m %d %H %M %S')
```

5. datetime.now()strptime(data_str, format) ===>字符串转时间日期对象

```python
m_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
```

6.  a = datetime(年，月，日)`年月日为必须输出参数`   创建新的`datetime`时间对象 

```pytjon
a = datetime(year=2017, month=12, day=23)  # 创建新的时间2017年12月23日
```



#### 4.代码案例

```python
from datetime import datetime  # 导入模块
# 获取当前时间
d = datetime.now()
print(d)

# 创建新的datetime时间对象
new = datetime(year=2017, month=12, day=23)
print(new)

# 时间日期转换成时间戳
s = new.timestamp()
print(s)

# 时间戳转换成日期
c = datetime.fromtimestamp(s)
print(c)

# datetime==>字符串格式化输出
m_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print(m_str)

```

```python
# time使用
import time
d = time.gmtime()  # 标准时间
g = time.localtime()  # 当地时间
l_1 = time.strftime('%Y-%m-%d %H:%M:%S',)  # 格式化输出
print(d)
print(g)
print(l_1)
```



简单使用

```python
from datetime import datetime

# 获取当前时间
d = datetime.now()
print(d)
# 单独取出年月日、时分秒。
print(d.year, '年',  d.month, '月',  d.day, '日',  d.hour, '时',  d.minute, '分',  d.second, '秒')
# datetime对象 -> 时间戳
st = d.timestamp()
print(st)

# datetime对象 -> 字符串 格式化输出  2019年5月7日 20点51分44秒
f_str = datetime.now().strftime('%Y-%m=%d %H:%M:%S')
print(f_str)
```

2. 时间格式化

   ```
       %Y  Year with century as a decimal number.
       %m  Month as a decimal number [01,12].
       %d  Day of the month as a decimal number [01,31].
       %H  Hour (24-hour clock) as a decimal number [00,23].
       %M  Minute as a decimal number [00,59].
       %S  Second as a decimal number [00,61].
       %z  Time zone offset from UTC.
       %a  Locale's abbreviated weekday name.
       %A  Locale's full weekday name.
       %b  Locale's abbreviated month name.
       %B  Locale's full month name.
       %c  Locale's appropriate date and time representation.
       %I  Hour (12-hour clock) as a decimal number [01,12].
       %p  Locale's equivalent of either AM or PM.
   ```

   ·

   ```python
   # 总结 三种时间的转换
   # 1. datetime
   # st = new_d.timestamp()       #  转时间戳
   # print(st)
   # new_d.strftime('%Y')    #  转字符串
   # 2. timestap   时间戳
   # d = datetime.fromtimestamp(1557072000)
   # print(d)
   # # 3. 字符串
   dt_str = '2019*5-10'
   d = datetime.strptime(dt_str, '%Y*%m-%d')  # 格式化输出格式要跟字符串格式一样
   print(d)
   ```

3.时间运算

`datetime, date`对象 之间可以进行减法运算，从而得到他们之间的时间间隔。

```python
import time
from datetime import datetime, timedelta
# 直接创建一个datetime对象  时间间隔
# 导入timedeta模块
today = datetime.now()  # 创建当前时间对象

tomorrow = today + timedelta(days=1)
yesterday = today - timedelta(days=1)
print(today)
print(tomorrow)
print(yesterday)
```

4. 时区转换

   ```python
   import time
   from datetime import datetime, timedelta, timezone
   # 导入timezone模块  时区转换
   # 创建一个时区
   tz = timezone(offset=timedelta(hours=8))
   
   
   d = datetime.now(tz=tz)
   
   new_tz = timezone(offset=timedelta(hours=5))
   
   new_d = d.astimezone(tz=new_tz)
   print(d)
   print(new_d)
   ```


## 二、logging模块

#### 1.概述

logging是python的内置的日志模块，很多的第三方库，例如scrapy，django框架的日志记录都是使用logging模块。

等级

| 日志等级（level) | 描述       |
| ---------------- | ---------- |
| DEBUG            | 调试信息   |
| INFO             | 普通信息， |
| WARNING          | 警告信息， |
| ERROR            | 错误信息， |
| CRITICAL         | 严重错误   |

#### 2.简单使用

```python
import logging      #  导入

logging.basicConfig(
    level=logging.DEBUG,        # 等级
    format="%(asctime)s-%(levelname)s-%(message)s"  # 设置输出格式
)


logging.debug('This is a debug log')
logging.info('This is a info log')
logging.warning('This is a warning log')
logging.error('This is a error log')
logging.critical('This is a critical log')
```



format格式化规则：

| Attribute name  | Format                                      | Description                                                  |
| --------------- | ------------------------------------------- | ------------------------------------------------------------ |
| args            | You shouldn’t need to format this yourself. | The tuple of arguments merged into `msg` to produce `message`, or a dict whose values are used for the merge (when there is only one argument, and it is a dictionary). |
| asctime         | `%(asctime)s`                               | Human-readable time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord) was created. By default this is of the form ‘2003-07-08 16:49:45,896’ (the numbers after the comma are millisecond portion of the time). |
| created         | `%(created)f`                               | Time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord) was created (as returned by [`time.time()`](https://docs.python.org/3/library/time.html#time.time)). |
| exc_info        | You shouldn’t need to format this yourself. | Exception tuple (à la `sys.exc_info`) or, if no exception has occurred, `None`. |
| filename        | `%(filename)s`                              | Filename portion of `pathname`.                              |
| funcName        | `%(funcName)s`                              | Name of function containing the logging call.                |
| levelname       | `%(levelname)s`                             | Text logging level for the message (`'DEBUG'`, `'INFO'`, `'WARNING'`, `'ERROR'`, `'CRITICAL'`). |
| levelno         | `%(levelno)s`                               | Numeric logging level for the message (`DEBUG`, `INFO`,`WARNING`, `ERROR`, `CRITICAL`). |
| lineno          | `%(lineno)d`                                | Source line number where the logging call was issued (if available). |
| message         | `%(message)s`                               | The logged message, computed as `msg % args`. This is set when [`Formatter.format()`](https://docs.python.org/3/library/logging.html#logging.Formatter.format) is invoked. |
| module          | `%(module)s`                                | Module (name portion of `filename`).                         |
| msecs           | `%(msecs)d`                                 | Millisecond portion of the time when the [`LogRecord`](https://docs.python.org/3/library/logging.html#logging.LogRecord) was created. |
| msg             | You shouldn’t need to format this yourself. | The format string passed in the original logging call. Merged with `args` to produce `message`, or an arbitrary object (see [Using arbitrary objects as messages](https://docs.python.org/3/howto/logging.html#arbitrary-object-messages)). |
| name            | `%(name)s`                                  | Name of the logger used to log the call.                     |
| pathname        | `%(pathname)s`                              | Full pathname of the source file where the logging call was issued (if available). |
| process         | `%(process)d`                               | Process ID (if available).                                   |
| processName     | `%(processName)s`                           | Process name (if available).                                 |
| relativeCreated | `%(relativeCreated)d`                       | Time in milliseconds when the LogRecord was created, relative to the time the logging module was loaded. |
| stack_info      | You shouldn’t need to format this yourself. | Stack frame information (where available) from the bottom of the stack in the current thread, up to and including the stack frame of the logging call which resulted in the creation of this record. |
| thread          | `%(thread)d`                                | Thread ID (if available).                                    |
| threadName      | `%(threadName)s`                            | Thread name (if available).                                  |

#### 3.将日志写到文件

```python
import logging      #  导入

logging.basicConfig(
    filename='example.log',
    level=logging.DEBUG,        # 等级
    format="%(asctime)s-%(levelname)s-%(message)s"  # 设置输出格式
)


logging.debug('This is a debug log')
logging.info('This is a info log')
logging.warning('This is a warning log')
logging.error('This is a error log')
logging.critical('This is a critical log')
```

#### 4.高级用法

| 组件                   | 说明                         |
| ---------------------- | ---------------------------- |
| Loggers(日志记录器)    | 提供程序直接使用的接口       |
| Handler(日志处理组件)  | 将记录的日志发送到指定的位置 |
| Filters（日志过滤器）  | y用于过滤特定的日志          |
| Formatters(日志格式器) | y用于控制日志信息的输出格式  |

步骤：

1. 创建一个loggers对象
2. 设置日志级别
3. 创建formatters对象
4. 定义handler对象，决定吧日志发送到哪里

```python
import json
import logging      #  导入

#1. 创建一个loggers对象
logger = logging.getLogger('%s_log' % __name__)
#2. 设置日志级别
logger.setLevel(logging.INFO)
#3. 创建formatters对象
formatter = logging.Formatter('%(asctime)s - %(filename)s [line:%(lineno)d - %(levelname)s: %(message)s]')
#4. 定义handler对象，决定吧日志发送到哪里
fh = logging.FileHandler('log.log')
fh.setLevel(logging.WARNING)

# 再创建一个handler输出日志到控制台
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
#5.设置handler的日志格式
fh.setFormatter(formatter)
ch.setFormatter(formatter)
#6.将handler 添加到logger中
logger.addHandler(fh)
logger.addHandler(ch)


data = '1.1'
logger.info('转换数据 %s 为整数' % data)
try:
    int(data)
except Exception as e:
    logger.error(e)
```

