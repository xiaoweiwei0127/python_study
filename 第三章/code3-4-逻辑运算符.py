# coding: utf-8
# Project：pyton study
# File：code3-4-逻辑运算符
# Author：n00n3
# Date ：2024/4/7 11:10
# IDE：PyCharm

# and
print(True and True  and False)  # 全部为真才为真，有一个假就为假
print("n00n3" and "no") # 短路运算
print('' and 'hi')
# or
print(True or True or False)
print("n00n3" or "")
print(2024 or 2025 or 2026)
print(0 or '' or 123456)
# not
print(not True)
print(not 1)
print(not '')
# 优先级 not > and > or
print(True and False and not False)
print(True or False and True or False)