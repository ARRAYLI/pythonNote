#!/usr/bin/env python
# coding=utf-8


def is_in_range():
    index = input('请选择要(修改)删除的学员序号：')
    index = int(index)
    while index not in range(0, len(student_list)):
        index = input('您输入的序号不在范围内，请重新输入：')
        index = int(index)
    return index
def add_stu():
    name = input('请输入姓名：')
    age = input('请输入年龄：')
    sex = input('请输入性别：')
    person_list = [name, age, sex]
    student_list.append(person_list)
    print('添加成功！')
def alter_stu():
    index=is_in_range()
    person = student_list[index]
    name = person[0]
    age = person[1]
    sex = person[2]
    student_list[index][0] = input('请输入修改后的姓名：(%s):' % name)
    student_list[index][1] = input('请输入修改后的年龄：(%s):' % age)
    student_list[index][2] = input('请输入修改后的性别：(%s)' % sex)
    print('修改成功！')
def see_stu():
    for x in range(0, len(student_list)):
        person = student_list[x]
        name = person[0]
        age = person[1]
        sex = person[2]
        print('序号：%s 姓名：%s 年龄:%s  性别:%s ' % (x, name, age, sex))
def del_stu():
    print('1.删除所有学员')
    print('2.删除选择的学员')
    num = input('请输入您的选择：')
    if num == '1':
        student_list.clear()
    else:
        index = is_in_range()
        del student_list[index]
#声明保存数据的函数
def save_data():
    #1.打开文件
    file_handle=open('student_v2.txt',mode='w')
    #2.for循环遍历大列表
    for student in student_list:
        #把列表中的数据用空格分开拼接成一个字符串
        s=' '.join(student)
        #写入
        file_handle.write(s)
        file_handle.write('\n')
    #3.关闭文件
    file_handle.close()
#引入os模
import os
#读取文件的函数
def read_data():
    #判断文件是否存在
    rs=os.path.exists('student_v2.txt')
    if rs==True:
        #1.打开文件
        file_handle=open('student_v2.txt',mode='r')
        #2.取出信息
        contents=file_handle.readlines()
        print(contents)
        for content in contents:
            #去除/n
            content=content.strip('\n')
            #使用空格分割字符串，得到列表
            list_1=content.split(' ')
            #将小列表添加到大列表中
            student_list.append(list_1)
        # 3.关闭文件
        file_handle.close()
# 声明一个大列表，存放学院的姓名
student_list = []
read_data()
while True:
    print('1.添加学员')
    print('2.修改学员')
    print('3.查询学员')
    print('4.删除学员')
    print('0.退出程序')
    sel_num = input('请输入您要进行的操作：')
    sel_num = int(sel_num)
    # 如果选择的数字不在0~5 继续选择
    while sel_num not in range(0, 5):
        sel_num = input('您的选择无效，请重新选择：')
        sel_num = int(sel_num)
    # 添加学员
    if sel_num == 1:
        add_stu()
        save_data()
    elif sel_num == 2:
        # 1.展示所有学员信息
        see_stu()
        # 2.选择要修改的学员序号
        alter_stu()
        save_data()
    elif sel_num == 3:
        see_stu()
    elif sel_num == 4:
        see_stu()
        # 2.选择要删除的学员序号
        del_stu()
        save_data()
    else:
        break
        
