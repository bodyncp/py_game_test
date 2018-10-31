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

