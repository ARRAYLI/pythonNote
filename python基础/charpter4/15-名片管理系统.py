#!/usr/bin/env python
# coding=utf-8

# -*- coding:utf-8 -*-

'''
                完成一个名片管理器

    需要完成的基本功能如下：
        1、添加名片
        2、删除名片
        3、修改名片
        4、查询名片
        5、退出系统

'''
# 定义一个空的列表用来存储添加的名字

card_infors = []

def print_menu():
    """ 打印系统菜单 """
    print("="*50)
    print("                      名片管理器 V8.6")
    print("     1.添加一个新的名片")
    print("     2.删除一个名片")
    print("     3.修改一个名片")
    print("     4.查询一个名片")
    print("     5.显示所有名片")
    print("     6.退出名片管理器系统")
    print("="*50)

def add_new_card_info():
    """添加名片"""
    new_name = input("请输入您的名字：")
    new_qq = input("请输入您的 QQ:")
    new_weixin = input("请输入您的微信：")
    new_address = input("请输入您的地址: ")

    # 定义一个新的字典，用来存储一个新的名片
    new_infor = {}
    new_infor['name'] = new_name
    new_infor['qq'] = new_qq
    new_infor['weixin'] = new_weixin
    new_infor['address'] = new_address
    
    global card_infors
    # 将一个字典添加到列表中
    card_infors.append(new_infor)
    #names.append(new_name)
    #print(names)


def find_card_info():
    """用来查询一个名片"""

    global card_infors

    find_name = input("请输入一个你要查询的名字:")
    find_flag = 0   # 默认表示没有找到
    for temp in card_infors:
        if find_name == temp['name']:
            print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['address']))
            find_flag = 1       # 找到了
            break;
        if find_name == 0:
            print("查无此人")


def show_all_info():
    """ 显示所有名片的信息 """
    print("姓名\tQQ\t微信\t住址")
    for temp in card_infors:
        print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['address']))


def main():
    """完成整个程序的控制"""
    
    # 打印功能提示
    print_menu()

    while True:

        # 获取用户的选择
        num = int(input("请输入功能序号："))

         # 根据用户的选择，执行相应的功能
        if num==1:
             add_new_card_info()
        elif num == 2:
             pass
        elif num == 3:
             pass
        elif num == 4:
             find_card_info()
        elif num == 5:
             show_all_info()    
        elif num == 6:
             break
        else:
             print("您的输入有误，请重新输入")
             print("")


'''
def main():
    """完成对整个程序的控制"""
    #1. 打印功能提示
    print_menu()

    while True:

        #2. 获取用户的输入
        num = int(input("请输入操作序号:"))

        #3. 根据用户的数据执行相应的功能
        if num==1:
            add_new_card_infor()
        elif num==2:
            pass
        elif num==3:
            pass
        elif num==4:
            find_card_infor()
        elif num==5:
            show_all_infor()
        elif num==6:
            break
        else:
            print("输入有误,请重新输入")


        print("")

'''






# 调用主函数
main()


'''
# 获取用户的 输入选择

num = int(input("请输入功能序号："))

if num == 1:
    pass

elif num==2:
    pass
elif num==3:
    pass
elif num==4:
    pass
else:
    print("您的输入有误，请重新输入")

'''
