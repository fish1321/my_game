from 变量 import *
import math


class abc(pygame.sprite.Sprite):
    def __init__(self):
        super(abc, self).__init__()
        self.BlockX = 0
        self.BlockY = 0
        self.ItemLook = 1
        self.Bag = []
        self.updd = False


class miner(pygame.sprite.Sprite):
    def __init__(self):
        super(miner, self).__init__()
        self.image = pygame.image.load('assets/role/miner1.png')
        self.rect = self.image.get_rect(left=496, top=400)
        self.action = ''
        self.order = ['1', '1', '1', '1', '1', '1', '1', '2', '2', '2', '2', '2', '2', '2', '3', '3', '3', '3', '3', '3', '3']
        self.number = 0
        self.flip = False
        self.speed = 0
        self.blocksX, self.blocksY = 0, 768
        self.depth = 0

    def move(self):
        key = pygame.key.get_pressed()
        x, y = pygame.mouse.get_pos()
        if key[pygame.K_a]:
            self.action = '_run'
            self.rect.move_ip(-8, 0)
            while pygame.sprite.spritecollide(self, blocks, False) or self.rect.left < 0:
                self.rect.move_ip(1, 0)
                self.action = ''
        elif key[pygame.K_d]:
            self.action = '_run'
            self.rect.move_ip(8, 0)
            while pygame.sprite.spritecollide(self, blocks, False) or self.rect.left > 992:
                self.rect.move_ip(-1, 0)
                self.action = ''
        else:
            self.action = ''
        if x > self.rect.left:
            self.flip = False
        else:
            self.flip = True

    def under(self):
        key = pygame.key.get_pressed()
        self.speed += 1
        blocks.update(5)
        # ↓ ↓ ↓ ↓ ↓ ↓
        # self.rect.move_ip(0, 0 - player.speed)
        items.update(5)
        # ↓ ↓ ↓ ↓ ↓ ↓
        # self.rect.move_ip(0, 0 - player.speed)
        self.depth -= self.speed
        if self.speed > -1:
            while pygame.sprite.spritecollide(self, blocks, False):
                blocks.update(3)
                # ↓ ↓ ↓ ↓ ↓ ↓
                # self.rect.move_ip(0, 1)
                items.update(3)
                # ↓ ↓ ↓ ↓ ↓ ↓
                # self.rect.move_ip(0, 1)
                self.speed = 0
                self.depth += 1
                if key[pygame.K_w]:
                    self.speed -= 15
        elif self.speed < -1:
            while pygame.sprite.spritecollide(self, blocks, False):
                blocks.update(4)
                # ↓ ↓ ↓ ↓ ↓ ↓
                # self.rect.move_ip(0, -1)
                items.update(4)
                # ↓ ↓ ↓ ↓ ↓ ↓
                # self.rect.move_ip(0, -1)
                self.speed = 0
                self.depth -= 1

    def update(self):
        self.under()
        self.move()
        if self.speed > 1:
            self.number = 8
            self.action = '_jump'
        elif self.speed < -1:
            self.number = 0
            self.action = '_jump'
        self.image = pygame.image.load('assets/role/miner' + self.action + self.order[self.number] + '.png')
        self.image = pygame.transform.scale(self.image, (64, 68))
        self.rect.size = [32, 48]
        self.image = pygame.transform.flip(self.image, self.flip, False)
        self.number += 1
        if self.number > 16:
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
        self.look = random.randint(1, 10)
        self.look2 = 0
        if not self.look <= 8:
            self.look2 = random.randint(1, 4)
        self.hardness = 0
        self.show = 1
        self.fissure = pygame.transform.scale(pygame.image.load('assets/other/fissure' + str(self.hardness) + '.png'), (64, 64))
        maps.append(self.look2)

    def update(self, a):
        x, y = pygame.mouse.get_pos()
        if a == 0:
            if self.rect.top < -128:
                self.rect.top = 768 - (-128 - self.rect.top)
                self.look = random.randint(1, 10)
                self.look2 = 0
                if not self.look <= 8:
                    self.look2 = random.randint(1, 4)
                self.rect.size = [64, 64]
                self.show = 1
                self.hardness = 0
                maps.append(self.look2)
            if self.show == 1:
                if self.look <= 8:
                    self.image = pygame.image.load('assets/block/stone.png')
                    self.image = pygame.transform.scale(self.image, (64, 64))
                else:
                    self.image = pygame.image.load('assets/block/' + str(self.look2) + 'mine.png')
                    self.image = pygame.transform.scale(self.image, (64, 64))
                if self.show == 1:
                    screen.blit(self.image, self.rect)
                    if ABC.updd == False:
                        items.update(0)
                    ABC.updd = True
                    if good.rob > 30 and pygame.sprite.collide_mask(self, good):
                        self.hardness += 1
                    if self.hardness >= self.look2 + 1:
                        ABC.ItemLook = self.look2
                        ABC.BlockX = self.rect.left
                        ABC.BlockY = self.rect.top
                        item = Item()
                        items.add(item)
                        self.rect.size = [0, 0]
                        self.show = 0
                    else:
                        if self.hardness != 0:
                            print(self.hardness)
                            print(self.look2 / self.hardness)
                            screen.blit(pygame.transform.scale(
                                pygame.image.load('assets/other/fissure' + str(math.ceil(5/(self.look2 / self.hardness))) + '.png'),
                                (64, 64)), self.rect)
                        else:
                            screen.blit(pygame.transform.scale(
                                pygame.image.load('assets/other/fissure0.png'),
                                (64, 64)), self.rect)
                if self.rect.left <= x <= self.rect.left + 63 and self.rect.top <= y <= self.rect.top + 63:
                    self.check = pygame.transform.scale(self.check, (64, 64))
                    if self.show == 1:
                        screen.blit(self.check, self.rect)
        elif a == 2:
            self.kill()
        elif a == 3:
            self.rect.move_ip(0, 1)
        elif a == 4:
            self.rect.move_ip(0, -1)
        elif a == 5:
            self.rect.move_ip(0, 0 - player.speed)
        elif a == 6:
            self.rect.move_ip(0, -4)


class Good(pygame.sprite.Sprite):
    def __init__(self):
        super(Good, self).__init__()
        self.image = pygame.image.load('assets/goods/tool1.png')
        self.rect = self.image.get_rect(left=player.rect.left, top=player.rect.top - 20)
        self.ro = 0
        self.rob = 0
        self.type = 1
        self.a = y - self.rect.top
        self.b = x - self.rect.left
        self.c = 0
        self.image = pygame.transform.rotate(self.image, self.ro)

    def update(self):
        x, y = pygame.mouse.get_pos()
        self.a = 0 - (y - self.rect.top)
        self.b = 0 - (x - self.rect.left)
        self.rob = abs(self.ro - math.degrees(math.atan2(-self.a, self.b)))
        self.ro = math.degrees(math.atan2(-self.a, self.b))
        self.image = pygame.image.load('assets/goods/tool' + str(self.type) + '.png')
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.image = pygame.transform.rotate(self.image, self.ro + 90)

        self.rect.left = player.rect.left + math.sqrt(32 * 32 * (abs(self.b) / (abs(self.a) + abs(self.b)))) - 20
        self.rect.top = player.rect.top + math.sqrt(32 * 32 * (abs(self.a) / (abs(self.a) + abs(self.b)))) - 20
        if self.b > 0:
            self.rect.left -= 2 * math.sqrt(32 * 32 * (abs(self.b) / (abs(self.a) + abs(self.b))))
        if self.a > 0:
            self.rect.top -= 2 * math.sqrt(32 * 32 * (abs(self.a) / (abs(self.a) + abs(self.b))))
        screen.blit(self.image, (self.rect.left, self.rect.top))


class Item(pygame.sprite.Sprite):
    def __init__(self):
        super(Item, self).__init__()
        self.image = pygame.image.load('assets/item/1mine_item.png')
        self.rect = self.image.get_rect(left=ABC.BlockX, top=ABC.BlockY)
        self.look = ABC.ItemLook
        self.speed = 0
        self.fly = 0
        self.rect.size = [64, 64]

    def update(self, a):
        key = pygame.key.get_pressed()
        if a == 0:
            self.speed += 1
            self.rect.move_ip(0, self.speed)
            while pygame.sprite.spritecollide(self, blocks, False):
                self.speed = 0
                self.rect.move_ip(0, -1)
            self.image = pygame.image.load('assets/item/' + str(self.look) + 'mine_item.png')
            self.image = pygame.transform.scale(self.image, (64, 64))
            screen.blit(self.image, (self.rect.left, self.rect.top + self.fly))
        elif a == 3:
            self.rect.move_ip(0, 1)
        elif a == 4:
            self.rect.move_ip(0, -1)
        elif a == 5:
            self.rect.move_ip(0, 0 - player.speed)


player = miner()
good = Good()
ABC = abc()
blocks = pygame.sprite.Group()
items = pygame.sprite.Group()

