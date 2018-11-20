#!/usr/bin/env python
# coding=utf-8

import pygame
import time
from pygame.locals import *


# 飞机类
class HeroPlane(object):
    def __init__(self,screen_temp):
        self.x = 210
        self.y = 500
        self.image = pygame.image.load("./feiji/hero1.png")
        self.screen = screen_temp

    def display(self):
        self.screen.blit(self.image,(self.x,self.y))
    
    def move_left(self):
        self.x -= 5

    def move_right(self):
        self.x += 5
    

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
                hero_temp.move_left()
                print('left')
            elif event.key == K_d or event.key == K_RIGHT:
                hero_temp.move_right()
                print('right')
                #检测按键是否是空格键
            elif event.key == K_SPACE:
                print('space')


def main():
    """整个程序的的框架"""
    # 1.创建一个窗口来显示屏幕
    screen = pygame.display.set_mode((480,700),
0,32)
    # 2.创建一个和窗口大小的图片，用来当作背景
    background = pygame.image.load("./feiji/background.png")

    # 3.创建一个飞机图片
    hero = HeroPlane(screen)    

    while True:
        screen.blit(background,(0,0))
        hero.display()
        keyControl(hero) 
        pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()
