# python常用模块（json、base64、hashlib）

## 一、json模块

#### 1.json概述

json其实就是一种文本格式，用来在不同的应用中传递数据。

json字符串案例：

```json
{"name":"心蓝", "age": 18, "salary": 5000.5, "hobby": ["money", "girl"]}
```

#### 2.语法规则

*字符串一定要用双引号*

| python     | json        |
| ---------- | ----------- |
| 字典       | 对象        |
| 列表       | 数组        |
| 字符串     | 字符串      |
| int或float | 数字        |
| True,False | true或false |
| None       | null        |

#### 3.json模块接口

1. json.dunmps(obj)===>将python数据转换成json数据。

```python
my_json = json.dunmps(dict1, ensure_ascii=False, inden=1)  # ensure_ascii用于ascii解析，inden=1实现缩进缩进。
```

2. json.loabs(s)===>将json数据转换成python。

```python
dact1 = json.loabs(my_json)  # 括号里传入要转换的joon数据，dict1接收转换成python的字符数据。
```

3. json.dump(obj,fb)===>转换为josn保存在文件中。

   ```python
   with open('tzu.json', 'w', encoding='utf-8') as f:  # 生成文件
       josn.dump(dict1, f,ensure_ascii=False, inden=1)  # 括号写入要保存的文件及文件句柄
   ```

4. json.loab(fb)===>读取文件中的json数据，并转换成python数据。

   ```python
   with open('tzu.json', 'r', encoding='utf-8') as f:  # 读取文件
       dact1 = json.loab(f)  # 使用语法，转换括号里传入文件句柄，dict1接收转换后的pyth文件
   ```

   

- 总结：语法里面带s的是处理字符串，没有带s的则是要处理的文件。



#### 4.json 代码案例

```python
import json  # 导入json模块
# json 格式的字符串
json_str = '{"name":"心蓝", "age": 18, "salary": 5000.5, "hobby": ["money", "girl"]}'
# 需求，改掉 name对应的值，为‘xinlan’
# json字符串 -> python object
# json 字符串转换成 python中的数据类型
data = json.loads(json_str)     # 转换成字典
# print(data)
data['name'] = 'xinlan'  # 使用字典方法修改name的值
data['hobby'].append('慢跑')  # 兴趣里面添加‘慢跑’
# print(data['hobby'][-1])  # 打印查看兴趣里面最后一个内容。
# print(data)
# python object -> json 字符串
json_str = json.dumps(data, ensure_ascii=False, indent=1)  # 修改后的数据转换成json字符串。
print(json_str)  # 打印查看转换后的字符串。
print(type(json_str))  # 查看字符类型
```

```python
# json文件写入 json.dump(obj, fp) 转换为json并保存到文件中
import json  # 导入模块
data = {"name": "心蓝", "age": 18,"feature": ["高", "富", "帅"]}
# 生成写入文件 tzu.json，写入（w）
with open('tzu.json', 'w', encoding='utf-8') as f:
# 使用 json.dump 语法将 data 转换成josn文件 并保存
    json.dump(data, f, ensure_ascii=False, indent=1)
```



```python
#json文件读取  json.load(fp)  从文件中读取json，并转化为python数据
with open('tzu.json', 'r', encoding='utf-8') as f:  # 打开文件tzu.json 读取（r） 
    data1 = json.load(f)   # 使用变量接收 json.load(f) 读取出来的数据   
    print(data1['feature'][1])  # 根据需求提取需要的数据（字典方法）

```



#### 5.总结注意事项

1. json格式字符串使用双引号
2. python数据类型在转换成json类型时，在文本里有中文时需要使用（出现乱码） ensure_ascii=False 
3. indent = 1 可以让文本 缩进1格，可以让代码具有更好的可读性。

## 二、hashlib

#### 1.数据安全

数据加密

- 对称加密：数据加密和解密的秘钥相同
- 非对称加密：加密和解密的秘钥不相同 公钥，私钥
- 单向加密：只能加密，不能解密（原则上，不属于加密）

1. hash

   一种算法的名称，哈希，散列

   它是把，任意长度的输入通过算法转变成固定长度的输出，该输出就是散列

   - 不可逆
   - 定长输出
   - 抗修改性
   - 强碰撞性

   应用：

   - 数据指纹
   - 区块链
   - 数据加密

#### 2.hashlib模块的接口

1. md5
2. sha系列：sha1 ,sha224, sha256, sha384, sha512

#### 3.代码案例



```python
# 使用hashlib
import hashlib
info = '新蓝老师最帅！'
m = hashlib.md5(info.encode())     # 注意一定要传递二进制数，不能是字符串
res1 = m.hexdigest()                # 散列字符串
res2 = m.digest()                   # 二进制数据格式输出
print(res1)
print(res2)
```

```python
import hashlib
# 1.选择一种算法， 创建一个算法对象
m = hashlib.md5()   
# 2. 添加数据
m.update('新蓝老师'.encode())  # 传入数据要转换成二进制数据
m.update('最帅！'.encode())
# 3.获取散列结果
res = m.hexdigest()  # res接收结果，m对象转换成hexdigest（散列字符串）
print(res) 
```

`案例思路：`

`1、创建一个算法对象用一个变量（m）接收以后要传入进去的数据。`

`                     2、使用update添加更新数据，数据添加要使用encode转换成二进制数据（一定要是二进制数据）。`

`3、将m接收的的值转换成散列字符，重新赋值给res接收，最后打印。`

大文件hash

```python
# 使用hashlib  hash 大文件 
import hashlib
# 1.创建算法对象
m = hashlib.md5()
# 2.读取文件
with open('json.wmv', 'rb') as f:
    for line in f:  # 大文件时无法全部一次读取，使用循环分多次读取。
        m.update(line)

res = m.hexdigest()
print(res)
```

 **案例思路**

1、创捷一个算法对象。

2、读取文件。

3、使用for循环对文件（循环读取创建的文件句柄 f ）进行重复分段读取.

4、将循环读取的文件更新添加到算法对象（m）里面 m.update(line)

5、将算法结果转换成散列字符，赋值给res输出

#### 4.总结及注意事项

1.创建的hashlib传入数据必须为二进制数据，所有需要使用encode转换成二进制格式。

2.在遇到大文需要加密时可以使用for循环进行分段读取，否则遇到超大文件是会加载不了。

## 三、base64

#### 1. 概念

base64是一种编码方式，将二进制数转换成字符串的方法。

用途：

- 二进制转文本便于网络传输
- 简单加密，不可见

#### 2.原理

1. 标准的base64编码

   首先准备一个包含64个字符的数组：

   `['A', 'B',...,'a', 'b',...'0', '1',...'9', '+', '/']`

   对二进制数据进行梳理，每3个字节为一组，一共就是3*8=24位，划分成4组，每组刚好6位

   然后将6位二进制数转换成10进制数，得到4个索引，然后查表，获得相应的4个字符，就是编码后的字符串。

   如果要编码的二进制数长度不是3的倍数，最后会剩下 1，或者2个字节，就是用`\x00`再末尾补充

   再到编码末尾加上1到2个`=`号，表示补了多少个字节，解码的时候，会自动去掉。

   'a'   01100001 00000000 00000000

   011000   010000  000000 000000

   24             16             0            0

   Y		Q		=             =  

2. 自定义base64编码

   其实就是改变字符串数组的字符，和顺序

3. url safe 编码

   对url进行base64编码。标准的base64中，`+, /`  不能直接作为url参数，所以有又出现一种，url safe base64编码。

   它将`+， /` 替换成 `-,_`,并且去掉补齐的`=`

#### 3. 模块的接口

1. **base64.b64encode(s)**  二进制数据base64编码。传入数据必须是二进制数据，需要使用`encode`进行二进制转换。

```python
res = b64encode(data.encode())  # 插入数据,转换成二进制，使用b64encode转换成编码，赋值给res
```

2. **base64.b64decode(s).decode('utf-8')**  base64解码。括号传入要解密的的数据，传入数据也必须是二进制数据，在使用`decode('utf-8')`进行解码。

```python
res1 = base64.b64decode(res).decode.('utf-8')
```

3. base64.urlsafe_b64encode(s) 对URL进行base64编码（使用方法同上面一样）

```python
res = base64.urlsafe_b64encode(data.encode())  # 传入数据，进行二进制转换，使用方法编码，赋值res
```

4. base64.urlsafe_b64decode(s) 解码（解码后是二进制数据，需要对数据进一步的编码转换使用）

```python
data1 = base64.urlsafe_b64decode(data).decode.('utf-8')  # 解码后数据为二进制格式使用编码进行解码
```

编码接受的是二进数据，返回的也是二进数据

解码接受的也是二进数据，返回的也是二进数据

#### 4.案例

```python
import base64
data = '心蓝最帅'
res = base64.b64encode(data.encode())           # 编码  需要传入二进制数
res2 = base64.b64decode(res)
res2 = res2.decode('utf-8')                    # 解码  返回的是二进制数
print(res)
print(res2)
```

#### 5.总结注意事项

1. 编码传入的数据以及解码返回的结果，都是二进制数据，在对返回的二进制数据需要解码时使用`decode.('utf-8')`进行解码。
2. 在使用`encode()`时注意后面括号的添加，多次出错。





