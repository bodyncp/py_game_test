#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 15:32
# @Author  : NCP
# @File    : alien_invasion.py
# @Software: PyCharm


import sys
import pygame

from settings import Setting
from ship import Ship
from button import Button
from game_stats import GameStats
from game_src import game_functions as gf
from pygame.sprite import Group
from alien import Alien


def run_game():
    # 初始化
    pygame.init()

    ai_settings = Setting()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height)
    )

    pygame.display.set_caption("Alien Invasion....打飞机")

    # # 设置背景颜色
    # bg_color = (230,230,230)
    # 创建飞船
    ship = Ship(ai_settings, screen)

    # 创建外星人
    alien = Alien(ai_settings, screen)

    # 创建一个用于存储子弹的编组和外星人组
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 创建按钮
    button = Button(ai_settings, screen, "Play")

    # 创建一个用户存储游戏统计信息的实例
    stats = GameStats(ai_settings)

    # 开始游戏循环
    while True:
        # 监视键盘和鼠标事件
        gf.check_events(ai_settings, screen, ship, bullets)
        if stats.game_active:
            # 添加飞船移动接口
            ship.update()
            gf.update_bullets(ai_settings, screen, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            # print(len(bullets))  # 查看子弹是否删除
        else:
            # 创建按钮
            button = Button(ai_settings, screen, "you are lower")
            button.draw_button()
        # 更新飞船位置
        gf.update_screen(ai_settings, screen, stats, ship, aliens, bullets, button)


run_game()
