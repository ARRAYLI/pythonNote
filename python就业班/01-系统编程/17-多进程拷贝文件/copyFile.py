#!/usr/bin/env python
# coding=utf-8

from multiprocessing import Pool,Manager
import os 


def copyFileTask(name,oldFolderName,newFolderNmae,queue):
    "完成拷贝一个文件的功能"
    fr = open(oldFolderName+"/"+name)
    fw = open(newFolderNmae+"/"+name,"w")

    content = fr.read()
    fw.write(content)

    fr.close()
    fw.close()

    queue.put(name)

def main():

    # 0. 获取用户要 copy 文件夹的名字
    oldFolderName = input("请输入文件夹的名字:")

    # 1. 创建一个文件夹
    newFolderNmae = oldFolderName + "-复件"

    #print(newFolderNmae)
    os.mkdir(newFolderNmae)

    # 2. 获取old文件夹中的所有文件的名字
    fileNames = os.listdir(oldFolderName)

    #print(fileNames)

    # 3. 使用多进程的方式copy原文件夹中的所有文件到新的文件中
    pool = Pool(5)

    queue = Manager().Queue()
    for name in fileNames:
        pool.apply_async(copyFileTask,args=(name,oldFolderName,newFolderNmae,queue))

    num = 0
    allNum = len(fileNames)
    copyRate = 0
    while num<allNum:
        queue.get()
        num += 1
        copyRate = num/allNum
        print("\rcopy的进度是:%.2f%%"%(copyRate*100),end="")

    print("\n已完成 copy....") 
    

if __name__ == "__main__":
    main()

