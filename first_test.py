#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 15:32
# @Author  : NCP
# @File    : first_test.py
# @Software: PyCharm


import sys
import pygame

from settings import Setting
from ship import Ship
from game_src import game_functions as gf

def run_game():
    #初始化
    pygame.init()

    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion....打飞机")

    # # 设置背景颜色
    # bg_color = (230,230,230)

    ship = Ship(ai_settings, screen)

    # 开始游戏循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ship)
        # 添加移动接口
        ship.update()

        gf.update_screen(ai_settings,screen,ship)

run_game()
