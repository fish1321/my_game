from 变量 import *


class miner(pygame.sprite.Sprite):
    def __init__(self):
        super(miner, self).__init__()
        self.image = pygame.image.load('assets/role/miner1.png')
        self.rect = self.image.get_rect(left=496, top=400)
        self.action = ''
        self.order = ['1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3']
        self.number = 0
        self.flip = False
        self.speed = 0
        self.blocksX, self.blocksY = 0, 128
        self.depth = 0

    def move(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.flip = True
            self.action = '_run'
            self.rect.move_ip(-8, 0)
            while pygame.sprite.spritecollide(self, blocks, False):
                self.rect.move_ip(1, 0)
                self.action = ''
        elif key[pygame.K_d]:
            self.flip = False
            self.action = '_run'
            self.rect.move_ip(8, 0)
            while pygame.sprite.spritecollide(self, blocks, False):
                self.rect.move_ip(-1, 0)
                self.action = ''
        else:
            self.action = ''
        self.rect = self.rect

    def under(self):
        key = pygame.key.get_pressed()
        self.speed += 1
        blocks.update(5)
        # ↓ ↓ ↓ ↓ ↓ ↓
        # self.rect.move_ip(0, 0 - player.speed)
        self.depth -= self.speed
        if self.speed > -1:
            while pygame.sprite.spritecollide(self, blocks, False):
                blocks.update(3)
                # ↓ ↓ ↓ ↓ ↓ ↓
                # self.rect.move_ip(0, 1)
                # player.speed = 0
                self.depth += 1
                if key[pygame.K_w]:
                    self.speed -= 14
        elif self.speed < -1:
            while pygame.sprite.spritecollide(self, blocks, False):
                blocks.update(4)
                # ↓ ↓ ↓ ↓ ↓ ↓
                # self.rect.move_ip(0, -1)
                # player.speed = 0
                self.depth -= 1

    def update(self):
        self.under()
        self.move()
        if self.speed > 1:
            self.number = 6
            self.action = '_jump'
        elif self.speed < -1:
            self.number = 0
            self.action = '_jump'
        self.image = pygame.image.load('assets/role/miner' + self.action + self.order[self.number] + '.png')
        self.image = pygame.transform.scale(self.image, (64, 68))
        self.rect.size = [32, 48]
        self.image = pygame.transform.flip(self.image, self.flip, False)
        self.number += 1
        if self.number > 12:
            self.number = 0
        if self.rect.top >= 840:
            self.rect.top = -68
            self.depth = 196
        screen.blit(self.image, (self.rect.left - 16, self.rect.top - 20))


class Block(pygame.sprite.Sprite):
    def __init__(self):
        super(Block, self).__init__()
        self.image = pygame.image.load('assets/block/stone.png')
        self.check = pygame.image.load('assets/other/check.png')
        self.rect = self.image.get_rect(left=player.blocksX, top=player.blocksY)
        self.rect.size = [64, 64]
        self.look = random.randint(1, 20)
        self.look2 = random.randint(1, 4)
        self.hardness = 0
        self.show = 1
        self.fissure = pygame.transform.scale(pygame.image.load('assets/other/fissure' + str(self.hardness) + '.png'), (64, 64))

    def update(self, a):
        x, y = pygame.mouse.get_pos()
        if a == 0:
            if self.rect.top < -128:
                self.rect.top = 768 - (-128 - self.rect.top)
                self.look = random.randint(1, 20)
                self.look2 = random.randint(1, 4)
                self.rect.size = [64, 64]
                self.show = 1
                self.hardness = 0
            if self.look < 19:
                self.look2 = 1
                self.image = pygame.image.load('assets/block/stone.png')
            else:
                self.image = pygame.image.load('assets/block/' + str(self.look2) + 'mine.png')
            if self.show == 1:
                screen.blit(self.image, self.rect)
                screen.blit(pygame.transform.scale(pygame.image.load('assets/other/fissure' + str(self.hardness) + '.png'), (64, 64)), self.rect)
            if self.rect.left <= x <= self.rect.left + 63 and self.rect.top <= y <= self.rect.top + 63:
                self.check = pygame.transform.scale(self.check, (64, 64))
                if self.show == 1:
                    screen.blit(self.check, self.rect)
        elif a == 1:
            if self.rect.left <= x <= self.rect.left + 63 and self.rect.top <= y <= self.rect.top + 63 and self.show == 1:
                self.hardness += 1
            if self.hardness >= self.look2:
                self.rect.size = [0, 0]
                self.show = 0
        elif a == 2:
            self.kill()
        elif a == 3:
            self.rect.move_ip(0, 1)
            player.speed = 0
        elif a == 4:
            self.rect.move_ip(0, -1)
            player.speed = 0
        elif a == 5:
            self.rect.move_ip(0, 0 - player.speed)


player = miner()
blocks = pygame.sprite.Group()

