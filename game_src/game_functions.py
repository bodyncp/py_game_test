#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 14:28
# @Author  : NCP
# @File    : game_functions.py
# @Software: PyCharm


import sys
import pygame


def check_keydown_events(event, ship):
    """
    按键响应
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_d:
        ship.moving_right = True
    elif event.key == pygame.K_a:
        ship.moving_left = True
    elif event.key == pygame.K_w:
        ship.moving_top = True
    elif event.key == pygame.K_s:
        ship.moving_bottom = True


def check_keyup_events(event, ship):
    """
    松开按键
    :param event:
    :param ship:
    :return:
    """
    if event.key == pygame.K_d:
        ship.moving_right = False
    elif event.key == pygame.K_a:
        ship.moving_left = False
    elif event.key == pygame.K_w:
        ship.moving_top = False
    elif event.key == pygame.K_s:
        ship.moving_bottom = False


def check_events(ship):
    """
    响应按键和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, ship):
    # 每次循环都检测窗口背景
    screen.fill(ai_settings.bg_color)

    # 循环刷新飞船
    ship.blitme()

    # 让最近绘制的屏幕可见
    pygame.display.flip()
