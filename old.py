import pygame as pg

# pg.mixer.init()     #音乐播放模块初始化
pg.init()     #音乐播放模块初始化

#游戏窗口设置
win_x = 600     #游戏窗口宽度
win_y = 650     #游戏窗口高度
#雪人图片大小
skier_picture_x = 30
skier_picture_y = 64
#雪人位置
skier_x = (win_x - skier_picture_x)//2
skier_y = 0
#雪人移动速度
skier_speed = 0.1

#绘制游戏窗口
window = pg.display.set_mode((win_x, win_y))

pg.display.set_caption("ski game")          #窗口标题
# image = pg.image.load("./pictures/ddd.jpg").convert() #背景图片
# window.fill([245, 245, 245])                 #窗口背景填充
skier = pg.image.load("./pictures/skier_down.png").convert()  #雪人图片

pg.mixer.music.load("./musics/bg_music.mp3")     #背景音乐
# pg.draw.circle(window, [0,0,0],[60,60],30, 2)     #画个圆
# window.blit(image, (0, 0))      #游戏窗口显示
# window.blit(skier, (skier_x, skier_y))

# print(window.get_height())
# print(window.get_width())
while 1:
    # window.blit(image, (0, 0))      #游戏窗口显示
    window.fill([0, 255, 0])
    window.blit(skier, (skier_x, skier_y))    #初始位置雪人显示

    ret = pg.event.get()

    keystatus = pg.key.get_pressed()  # 检查键盘所有按键的状态（布尔型）

    # 播放音乐
    if pg.mixer.music.get_busy() == False:
        pg.mixer.music.play()

    #退出游戏
    for obj in ret:
        if obj.type == pg.QUIT:
            print("shut down the window.")
            exit()

    #雪人向下移动
    if keystatus[pg.K_DOWN] or keystatus[pg.K_s]:
        skier_y += skier_speed
        if skier_y >= win_y - skier_picture_y:
            skier_y = win_y - skier_picture_y
        window.blit(skier, (skier_x, skier_y))
    #雪人向上移动
    if keystatus[pg.K_UP] or keystatus[pg.K_w]:
        skier_y -= skier_speed
        if skier_y <= 0:
            skier_y = 0
        window.blit(skier, (skier_x, skier_y))
    #雪人向左移动
    if keystatus[pg.K_LEFT] or keystatus[pg.K_a]:
        skier_x -= skier_speed
        if skier_x <= 0:
            skier_x = 0
        window.blit(skier, (skier_x, skier_y))
    #雪人向右移动
    if keystatus[pg.K_RIGHT] or keystatus[pg.K_d]:
        skier_x += skier_speed
        if skier_x >= win_x - skier_picture_x:
            skier_x = win_x - skier_picture_x
        window.blit(skier, (skier_x, skier_y))

    pg.display.update()     #刷新

