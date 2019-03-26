"""小雪人滑雪游戏"""
import pygame as pg
import random
pg.init()


class Game(object):
    def __init__(self, win_x, win_y, title):
        self.win_x = win_x      #窗口宽
        self.win_y = win_y      #窗口高
        self.window = pg.display.set_mode((self.win_x, self.win_y))
        pg.display.set_caption(title)   #设置窗口标题

    def win_bk_color(self, color):
        """设置游戏窗口背景颜色、标题和尺寸"""
        self.window.fill([color[0], color[1], color[2]])

    def win_music(self, music_path):
        """设置游戏音乐"""
        pg.mixer.music.load(music_path)
        if pg.mixer.music.get_busy() == False:
            pg.mixer.music.play()

    def game_over(self):
        """结束游戏"""
        ret = pg.event.get()
        for obj in ret:
            if obj.type == pg.QUIT:
                print("shut down the window.")
                exit()


class Tree(object):
    def __init__(self, window, win_x, win_y):
        self.window = window
        self.win_x = win_x
        self.win_y = win_y

    def display_tree(self, tree_path, tree_pic_x):
        """
        显示一棵树
        :param tree_path: 数图片的路径
        """
        tree_y = self.win_y-50
        tree_x = random.randint(0, self.win_x - tree_pic_x)
        tree = pg.image.load(tree_path)
        self.window.blit(tree, (tree_x, tree_y))


class Skier(object):
    def __init__(self, window, win_x, win_y):
        self.skier_x = (win_x - 30)//2     #雪人初始位置x（30为雪人初始图片的宽度）
        self.skier_y = 0            #雪人位置y
        self.win_x = win_x          #游戏窗口x
        self.win_y = win_y          #游戏窗口y
        self.window = window        #游戏窗口
        self.skier_speed = 0.3      #雪人速度

    def display_skier(self, skier_pic_path):
        """
        显示雪人
        :param skier_pic_path: 雪人图片路径
        """
        skier = pg.image.load(skier_pic_path).convert()
        self.window.blit(skier, (self.skier_x, self.skier_y))

    def skier_down(self, skier_pic_path, skier_pic_y):
        """
        雪人向下移动
        :param skier_pic_path: 雪人图片路径
        :param skier_pic_y: 雪人图片高度
        """
        self.skier_y += self.skier_speed
        if self.skier_y >= self.win_y - skier_pic_y:
            self.skier_y = self.win_y - skier_pic_y
        self.display_skier(skier_pic_path)

    def skier_up(self, skier_pic_path):
        """
        雪人向上移动
        :param skier_pic_path: 雪人图片路径
        """
        self.skier_y -= self.skier_speed
        if self.skier_y <= 0:
            self.skier_y = 0
        self.display_skier(skier_pic_path)

    def skier_left(self, skier_pic_path):
        """
        雪人向左移动
        :param skier_pic_path: 雪人图片路径
        """
        self.skier_x -= self.skier_speed
        if self.skier_x <= 0:
            self.skier_x = 0
        self.display_skier(skier_pic_path)

    def skier_right(self, skier_pic_path, skier_pic_x):
        """
        雪人向右移动
        :param skier_pic_path:雪人图片路径
        :param skier_pic_x:雪人图片宽度
        """
        self.skier_x += self.skier_speed
        if self.skier_x >= self.win_x - skier_pic_x:
            self.skier_x = self.win_x - skier_pic_x
        self.display_skier(skier_pic_path)


if __name__ == '__main__':
    game = Game(600, 650, "ski game")   #创建游戏
    skier = Skier(game.window, game.win_x, game.win_y)         #创建雪人
    tree = Tree(game.window, game.win_x, game.win_y)       #创建一棵树

    while 1:
        game.win_bk_color([200, 255, 200])
        # game.win_music("./music/bg_music.mp3")
        # skier.display_skier("./pictures/skier_down.png")
        tree.display_tree("./pictures/skier_tree.png", 42)

        keystatus = pg.key.get_pressed()  # 检查键盘所有按键的状态（布尔型）

        if keystatus[pg.K_DOWN] or keystatus[pg.K_s]:
            skier.skier_down("./pictures/skier_down.png" , 64)
        if keystatus[pg.K_UP] or keystatus[pg.K_w]:
            skier.skier_up("./pictures/skier_down.png")
        if keystatus[pg.K_LEFT] or keystatus[pg.K_a]:
            skier.skier_left("./pictures/skier_left2.png")
        elif keystatus[pg.K_RIGHT] or keystatus[pg.K_d]:
            skier.skier_right("./pictures/skier_right2.png", 44)
        else:
            skier.display_skier("./pictures/skier_down.png")

        game.game_over()
        pg.display.update()




