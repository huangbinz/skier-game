import pygame
import random
pygame.init()


class Skier(pygame.sprite.Sprite):
    """创建滑雪小人"""
    def __init__(self, image, location, speed, window):
        """
        :param image: 字典类型，值分别为down,left,right,leftdown,rightdown,
                        值为相应图片的路径
        :param location: 图片的初始位置
        :param speed: 雪人的移动速度
        :param window: 游戏窗口
        """
        super().__init__()
        #加载雪人图片
        self.image = {}
        for key,value in image.items():
            self.image[key] = pygame.image.load(image[key])

        self.rect = self.image["down"].get_rect()
        self.rect.center = location
        self.speed = speed
        self.window = window

    def move(self):
        """通过键盘控制对象的移动"""
        keystatus = pygame.key.get_pressed()

        # 左下（必须在前面）
        if keystatus[pygame.K_DOWN] and keystatus[pygame.K_LEFT] or \
                keystatus[pygame.K_s] and keystatus[pygame.K_a]:
            self.rect.centery += self.speed[1]
            self.rect.centerx -= self.speed[0]
            if self.rect.centery > self.window.get_height() - self.image[
                "down"].get_height() // 2:
                self.rect.centery = self.window.get_height() - self.image[
                    "down"].get_height() // 2
            self.window.blit(self.image["leftdown"], self.rect)
        # 右下（必须在前面）
        elif keystatus[pygame.K_DOWN] and keystatus[pygame.K_RIGHT] or \
                keystatus[pygame.K_s] and keystatus[pygame.K_d]:
            self.rect.centery += self.speed[1]
            self.rect.centerx += self.speed[0]
            if self.rect.centery > self.window.get_height() - self.image[
                "down"].get_height() // 2:
                self.rect.centery = self.window.get_height() - self.image[
                    "down"].get_height() // 2
            self.window.blit(self.image["rightdown"], self.rect)
        #左移，方向左键或者按键a
        elif keystatus[pygame.K_LEFT] or keystatus[pygame.K_a]:
            self.rect.centerx -= self.speed[0]
            if self.rect.centerx < self.image["left"].get_width()//2:
                self.rect.centerx = self.image["left"].get_width()//2
            self.window.blit(self.image["left"], self.rect)
        #右移，方向右键或者按键d
        elif keystatus[pygame.K_RIGHT] or keystatus[pygame.K_d]:
            self.rect.centerx += self.speed[0]
            if self.rect.centerx > self.window.get_width() - self.image["right"].get_width()//2:
                self.rect.centerx = self.window.get_width() - self.image["right"].get_width()//2
            self.window.blit(self.image["right"], self.rect)
        #下移，方向下键或者按键s
        elif keystatus[pygame.K_DOWN] or keystatus[pygame.K_s]:
            self.rect.centery += self.speed[1]
            if self.rect.centery > self.window.get_height() - self.image["down"].get_height()//2:
                self.rect.centery = self.window.get_height() - self.image["down"].get_height()//2
            self.window.blit(self.image["down"], self.rect)
        #上移，方向上键或者按键w
        elif keystatus[pygame.K_UP] or keystatus[pygame.K_w]:
            self.rect.centery -= self.speed[1]
            if self.rect.centery < self.image["down"].get_height()//2:
                self.rect.centery = self.image["down"].get_height()//2
            self.window.blit(self.image["down"], self.rect)
        else:
            self.window.blit(self.image["down"], self.rect)


class FlagTree(pygame.sprite.Sprite):
    """创建一个旗帜或树"""
    def __init__(self, image, location, speed, type):
        """
        :param image: 图片路径
        :param location: 图片的初始位置
        :param speed: 对象的移动速度
        """
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = location
        self.speed = speed
        self.passed = False     #检测精灵是否和其它精灵碰撞过
        self.type= type

    def update(self):
        """自动移动树和小旗"""
        self.rect.centery -= self.speed
        if self.rect.centery < -self.image.get_height()//2:
            self.kill()


def create_tree_flag(window, num, speed, type):
    """
    创建树和旗帜对象
    :param window: 游戏窗口
    :param num: 创建树和旗帜的个数
    :param speed: 树和旗帜移动的速度
    :param type: 判断需要创建的对象类型，树或者小旗
    """
    global group
    locate_list = []

    for i in range(num):
        m = random.randint(21, window.get_width()-21)
        n = random.randint(window.get_height()+24, 2*window.get_height())
        if [m, n] not in locate_list:
            locate_list.append([m, n])
            type = random.choice(["tree", "flag"])
            if type == "tree":
                image_path = "./pictures/skier_tree.png"
            else:
                image_path = "./pictures/skier_flag.png"
            obj = FlagTree(image_path, [m, n], speed, type)
            group.add(obj)


if __name__ == '__main__':
    tree_flag_speed = 1     #树和旗帜的速度
    position = 0    #下层屏幕的初始位置
    score = 0   #得分

    #绘制游戏窗口
    window = pygame.display.set_mode((600, 650))
    window.fill([255, 255, 255])

    #音乐
    pygame.mixer.music.load("./musics/bg_music.mp3")    #背景音乐
    sound_tree = pygame.mixer.Sound("./musics/hit_paddle.wav")   #撞树音乐
    sound_flag = pygame.mixer.Sound("./musics/new_life.wav")

    group = pygame.sprite.Group()       # 创建一个组对象，树
    create_tree_flag(window, 15, tree_flag_speed, "tree")      #创建树和小旗

    #创建雪人
    skier_image = {"down": "./pictures/skier_down.png",
                   "left": "./pictures/skier_left2.png",
                   "right": "./pictures/skier_right2.png",
                   "leftdown": "./pictures/skier_left1.png",
                   "rightdown": "./pictures/skier_right1.png"
                   }
    skier = Skier(skier_image, [window.get_width()//2, 30], [1, 1], window)

    #得分显示
    font = pygame.font.Font(None, 50)

    # 设置帧,创建了一个时间对象
    clock = pygame.time.Clock()

    while 1:
        window.fill([255, 255, 255])
        clock.tick(150)     #屏幕刷新帧数，可调整游戏速度

        #音乐
        if pygame.mixer.music.get_busy() == False:
            pygame.mixer.music.play()

        #移动雪人
        skier.move()

        position += tree_flag_speed
        if position >= window.get_height():
            create_tree_flag(window, 15, tree_flag_speed, type)
            position = 0

        #刷新树和小旗
        group.update()
        group.draw(window)

        #碰撞检测
        return_list = pygame.sprite.spritecollide(skier, group, False)
        if return_list:
            """雪人和树发生碰撞"""
            if return_list[0].type == "tree" and not return_list[0].passed:
                score -= 100
                return_list[0].passed = True
                crash_image = pygame.image.load("./pictures/skier_crash.png")
                window.fill([255,255,255])
                group.draw(window)
                window.blit(score_text, [0, 0])
                window.blit(crash_image, skier.rect)
                pygame.display.flip()
                sound_tree.play()       #播放撞树的音乐
                pygame.time.delay(500)
            elif return_list[0].type == "flag":
                """雪人和小旗发生碰撞"""
                return_list[0].kill()
                score += 10
                sound_flag.play()       #播放拾到小旗的音乐

        #显示得分
        score_text = font.render(("score:" + str(score)), True, (0, 0, 255))
        window.blit(score_text, [0, 0])

        #结束游戏
        for obj in pygame.event.get():
            if obj.type == pygame.QUIT:
                exit()

        pygame.display.update()     #刷新屏幕
