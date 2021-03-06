#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/2 16:15
# @Author  : NCP
# @File    : bullet.py
# @Software: PyCharm


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """
    管理飞船发射的子弹
    """

    def __init__(self,ai_settings,screen,ship):
        """
        在飞船位置创建一个子弹对象
        :param ai_settings:
        :param screen:
        :param ship:
        """
        super(Bullet, self).__init__()
        self.screen = screen

        # 在（0,0）处创建一个表示子弹的矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width,ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # 存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """
        向上移动子弹
        :return:
        """
        # 更新表示子弹位置的小数值
        self.y -= self.speed_factor
        # 更新表示子弹位置的rect值
        self.rect.y = self.y

    def draw_bullet(self):
        """
        屏幕上绘制子弹
        :return:
        """
        pygame.draw.rect(self.screen, self.color, self.rect)
