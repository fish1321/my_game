import pygame
import math

# 初始化 pygame
pygame.init()

# 设置窗口尺寸
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("Rotating Sprite")

# 定义颜色
WHITE = (255, 255, 255)
RED = (255, 0, 0)
TRANSPARENT = (0, 0, 0, 0)  # 定义透明的颜色

# 创建透明的Surface用于绘制轨迹
trail_surface = pygame.Surface((win_width, win_height), pygame.SRCALPHA)

# 加载精灵图像
sprite_image = pygame.Surface((50, 50), pygame.SRCALPHA)  # 使用透明的Surface作为精灵的图像
pygame.draw.rect(sprite_image, RED, (0, 0, 50, 50))

# 初始位置和旋转角度
x = 100
y = 100
theta = 45

# 动物身体的长度和宽度
length = 50
width = 30

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 清空屏幕
    win.fill(WHITE)
    trail_surface.fill(TRANSPARENT)  # 每次循环前清空轨迹Surface

    # 旋转角度
    theta += 0.01
    if theta >= 360:
        theta = 0

    # 计算新位置
    x_new = x + length * math.cos(math.radians(theta)) - width * math.sin(math.radians(theta))
    y_new = y + length * math.sin(math.radians(theta)) + width * math.cos(math.radians(theta))

    # 画出轨迹
    pygame.draw.circle(trail_surface, (255, 0, 0, 50), (int(x_new), int(y_new)), 5)

    # 渲染轨迹
    win.blit(trail_surface, (0, 0))

    # 旋转精灵并渲染在新位置
    rotated_sprite = pygame.transform.rotate(sprite_image, -theta)
    win.blit(rotated_sprite, (x_new, y_new))

    # 更新窗口
    pygame.display.flip()

pygame.quit()
