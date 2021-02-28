import pygame
import random

display_width = 800
display_height = 600

display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Беги что бы выжить...")
icon = pygame.image.load('static/Men_black/character_malePerson_idle.png')
pygame.display.set_icon(icon)

WCR = [pygame.image.load("static/Men_black/character_malePerson_walk0.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk1.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk2.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk3.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk4.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk5.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk6.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk7.png")]
WCL = [pygame.image.load("static/Men_black/character_malePerson_walk0_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk1_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk2_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk3_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk4_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk5_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk6_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_walk7_left.png")]
RCR = [pygame.image.load("static/Men_black/character_malePerson_run0.png"),
       pygame.image.load("static/Men_black/character_malePerson_run1.png"),
       pygame.image.load("static/Men_black/character_malePerson_run2.png")]
RCL = [pygame.image.load("static/Men_black/character_malePerson_run0_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_run1_left.png"),
       pygame.image.load("static/Men_black/character_malePerson_run2_left.png")]
WZR = [pygame.image.load("static/Zombie/character_zombie_walk0.png"),
       pygame.image.load("static/Zombie/character_zombie_walk1.png"),
       pygame.image.load("static/Zombie/character_zombie_walk2.png"),
       pygame.image.load("static/Zombie/character_zombie_walk3.png"),
       pygame.image.load("static/Zombie/character_zombie_walk4.png"),
       pygame.image.load("static/Zombie/character_zombie_walk5.png"),
       pygame.image.load("static/Zombie/character_zombie_walk5.png"),
       pygame.image.load("static/Zombie/character_zombie_walk6.png"),
       pygame.image.load("static/Zombie/character_zombie_walk7.png")]
WZL = [pygame.image.load("static/Zombie/character_zombie_walk0_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk1_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk2_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk3_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk4_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk5_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk5_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk6_left.png"),
       pygame.image.load("static/Zombie/character_zombie_walk7_left.png")]

playerStand = pygame.image.load("static/Men_black/character_malePerson_idle.png")
bg = pygame.image.load("static/material/Background01.png")
mFloor = pygame.image.load("static/material/земля.png")
middlePlatform = pygame.image.load("static/material/меньше длинной.png")
smallPlatform = pygame.image.load("static/material/маленькая.png")
longPlatform = pygame.image.load("static/material/длинная.png")
fireball = pygame.image.load("static/material/fireball.png")


class User:
    def __init__(self, x, y, height, width, speed, boost, obj):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.boost = boost
        drawWindow(self.x, self.y, False, False, False, obj)

    def move_left(self, isFast, obj):
        if not isFast:
            if self.x - self.speed >= 5:
                drawWindow(self.x, self.y, True, False, False, obj)
                self.x -= self.speed
            else:
                drawWindow(self.x, self.y, False, False, False, obj)
        else:
            if self.x - self.speed - self.boost >= 5:
                drawWindow(self.x, self.y, True, False, True, obj)
                self.x -= self.speed
                self.x -= self.boost
            else:
                drawWindow(self.x, self.y, True, False, False, obj)

    def move_right(self, isFast, obj):
        if not isFast:
            if self.x + self.speed <= 795 - self.width:
                drawWindow(self.x, self.y, False, True, False, obj)
                self.x += self.speed
            else:
                drawWindow(self.x, self.y, False, False, False, obj)
        else:
            if self.x + self.speed + self.boost <= 795 - self.width:
                drawWindow(self.x, self.y, False, True, True, obj)
                self.x += self.speed
                self.x += self.boost
            else:
                drawWindow(self.x, self.y, False, False, False, obj)

    def get_coordinates(self):
        return (self.x, self.y)

    def jump(self, obj):
        global isJump, countJump
        isJump = True
        if countJump >= -10:
            if countJump > 0:
                self.y -= (countJump ** 2) // 4
            elif countJump < 0:
                self.y += (countJump ** 2) // 4
        else:
            isJump = False
            countJump = 10
        countJump -= 1
        drawWindow(self.x, self.y, False, False, False, obj)

    def stand(self, obj):
        drawWindow(self.x, self.y, False, False, False, obj)


class Ball:
    def __init__(self, x, y, speed=12):
        self.x = x
        self.y = y
        self.speed = speed

    def right(self):
        global fl, fr
        fr = True
        fl = False
        self.x += self.speed
        if self.x > 800:
            self.x = -1
            self.y = -1
            del self
            fr = False
            fl = False

    def left(self):
        global fl, fr
        fl = True
        fr = False
        self.x -= self.speed
        if self.x < 0:
            self.x = -1
            self.y = -1
            del self
            fr = False
            fl = False

    def get_coordinates(self):
        return (self.x, self.y)


animCount = 0
left = False
right = False
isJump = False
countJump = 10
clock = pygame.time.Clock()
fl = False
fr = False


def drawWindow(xp, yp, left, right, isRun, obj):
    global animCount, bg
    display.blit(bg, (0, 0))
    display.blit(longPlatform, (0, 580))
    if not (left) and not (right):
        animCount = 0
        display.blit(playerStand, (xp, yp))

    if animCount + 1 >= 32:
        animCount = 0

    if left:
        display.blit(WCL[animCount // 8], (xp, yp))
        animCount += 1
    elif right:
        display.blit(WCR[animCount // 8], (xp, yp))
        animCount += 1
    xb, yb = obj.get_coordinates()
    if xb != -1 and yb != -1:
        display.blit(fireball, (xb, yb))


ball = Ball(-1, -1)
player = User(800 - 20 - 48, 600 - 20 - 64, 64, 48, 3, 2, ball)


def run_game():
    global clock, isJump, countJump, fl, fr, player, ball
    game = True
    isJump = False
    JumpCount = 10

    while game:
        clock.tick(32)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
            player.move_right(True, ball)
        if keys[pygame.K_a]:
            player.move_left(False, ball)
        if keys[pygame.K_d]:
            player.move_right(False, ball)
        if keys[pygame.K_a] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
            player.move_left(True, ball)
        if fr:
            ball.right()
        if fl:
            ball.left()
        if not fl and not fr:
            if keys[pygame.K_q]:
                xb, yb = player.get_coordinates()
                ball = Ball(xb, yb + 15)
                ball.left()
        if not fr and not fl:
            if keys[pygame.K_e]:
                xb, yb = player.get_coordinates()
                ball = Ball(xb, yb + 15)
                ball.right()
        if isJump:
            player.jump(ball)
        if not isJump:
            countJump = 10
            if keys[pygame.K_SPACE]:
                player.jump(ball)
        if not (keys[pygame.K_a]) and not (keys[pygame.K_d]) and not (keys[pygame.K_q]) and \
                not (keys[pygame.K_e]):
            player.stand(ball)

        pygame.display.update()


run_game()
