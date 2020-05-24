class Settings():
    """存储外星人所有设置的类"""

    def __init__(self):
        """初始化游戏设置"""
        # 屏幕设置
        self.screen_width = 1000
        self.screen_height = 700
        self.bg_color = (230, 230, 230)

        # 飞船的设置
        self.ship_speed_factor = 1.5

        # 子弹的设置
        self.bullet_speed_factor = 1
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 100

        # 外星人设置
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        # fleet_direction 为1时表示向右移动，为-1时表示向左移动
        self.fleet_direction = 1
