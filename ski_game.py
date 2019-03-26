import pygame as pg
import random
import time
pg.init()


class Skier(pg.sprite.Sprite):
    """创建滑雪小人"""
    def __init__(self, image, location, speed):
        """
        :param image: 图片路径
        :param location: 图片的初始位置
        :param speed: 对象的移动速度
        """
        super().__init__()
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        keystatus = pg.key.get_pressed()
        #左移
        if keystatus[pg.K_LEFT] or keystatus[pg.K_a]:
            self.rect.left -= self.speed[0]
            if self.rect.left < 0:
                self.rect.left = 0
        #右移
        if keystatus[pg.K_RIGHT] or keystatus[pg.K_d]:
            self.rect.right += self.speed[0]
            if self.rect.right > 600:
                self.rect.right = 600
        #下移
        if keystatus[pg.K_DOWN] or keystatus[pg.K_s]:
            self.rect.bottom += self.speed[1]
            if self.rect.bottom > 650:
                self.rect.bottom = 650
        #上移
        if keystatus[pg.K_UP] or keystatus[pg.K_w]:
            self.rect.top -= self.speed[1]
            if self.rect.top < 0:
                self.rect.top = 0


class FlagTree(object):
    """创建一个旗帜或树"""
    def __init__(self, image, location, speed):
        """
        :param image: 图片路径
        :param location: 图片的初始位置
        :param speed: 对象的移动速度
        """
        super().__init__()
        self.image = pg.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
        self.speed = speed

    def move(self):
        self.rect = self.rect.move(self.speed)


if __name__ == '__main__':
    def delay(num):
        """自定义延时"""
        for i in range(num):
            for j in range(10):
                pass

    window = pg.display.set_mode((600, 650))
    window.fill([255, 255, 255])

    skier = Skier("./pictures/skier_down.png", (285, 2), [1, 1])
    tree1 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree2 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree3 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree4 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree5 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree6 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree7 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    tree8 = FlagTree("./pictures/skier_tree.png", (random.randint(0, 570), random.randint(650, 1500)), [0, -1])
    flag1 = FlagTree("./pictures/skier_flag.png", (random.randint(0, 580), random.randint(650, 1200)), [0, -1])
    flag2 = FlagTree("./pictures/skier_flag.png", (random.randint(0, 580), random.randint(650, 1200)), [0, -1])
    flag3 = FlagTree("./pictures/skier_flag.png", (random.randint(0, 580), random.randint(650, 1200)), [0, -1])
    tree = [tree1, tree2, tree3,tree4,tree5,tree6,tree7,tree8]
    flag = [flag1, flag2, flag3]


    while 1:
        window.fill([255, 255, 255])

        skier.move()
        window.blit(skier.image, skier.rect)

        #树
        for i in range(8):
            tree[i].move()
            window.blit(tree[i].image, tree[i].rect)
            # time.sleep(0.00001)
            delay(1000)
            if tree[i].rect.bottom < 0:
                tree[i].rect.top = random.randint(650, 1500)
                tree[i].rect.left = random.randint(0, 570)

        #旗
        for i in range(3):
            flag[i].move()
            window.blit(flag[i].image, flag[i].rect)
            if flag[i].rect.bottom < 0:
                flag[i].rect.top = random.randint(650, 1200)
                flag[i].rect.left = random.randint(0, 570)

        #结束游戏
        for obj in pg.event.get():
            if obj.type == pg.QUIT:
                exit()
        pg.display.update()
