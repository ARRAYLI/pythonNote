#!/usr/bin/env python
# coding=utf-8

import pygame

import time

from pygame.locals import *

def main():
    """整个程序的的框架"""
    # 1.创建一个窗口来显示屏幕
    screen = pygame.display.set_mode((480,700),
0,32)
    # 2.创建一个和窗口大小的图片，用来当作背景
    background = pygame.image.load("./feiji/background.png")

    # 3.创建一个飞机图片
    hero = pygame.image.load("./feiji/hero1.png")
    
    x = 210
    y = 500


    while True:
        screen.blit(background,(0,0))

        screen.blit(hero,(x,y))


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
                    x -= 5
                    print('left')
                elif event.key == K_d or event.key == K_RIGHT:
                    x += 5
                    print('right')
                    #检测按键是否是空格键
                elif event.key == K_SPACE:
                    print('space')

            pygame.display.update()

        time.sleep(0.01)

if __name__ == '__main__':
    main()
