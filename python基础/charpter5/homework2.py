#!/usr/bin/env python
# coding=utf-8

import os

info = []

file_name = "mima.txt"

# 制作一个“密码薄",其可以死存储一个网址（例如 www.itcast.cn)，和一个密码（例如12345）。
# 请编写程序完成这个密码薄的增删查改功能，并实现文件存储功能

def print_menu():
    """打印菜单"""
    print("-"*50)
    print("                 学生管理系统V1.0")
    print("         1.增加信息")
    print("         2.删除信息")
    print("         3.修改信息")
    print("         4.查找信息")
    print("         5.显示所有信息")
    print("         6.退出系统")
    print("-"*50)

def is_range():

    index = input('请选择要(修改,查找)删除的学员序号：')
    index = int(index)
    while index not in range(0, len(info)):
        index = input('您输入的序号不在范围内，请重新输入：')
        index = int(index)
    return index

def add_info():
    """添加信息""" 
    user_name = input("请您输入用户名:")
    user_passwd = input("请您输入密码:")
    
    print("user_name = %s,user_passwd = %s"%(user_name,user_passwd))
    user_info = [user_name,user_passwd]
    #user_info.append(user_name)
    #user_info.append(user_passwd)
    print(user_info)
    info.append(user_info)
    print("添加成功!")

def del_info():
    """删除信息"""
    print("1.删除所有学员")
    print("2.删除选中学员")
    num = int(input("请输入您的选择:"))
    if num == 1:
        info.clear()
    else:
        del_index = is_range()
        del info[del_index]
    print("删除成功!")

def mod_info():
    """修改学员信息"""
    index = is_range()
    person = info[index]
    name = person[0]
    pwd = person[1]
    info[index][0] = input('请输入修改后的用户名: (%s) :'%name)
    info[index][1] = input('请输入修改后的密码: (%s) :'%pwd)
    print("修改成功!")
   
def search_info():
    """查看信息"""
    index = is_range()
    person = info[index]
    name = person[0]
    pwd = person[1]
    print("序号:\t%s\t用户名:\t%s\t密码:\t%s"%(index,name,pwd))
    print("查询成功!")

def show_info():
    """显示所有学员的信息"""
    for x in range(0,len(info)):
        person = info[x]
        name = person[0]
        pwd = person[1]
        print("序号:\t%s\t用户名:\t%s\t密码:\t%s"%(x,name,pwd))
    print("显示成功!")

def save_data():
    """保存数据"""
    # 1.打开文件
    file = open(file_name,"w")
    # 2.for 循环遍历大列表 
    for x in info:
        # 把列表中的数据用空格分开并拼接成一个字符串
        s = ' '.join(x)
        # 写入文件
        file.write(s)
        # 换行
        file.write('\n')
    # 关闭文件
    file.close()

def read_data():
    """读取文件数据"""
    # 判断文件是否存在
    rs = os.path.exists(file_name)
    if rs == True:
        # 1.打开文件
        file_handle = open(file_name,"r")
        # 2.取出信息
        contents = file_handle.readlines()
        print(contents)
        for content in contents:
            # 去除 \n
            content = content.strip("\n")
            # 使用空格分割字符串得到列表
            list = content.split(' ')
            # 将小列表加到大列表中
            info.append(list)
        # 关闭文件
        file_handle.close()

def main():
    """完成整个模块"""
    print_menu()
    read_data()
    while True:
        option = int(input("请输入您的操作选项："))
        if option == 1:   # 增加信息
            add_info()
            save_data()
        elif option == 2:  # 删除信息
            del_info()
            save_data()
        elif option == 3:  # 修改信息
            mod_info()
            save_data()
        elif option == 4:  # 查找信息
            search_info()
        elif option == 5:  # 显示所有信息
            show_info()
        elif option == 6:  # 退出系统
           break
        else:
            print("您的输入有误，请重新进行输入!")

# 主程序
main()

