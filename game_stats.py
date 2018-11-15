#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/15 9:40
# @Author  : NCP
# @File    : game_stats.py
# @Software: PyCharm

class GameStats():
    """
    跟踪游戏的统计信息
    """
    def __init__(self, ai_settings):
        """
        初始化统计信息
        :param ai_settings:
        """
        self.game_active = True
        self.ai_settings = ai_settings
        self.reset_stats()

    def reset_stats(self):
        """
        初始化在游戏运行期间可能变化的统计信息
        :return:
        """
        self.ships_left = self.ai_settings.ship_limit