#!/usr/bin/env python
# coding=utf-8


# 用函数实现输入某年某月某日，判断这一天是这一年的第几天？闰年情况也考虑进去
LeapYear   = [31,28,31,30,31,30,31,31,30,31,30,31]
CommonYear = [31,28,31,30,31,30,31,31,30,31,30,31]


def isLeapYear(year):
    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        return True
    else:
        return False

# 计算天数
def CaclDay(year,month,day):
    sum = 0
    j = 0
    if isLeapYear(year) == True:
        while j<month-1:
            sum += LeapYear[j]
            j += 1
    else:
         while j<month-1:
            sum += CommonYear[j]
            j += 1
    sum += day
    return sum

# 获取年月日
def get_year_mon_day(time):
    global year
    global month
    global day
    year=int(time[0:4])    
    month=int(time[4:6])
    day=int(time[6:8])


#year = int(input("请输入年："))
#month = int(input("请输入月："))
#day = int(input("请输入日："))

year = 0
month = 0
day = 0

# 输入年月日
time = input("请输入年月日:")

get_year_mon_day(time)

sum = CaclDay(year,month,day)
print("%d 年 %d 月 %d 日 是 %d 年中的第 %d 天"%(year,month,day,year,sum))
