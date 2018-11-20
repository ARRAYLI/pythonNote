#!/usr/bin/env python
# coding=utf-8

import pygame
import time
from pygame.locals import *
import random

class Base(object):
    def __init__(self,screen_temp,x,y,image):
        self.x = x 
        self.y = y
        self.image = pygame.image.load(image)
        self.screen = screen_temp

    def display(self):
        # 显示飞机
        self.screen.blit(self.image,(self.x,self.y))
        
        # 显示飞机打出去的所有子弹
        for bullet in self.bullet_list:
            bullet.display()
            bullet.move()
            if bullet.judge():  # 判断子弹是否越界
                self.bullet_list.remove(bullet)


class BasePlane(Base):
    def __init__(self,screen_temp,x,y,image):
        Base.__init__(self,screen_temp,x,y,image)
        self.bullet_list = []  # 存储发射出去的子弹的引用
    
# 飞机类
class HeroPlane(BasePlane):
    def __init__(self,screen_temp):
        # 方法一：
        BasePlane.__init__(self,screen_temp,210,500,"./feiji/hero1.png")
        # 方法二：
        #supper().__init__()
    
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
    
    def fire(self):
        self.bullet_list.append(Bullet(self.screen,self.x,self.y))


# 敌机类
class EnemyPlane(BasePlane):
    def __init__(self,screen_temp):
        BasePlane.__init__(self,screen_temp,0,0,"./feiji/enemy0.png")
        self.direction = "right"  # 使用direction 来控制飞机的方向
    
    def move(self):
        if self.direction == "right":
            self.x += 5
        elif self.direction == "left":
            self.x -= 5

        if self.x > 480-50:
            self.direction = "left"
        elif self.x <0:
            self.direction = "right"


    def fire(self):
        random_num = random.randint(1,100)
        if random_num == 8 or random_num == 90 or random_num == 60:
            self.bullet_list.append(EnemyBullet(self.screen,self.x,self.y))

class BaseBullet(object):
    def __init__(self,screen_temp,x,y,image):
        Base.__init__(self,screen_temp,x,y,image)

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))

# 子弹类
class Bullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+40,y-20,"./feiji/bullet.png")

    def move(self):
        self.y -= 10

    def judge(self):
        if self.y < 0:
            return True
        else:
            return False

# 敌机子弹类
class EnemyBullet(BaseBullet):
    def __init__(self,screen_temp,x,y):
        BaseBullet.__init__(self,screen_temp,x+25,y+40,"./feiji/bullet1.png")
    
    def move(self):
        self.y += 10

    def judge(self):
        if self.y > 700:
            return True
        else:
            return False


# 键盘控制
def keyControl(hero_temp):

    #获取事件，比如按键等
    for event in pygame.event.get():
        #判断是否是点击了退出按钮
        if event.type == QUIT:
            print("exit")
            exit()
            #判断是否是按下了键
        elif event.type == KEYDOWN:
            #检测按键是否是a或者left
            if event.key == K_a or event.key == K_LEFT:
                print('left')
                hero_temp.move_left()
            elif event.key == K_d or event.key == K_RIGHT:
                print('right')
                hero_temp.move_right()
                #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')
                hero_temp.fire()  # 开火



def main():
    """整个程序的的框架"""
    # 1.创建一个窗口来显示屏幕
    screen = pygame.display.set_mode((480,700),
0,32)
    # 2.创建一个和窗口大小的图片，用来当作背景
    background = pygame.image.load("./feiji/background.png")

    # 3.创建一个飞机图片
    hero = HeroPlane(screen)    

    # 4.创建一个敌机
    enemy = EnemyPlane(screen)

    while True:
        screen.blit(background,(0,0))
        hero.display()
        enemy.display()  # 显示敌机
        enemy.move()  # 敌机移动
        enemy.fire()  # 敌机开火
        keyControl(hero) 
        pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()
