#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:01
# @Author  : NCP
# @File    : settings.py
# @Software: PyCharm


class Setting():
    """
    存储外星人游戏的所有设置
    """

    def __init__(self):
        """
        初始化游戏设置
        """
        # 屏幕设置
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (255,255,255)

        # 飞船设置移动速度为1.5像素
        self.ship_speed_factor = 0.5

        # 为创建子弹设置属性
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        # 限制子弹数量
        self.bullets_allowed = 3

        # 外星飞船属性设置
        # 移动速度
        self.alien_speed_factor = 1
        self.ship_limit = 1
        self.fleet_drop_speed = 10
        # 1表示向右移，-1表示向左移
        self.fleet_direction = 0.5



