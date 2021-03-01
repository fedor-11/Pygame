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
    def __init__(self, x, y, height, width, speed, boost, obj, z1, z2, z3):
        self.x = x
        self.y = y
        self.height = height
        self.width = width
        self.speed = speed
        self.boost = boost
        drawWindow(self.x, self.y, False, False, False, obj, z1, z2, z3)

    def move_left(self, isFast, obj, z1, z2, z3):
        if not isFast:
            if self.x - self.speed >= 5:
                drawWindow(self.x, self.y, True, False, False, obj, z1, z2, z3)
                self.x -= self.speed
            else:
                drawWindow(self.x, self.y, False, False, False, obj, z1, z2, z3)
        else:
            if self.x - self.speed - self.boost >= 5:
                drawWindow(self.x, self.y, True, False, True, obj, z1, z2, z3)
                self.x -= self.speed
                self.x -= self.boost
            else:
                drawWindow(self.x, self.y, True, False, False, obj, z1, z2, z3)

    def move_right(self, isFast, obj, z1, z2, z3):
        if not isFast:
            if self.x + self.speed <= 795 - self.width:
                drawWindow(self.x, self.y, False, True, False, obj, z1, z2, z3)
                self.x += self.speed
            else:
                drawWindow(self.x, self.y, False, False, False, obj, z1, z2, z3)
        else:
            if self.x + self.speed + self.boost <= 795 - self.width:
                drawWindow(self.x, self.y, False, True, True, obj, z1, z2, z3)
                self.x += self.speed
                self.x += self.boost
            else:
                drawWindow(self.x, self.y, False, False, False, obj, z1, z2, z3)

    def get_coordinates(self):
        return (self.x, self.y)

    def jump(self, obj, z1, z2, z3):
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
        drawWindow(self.x, self.y, False, False, False, obj, z1, z2, z3)

    def stand(self, obj, z1, z2, z3):
        drawWindow(self.x, self.y, False, False, False, obj, z1, z2, z3)


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


class Zombie:
    def __init__(self, x, y, speed=1.5):
        self.x = x
        self.y = y
        self.speed = speed
        self.move = "left"

    def move_left(self):
        self.x -= self.speed
        if (self.x - 40) < 0:
            if random.choice([0, 1]) == 1:
                self.x = 800
                self.move = "left"
            else:
                self.x = 0
                self.move = "right"

    def move_right(self):
        self.x += self.speed
        if self.x > 800:
            if random.choice([0, 1]) == 1:
                self.x = 800
                self.move = "left"
            else:
                self.x = 0
                self.move = "right"

    def get_move(self):
        return self.move

    def get_coordinates(self):
        return (self.x, self.y)

    def die(self):
        if random.choice([0, 1]) == 1:
            self.x = 800
            self.move = "left"
        else:
            self.x = 0
            self.move = "right"


animCount = 0
left = False
right = False
isJump = False
countJump = 10
clock = pygame.time.Clock()
fl = False
fr = False
acz = 0
zombies = [Zombie(0, 600 - 20 - 64), Zombie(0, 600 - 20 - 64), Zombie(0, 600 - 20 - 64)]


def drawWindow(xp, yp, left, right, isRun, obj, z1, z2, z3):
    global animCount, bg, acz
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

    if acz + 1 >= 32:
        acz = 0
    if z1.get_move() == "left":
        display.blit(WZL[acz//8], z1.get_coordinates())
        acz += 1
    else:
        display.blit(WZR[acz // 8], z1.get_coordinates())
        acz += 1
    if z2.get_move() == "left":
        display.blit(WZL[acz // 8], z2.get_coordinates())
        acz += 1
    else:
        display.blit(WZR[acz // 8], z2.get_coordinates())
        acz += 1
    if z3.get_move() == "left":
        display.blit(WZL[acz//8], z3.get_coordinates())
        acz += 1
    else:
        display.blit(WZR[acz // 8], z3.get_coordinates())
        acz += 1




ball = Ball(-1, -1)
player = User(800 - 20 - 48, 600 - 20 - 64, 64, 48, 3, 2, ball, zombies[0], zombies[1], zombies[2])
time = 0

def run_game():
    global clock, isJump, countJump, fl, fr, player, ball, zombies, time
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
            player.move_right(True, ball, zombies[0], zombies[1], zombies[2])
        if keys[pygame.K_a]:
            player.move_left(False, ball, zombies[0], zombies[1], zombies[2])
        if keys[pygame.K_d]:
            player.move_right(False, ball, zombies[0], zombies[1], zombies[2])
        if keys[pygame.K_a] and (keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT]):
            player.move_left(True, ball, zombies[0], zombies[1], zombies[2])
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
            player.jump(ball, zombies[0], zombies[1], zombies[2])
        if not isJump:
            countJump = 10
            if keys[pygame.K_SPACE]:
                player.jump(ball, zombies[0], zombies[1], zombies[2])
        if not (keys[pygame.K_a]) and not (keys[pygame.K_d]) and not (keys[pygame.K_q]) and \
                not (keys[pygame.K_e]):
            player.stand(ball, zombies[0], zombies[1], zombies[2])
        if zombies[0].get_move() == "left":
            zombies[0].move_left()
        else:
            zombies[0].move_right()

        if zombies[1].get_move() == "left":
            zombies[1].move_left()
        else:
            zombies[1].move_right()

        if zombies[2].get_move() == "left":
            zombies[2].move_left()
        else:
            zombies[2].move_right()

        xb, yb = ball.get_coordinates()
        xz, yz = zombies[0].get_coordinates()
        xp, yp = player.get_coordinates()
        if xz <= xp <= xz + 48 and yz <= yp <= yz + 64:
            print("Game Over")
            print(time/32)
            quit()
        if xz <= xb <= xz + 48:
            zombies[0].die()
        xz, yz = zombies[1].get_coordinates()
        if xz <= xp <= xz + 48 and yz <= yp <= yz - 64:
            print("Game Over")
            print(time / 32)
            quit()
        if xz <= xb <= xz + 48:
            zombies[1].die()
        xz, yz = zombies[2].get_coordinates()
        if xz <= xp <= xz + 48 and yz <= yp <= yz - 64:
            print("Game Over")
            print(time / 32)
            quit()
        if xz <= xb <= xz + 48:
            zombies[2].die()

        time += 1
        pygame.display.update()


run_game()
