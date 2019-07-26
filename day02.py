#!/usr/bin/env python 
# -*- coding: utf-8 -*-
# author:fei time:2019/7/25 19:32

"""
一人进入网吧，输入自己的年龄，判断是否大于等于18岁，
如果满足就输出“欢迎光临，请进”，否则则输出“未成年人不准入内！”
"""
# 练习题1
# age = int(input('请输入年龄：'))
# if age >= 18:
#     print(f'年龄{age}大爷里面请')
# else:
#     print(f'年龄{age} 滚')

# 练习题2
# user_name = input('请输入用户名：')
# code = input('请输入密码：')
# if user_name == 'zhangsan'and code == 'ilovethedog':
#     print('登录成功！')
#     monse = int(input('请输入金额转账：'))
#     if monse == 185:
#         print('转账成功！')
#     else:
#         print('转账失败！')
# else:
#     print('登录失败，账号或密码错误！')

# 练习题3
# num = int(input('请输入数字：'))
# if num % 2 == 0:
#     print('偶数')
# else:
#     print('奇数')

# 练习题4
# num = int(input('请输入数字：'))
# if num % 3 == 0 and num % 5 == 0:
#     print('能被整除')
# else:
#     print('不能被整除')
# 练习题5
# year = int(input('请输入年份：'))
# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('闰年')
# else:
#     print('不是闰年')

# 练习题6
# mone = int(input('请输入用餐金额：'))
# mone = mone - 300  # 减去报销，剩下需要AA的金额。
# if mone > 0:
#     mone = mone/3
#     print('每人应出:%0.2f元' % mone)
# else:
#     print(mone)

# 练习题7
# num1 = int(input('请输入数字（ 100 > 999 ）：'))
# if 999 > num1 > 100:
#     num2 = num1 // 100
#     num3 = num1 % 10
#     num4 = num1 // 10
#     num4 = num4 % 10
#     print('百位数是%.f' % num2)
#     print('十位数是%.f' % num4)
#     print('个位数是%.f' % num3)

# 练习题8
# grade = int(input('请输入查询成绩:'))
# if grade >= 90:
#     print('优秀')
# elif 90 > grade >= 80:
#     print('良好')
# elif 80 > grade >= 70:
#     print('合格')
# elif grade >= 60:
#     print('及格')
# else:
#     print('不合格')
