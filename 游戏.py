import pygame
import random
pygame.init()

window = pygame.display.set_mode((640,600))
window.fill([255, 255, 255]) # rgb 值


class SkierClass(pygame.sprite.Sprite):
    '''实现精灵类的继承，完成滑雪小人的写成'''
    def __init__(self,image,location,speed):
        '''
        :param image: 指的是图片的路径
        :param location: 列表类型的属性，[x横轴坐标，y纵轴坐标]
        :param speed: 列表类型，[横轴的速度,纵轴的速度]
        '''
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image) #<Surface(30x64x32 SW)>，加载雪人的状态图像
        self.rect = self.image.get_rect() #<rect(0, 0, 30, 64)> # 获取图像边界的矩形
        self.rect.left = location[0]
        self.rect.top = location[1] #设置图像的初始位置
        # self.rect.left,self.rect.top = location
        self.speed = speed

    def move(self):
        '''这个方法实现了小人的移动，利用的是rect内置的move方法'''
        retdata = self.rect.move(self.speed)
        print('move方法的返回值',retdata)
        self.rect = retdata
        if self.rect.left < 0 or self.rect.right > 640:
            self.speed[0] = -self.speed[0]
        if self.rect.top < 0 or self.rect.bottom >600:
            self.speed[1] = -self.speed[1]


if __name__ == '__main__':

    # 创建单个小人实例

    ski = SkierClass('./pic/skier_down.png', [500, 100],[0,1])


    #
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('关闭窗口')
                exit()
        window.fill([255,255,255]) #创建一个新背景，掩饰之前出现的遗留图像的问题
        ski.move()
        window.blit(ski.image,ski.rect) #将图像添加到窗口显示

        pygame.display.update()