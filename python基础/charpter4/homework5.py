#!/usr/bin/env python
# coding=utf-8

# 编写学生管理系统

def print_menu():
    """显示菜单"""
    print("="*50)
    print("             学生管理系统1.0            ")
    print("     1.添加学生信息")
    print("     2.删除学生信息")
    print("     3.修改学生信息")
    print("     4.查询学生信息")
    print("     5.显示学生信息")
    print("     6.退出系统")
    print("="*50)

def get_optipn():
    """获取用户的菜单选项"""
    option = int(input("请输入您的选项序号:"))
    return int(option)

def add_info(stu_info):
    """添加学生信息"""
    name = input("请输入学生的姓名:")
    age = int(input("请输入学生的年龄:"))
    id = input("请输入学生的学号:")
    
    # 定义一个临时字典变量来存储学生信息
    stuInfo = {}
    stuInfo['name']=name
    stuInfo['age']=age
    stuInfo['id']=id
    stu_info.append(stuInfo)

def del_info(stu_info):
    """删除学生信息"""
    del_num = int(input("请输入要删除的学生的序号："))
    del stu_info[del_num]

def mod_info(stu_info):
    """修改学生信息"""
    mod_num = int(input("请输入要修改的序号:"))
    mod_name = input("请输入姓名：")
    mod_age = input("请输入年龄：")
    mod_id = input("请输入学号:")
    
    stu_info[mod_num]['name'] = mod_name
    stu_info[mod_num]['age'] = mod_age
    stu_info[mod_num]['id'] = mod_id

def search_info(stu_info):
    """查询学生信息"""
    search_num = int(input("请输入要查询的学生的序号:"))
    print(stu_info[search_num])

def show_info(stu_info):
    """显示所有学生信息"""
    for tmp in stu_info:
        print(tmp)


# 定义一个学生列表
stu_info = []

def main():
    """完成整个系统的功能"""
    print_menu()    # 显示菜单
    while True:
        option = get_optipn()    # 获取用户的输入选项
        if option == 1: # 添加学生信息
            add_info(stu_info)
        elif option == 2:  # 删除学生信息
            del_info(stu_info)
        elif option == 3:  # 修改学生信息
            mod_info(stu_info)
        elif option == 4:  # 查询学生信息
            search_info(stu_info)
        elif option == 5:  # 显示学生信息
            show_info(stu_info)
        elif option == 6:  # 退出系统
            break
        else:
            print("您的输入有误，请重新输入！")

# 主程序
main()

