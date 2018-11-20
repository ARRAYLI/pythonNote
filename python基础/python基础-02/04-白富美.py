#-*- coding=utf8 -*-
#!/usr/bin/env python
# coding=utf-8


color = input("你白吗？") # 白或者黄
money = int(input("请输入你的财产总和："))  # 输入 100
beautiful = input("你美吗?")  # 美或者普通

# if 白 并且 富 并且 美：
# if 白 and 富 and 美：

if color == "白" and money > 1000000 and beautiful == "美":
    print("白富美...")
    print("白富美...")

else:
    print("矮矬穷...")

# 下面 的代码不会因为上面第13行的 if 条件满足或者不满足而一样，它们之间没有任何关系
print("矮矬穷...")
print("矮矬穷...")
print("矮矬穷...")

