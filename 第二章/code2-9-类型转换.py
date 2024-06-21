# coding: utf-8
# Project：pyton study
# File：code2-9-类型转换
# Author：n00n3
# Date ：2024/4/5 17:27
# IDE：PyCharm

# 转换为整数
# 字符串->整数
# 纯数字字符串
s = '2024'
print(int(s))
# 浮点数->整数
s = 2.15
print(int(s))
# 布尔->整数
s1 = True
s2 = False
print(int(s1),int(s2))


# 转换为浮点数
# str->float
s = '17.25'
print(float(s))
# int->float
s = 2024
print(float(s))
# bool->float
t = True
f = False
print(float(t),float(f))


# 转换为布尔
# str->bool
s1 = '0'
s2 = ''
print(bool(s1),bool(s2))
# int->bool
n1 = 2024
n2 = 0
print(bool(n1),bool(n2))
# float->bool
f1 = 3.14
f2 = 0.0
print(bool(f1),bool(f2))

# 转换为字符串
# int->str
n1 = 5
print(str(n1))
# float->str
f3 = 3.0
print(str(f3))
# bool->str
b2 = True
print(str(b2))

# 进制转换
s100 = "10"
print(int(s100, 2))