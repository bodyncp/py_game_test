#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/10/31 14:28
# @Author  : NCP
# @File    : game_functions.py
# @Software: PyCharm


import sys
from time import sleep
import pygame
from bullet import Bullet
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, bullets):
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
    elif event.key == pygame.K_SPACE:
        # 创建一棵子弹，并加入到编组bullets中,这里限制了子弹数
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


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


def check_events(ai_settings, screen, ship, bullets):
    """
    响应按键和鼠标事件
    :return:
    """
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(ai_settings, screen, stats, ship, aliens, bullets, button):
    # 每次循环都检测窗口背景
    screen.fill(ai_settings.bg_color)

    # 如果游戏待机就出现play按钮
    if not stats.game_active:
        button.draw_button()

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 循环刷新飞船和外星人
    ship.blitme()
    aliens.draw(screen)

    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):
    """
    更新子弹的位置，并删除已消失的子弹
    :param bullets:
    :return:
    """
    # 更新子弹的位置
    # 添加子弹移动接口
    bullets.update()
    # 删除消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)

    # 检测是否有子弹击中飞船，击中则删除飞船和子弹
    check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets)


def check_bullet_alien_collisions(ai_settings, screen, ship, aliens, bullets):
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    if len(aliens) == 0:
        # 删除现有的子弹并删除外星人
        bullets.empty()
        create_fleet(ai_settings, screen, ship, aliens)


def fire_bullet(ai_settings, screen, ship, bullets):
    """
    如果没到达限制就发射子弹
    :param ai_settings:
    :param screen:
    :param ship:
    :param bullets:
    :return:
    """
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, ship, aliens):
    """
    创建外星人群
    :param ai_settings:
    :param screen:
    :param aliens:
    :return:
    """
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)

    for row_number in range(number_rows):
        for alien_number in range(number_aliens_x + 1):
            number_rows = number_rows
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def get_number_aliens_x(ai_settings, alien_width):
    """
    计算每行可容纳的外星人
    :param ai_settings:
    :param alien_width:
    :return:
    """
    # 设置外形飞机个数和间距
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - (3 * alien_height) - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """
    更新外星飞船的位置
    :param aliens:
    :return:
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星飞船和自己飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                break
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    """
    有飞船到达边缘时，采取措施
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """
    将整对人下移，并改变方向
    :param ai_settings:
    :param aliens:
    :return:
    """
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """
    响应被外星人飞船装击的飞船
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    if stats.ships_left > 0:
        # 将ship_left减1
        stats.ships_left -= 1

        # 清空外星飞船列表和子弹列表
        aliens.empty()
        bullets.empty()

        sleep(1)
        # 创建一群外星飞船， 并放置在屏幕底端中央
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """
    检测是否有外星人飞船触底
    :param ai_settings:
    :param stats:
    :param screen:
    :param ship:
    :param aliens:
    :param bullets:
    :return:
    """
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 以飞船被撞为原型处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break



