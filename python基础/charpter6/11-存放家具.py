#!/usr/bin/env python
# coding=utf-8

class Home:

    def __init__(self,area,info,addr):
        self.area = area 
        self.info = info
        self.addr = addr
        self.left_area = area
        self.contains_items = []

    def __str__(self):
        msg = "房子总的面积是:%d,可用面积是:%d,户型是:%s,地址是：%s"%(self.area,self.left_area,self.info,self.addr)
        msg += " 当前房子里的物品有：%s"%(str(self.contains_items))
        return msg
    
    def add_item(self,item):
        #self.left_area -= item.area  
        #self.contains_items.append(item.name)
        
        self.left_area -= item.get_area()
        self.contains_items.append(item.get_name())

class Bed:

    def __init__(self,name,area):
        self.name = name
        self.area = area
    
    def __str__(self):
        return "%s 占用的面积是： %d"%(self.name,self.area)
    
    def get_area(self):
        return self.area
    
    def get_name(self):
        return self.name

fangzi = Home(130,"三室一厅","北京市朝阳区长安街666号")

print(fangzi)

bed1 = Bed("席梦思",4)
print(bed1)

fangzi.add_item(bed1)
print(fangzi)

bed2 = Bed("三人床",6)
fangzi.add_item(bed2)

print(fangzi)
