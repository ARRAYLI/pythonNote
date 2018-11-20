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


# 打印功能提示

print("="*50)
print("                      名片管理器 V8.6")
print("     1.添加一个新的名片")
print("     2.删除一个名片")
print("     3.修改一个名片")
print("     4.查询一个名片")
print("     5.显示所有名片")
print("     6.退出名片管理器系统")
print("="*50)

# 定义一个空的列表用来存储添加的名字

card_infors = []

while True:
    # 获取用户的选择
    num = int(input("请输入功能序号："))
    
    # 根据用户的选择，执行相应的功能

    if num == 1:
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

        # 将一个字典添加到列表中
        card_infors.append(new_infor)
        #names.append(new_name)
        #print(names)
    elif num == 2:
        # 删除一个名片
        '''
        del_name = input("请输入您要删除的名片的姓名:")
        card_infors.remove(del_name)
        '''
    elif num == 3:
        # 修改一个名片
        pass
    elif num == 4:
        find_name = input("请输入一个你要查询的名字:")
        find_flag = 0   # 默认表示没有找到
        for temp in card_infors:
            if find_name == temp['name']:
                print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['address']))
                find_flag = 1       # 找到了
                break;
        if find_name == 0:
            print("查无此人")
    elif num == 5:
        print("姓名\tQQ\t微信\t住址")
        for temp in card_infors:
                print("%s\t%s\t%s\t%s"%(temp['name'],temp['qq'],temp['weixin'],temp['address']))
    elif num == 6:
        break
    else:
        print("您的输入有误，请重新输入")
print("")


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
