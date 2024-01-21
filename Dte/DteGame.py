from 角色 import *

for i in range(0, 14):
    for j in range(0, 16):
        block = Block()
        blocks.add(block)
        player.blocksX += 64
    player.blocksX = 0
    player.blocksY += 64

while running:
    key = pygame.key.get_pressed()
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == start:
            icon = 1
    if icon == 1:
        if background[0] < 80:
            background[0] += 1
        if background[1] > 0:
            background[1] -= 0.25
        if background[2] > 0:
            background[2] -= 0.25
    if background == [80, 0, 0] or key[pygame.K_ESCAPE]:
        background = [80, 0, 0]
        break
    clock.tick(60)
    pygame.display.update()

while running:
    key = pygame.key.get_pressed()
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    if key[pygame.K_ESCAPE]:
        break
    if move < 80:
        blocks.update(6)
        move += 1
    else:
        break
    blocks.update(0)
    clock.tick(60)
    pygame.display.update()

while running:
    key = pygame.key.get_pressed()
    x, y = pygame.mouse.get_pos()
    screen.fill(background)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 4 and good.type < 2:
                good.type += 1
            if event.button == 5 and good.type > 1:
                print(111)
                good.type -= 1
    blocks.update(0)
    ABC.updd = False
    player.update()
    good.update()
    clock.tick(20)
    if key[pygame.K_f]:
        title = font.render(str(clock.get_fps()), True, (255, 255, 255))
        screen.blit(title, (10, 50))
    if key[pygame.K_c]:
        print(maps)
    title = font.render(str(player.depth), True, (255, 255, 255))
    screen.blit(title, (10, 10))
    pygame.display.update()

#                 _oo0oo_
#                o8888888o
#                88" . "88
#                (| -_- |)
#                0\  =  /0
#              ___/'___'\___
#            ,' \\|     |// ',
#           / \\|||  :  |||// \
#          / _||||| -:- |||||_ \
#         |   | \\\  _  /// |   |
#         | \_/  ''\---/''   \_/|
#         \  .-\__  '_'  __/-.  /
#       ___'. .'  /--.--\  '. .'___
#    ."" '<  '.___\_<|>_/___.' >' "".
#   | | :  '_ \'.;'\ _ /';.'/ _'  : | |
#   \  \ '_.   \_ __\ /__ _/   ._' /  /
#
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 佛祖保佑          求个点赞           永无BUG
