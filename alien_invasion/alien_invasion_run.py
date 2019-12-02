import sys
import pygame
from pygame.sprite import Group

from alien_invasion.settings import Settings
from alien_invasion.ship import Ship
import alien_invasion.game_functions as gf
from alien_invasion.alien import Alien


def run_game():
    # 初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # 创建一艘飞船,一个用于存储子弹的编组，一个外星人编组
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)

    # 开始游戏主循环
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        ship.update()
        gf.update_bullets(bullets)
        gf.update_bullets(aliens)
        gf.update_screen(ai_settings, screen, ship, aliens, bullets)


if __name__ == "__main__":
    run_game()
