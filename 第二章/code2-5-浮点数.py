# coding: utf-8
# Project：pyton study
# File：code2-5-浮点数
# Author：n00n3
# Date ：2024/4/5 16:19
# IDE：PyCharm

# 浮点数的计算
n1 = 31.1
n2 = 0.2
n = n1 + n2
print(n)
# 四射五入round
n1 = 1.1
n2 = 0.2
n3 = round(n1 + n2, 2)
print("四舍五入的结果是：",n3)

# 向上取整ceil
import math
n4 =math.ceil(n1 + n2)
print("向上取整的结果是：", n4)
# 向下取整floot
n5 =math.floor(n1 + n2)
print("向下取整的结果是",n5)

