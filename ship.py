#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/30 16:20
# @Author  : NCP
# @File    : ship.py
# @Software: PyCharm

import pygame


class Ship():

    def __init__(self, ai_settigs, screen):
        """
        初始化飞船并设置初始位置
        """
        self.screen = screen
        self.ai_settings = ai_settigs
        self.image_file = 'game_img/ship.bmp'

        # 加载飞机图像并获取外接矩形
        self.img = pygame.image.load(self.image_file)
        # 修改图片大小
        self.img = pygame.transform.scale(self.img, (80, 60))
        self.rect = self.img.get_rect()
        self.screen_rect = screen.get_rect()

        # 将每艘飞船放置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 允许飞船移动
        # 1.设置移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_top = False
        self.moving_bottom = False

        # 存储左右最小的移动值
        self.center = float(self.rect.centerx)
        self.updown = float(self.rect.bottom)

    def update(self):
        """
        定义飞船移动功能，根据移动标志调整飞船位置
        :return:
        """
        # 限制飞船移动范围不能超出屏幕
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor
        if self.moving_top and self.rect.bottom > self.rect.height:
            self.updown -= self.ai_settings.ship_speed_factor
        if self.moving_bottom and self.rect.bottom < self.screen_rect.height:
            self.updown += self.ai_settings.ship_speed_factor

        # 根据self.centerx更新rect对象(self.rect.centerx用于记录飞船位置)
        self.rect.centerx = self.center
        self.rect.bottom = self.updown

    def blitme(self):
        """
        在指定位置绘制飞船
        :return:
        """
        self.screen.blit(self.img, self.rect)

    def center_ship(self):
        """
        让飞船在屏幕上居中
        :return:
        """
        self.center = self.screen_rect.centerx
        self.updown = self.screen_rect.bottom

