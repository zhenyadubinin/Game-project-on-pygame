import pygame
import math
import random
import sys

WIDTH = 1366
HEIGHT = 768
block_size = 60
coin_size = block_size//2
gun_size = block_size
key_size = 30
FPS = 60
current_time = 0
button_press_time = 0
turret_reload = 0
timer_for_shooting = 0
coin_iteration = 0
heart_iteration = 0
key_iteration = 0
santa_got_free = 0
start_music_play = True
play_music_play = False
end_music_play = False
boss_music_play = False

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
COIN = (204, 204 ,0)

pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 40, True, False)
font2 = pygame.font.SysFont('Comic Sans MS', 26, True, False)
font3 = pygame.font.SysFont('Comic Sans MS', 20, True, False)
font4 = pygame.font.SysFont('Comic Sans MS', 150, True, False)
text_start = font.render("Press space to restart", True, YELLOW)
text_game_over = font4.render("Game Over", True, RED)
text_buy_gun = font.render("You need 60 coins to buy a weapon", True, COIN)
text_no_coin = font.render("You don't have enough money", True, RED)
text_full_gun = font.render("You have already received a weapon", True, RED)
text_success_purchase = font.render("You have bought a weapon!", True, GREEN)
text_thanks_1 = font2.render("Ohh, snowman, how can I prove my gratitude!", True, BLACK)
text_thanks_2 = font2.render("You, didn't only rescue me, but saved the whole", True, BLACK)
text_thanks_3 = font2.render("holiday on the whole Earth! Thank you!", True, BLACK)
text_the_end = font4.render('THE END', True, GREEN)
text_authors = [
    font3.render('Adilzhan Alibek', True, BLACK),
    font3.render('Dubinin Evgenii', True, BLACK),
    font3.render('Sagymbayeva Gulim', True, BLACK),
    font3.render('Abdigaliev Ernar', True, BLACK),
    font3.render('Erzhanuly Asyl', True, BLACK),
    font3.render('Beisov Anuar', True, BLACK),
]
text_authors7 = font3.render('Special thanks to prof. Timur Bakibayev (for sleepless nights in front of the laptop)', True, YELLOW)
text_esc = font3.render('press ESC to quit', True, BLUE)
g = font4.render('G', True, RED)
t = font4.render('T', True, GREEN)

state_start = "welcome"
state_play = "play"
state_game_over = "game over"
state_game_win = "game_win"

pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.mixer.init()
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
window = pygame.Surface((WIDTH, HEIGHT))
clock = pygame.time.Clock()

sound_coin = pygame.mixer.Sound('sound/coin.wav'); sound_coin.set_volume(0.05)
sound_jump = pygame.mixer.Sound('sound/jump_up.wav'); sound_jump.set_volume(0.2)
sound_shotgun = pygame.mixer.Sound('sound/shotgun.wav'); sound_shotgun.set_volume(0.2)
sound_machinegun = pygame.mixer.Sound('sound/machine_gun2.wav'); sound_machinegun.set_volume(0.2)
sound_run = pygame.mixer.Sound('sound/leg.wav'); sound_run.set_volume(0.2)
sound_gun = pygame.mixer.Sound('sound/gun.wav'); sound_gun.set_volume(0.08)
sound_gameover = pygame.mixer.Sound('sound/game_over2.wav')
sound_key = pygame.mixer.Sound('sound/key.wav'); sound_key.set_volume(0.3)
sound_new_level = pygame.mixer.Sound('sound/new_level.wav')
sound_trampoline = pygame.mixer.Sound('sound/trampoline.wav'); sound_trampoline.set_volume(0.08)
sound_no_bullets = pygame.mixer.Sound('sound/no_bullets.wav')
sound_reload_fast = pygame.mixer.Sound('sound/reload3.wav')
sound_reload_slow = pygame.mixer.Sound('sound/reload5.wav')
sound_jump_landing = pygame.mixer.Sound('sound/jump_landing2.wav')
sound_santa = pygame.mixer.Sound('sound/santa_voice.wav')

background_image = pygame.image.load('png/BG/BG.png').convert_alpha()
player_right = pygame.image.load('png/Characters/player/SnowMan1_right.png').convert_alpha()
player_left = pygame.image.load('png/Characters/player/SnowMan1_left.png').convert_alpha()
boss1_left = pygame.image.load('png/Characters/boss/boss1_snowman_left.png').convert_alpha()
boss1_right = pygame.image.load('png/Characters/boss/boss1_snowman_right.png').convert_alpha()
boss2_left = pygame.image.load('png/Characters/boss/boss2_snowman_left.png').convert_alpha()
boss2_right = pygame.image.load('png/Characters/boss/boss2_snowman_right.png').convert_alpha()
snow_left = pygame.image.load('png/Tiles/1.png').convert_alpha()
snow_mid_left = pygame.image.load('png/Tiles/B.png').convert_alpha()
snow_mid = pygame.image.load('png/Tiles/2.png').convert_alpha()
snow_mid_right = pygame.image.load('png/Tiles/7.png').convert_alpha()
snow_right = pygame.image.load('png/Tiles/3.png').convert_alpha()
ground_left = pygame.image.load('png/Tiles/4.png').convert_alpha()
ground_mid_left = pygame.image.load('png/Tiles/8.png').convert_alpha()
ground_mid = pygame.image.load('png/Tiles/5.png').convert_alpha()
ground_mid_right = pygame.image.load('png/Tiles/A.png').convert_alpha()
ground_right = pygame.image.load('png/Tiles/6.png').convert_alpha()
ground_bottom_left = pygame.image.load('png/Tiles/C.png').convert_alpha()
ground_bottom_mid = pygame.image.load('png/Tiles/9.png').convert_alpha()
ground_bottom_right = pygame.image.load('png/Tiles/D.png').convert_alpha()
platform_left = pygame.image.load('png/Tiles/E.png').convert_alpha()
platform_mid = pygame.image.load('png/Tiles/F.png').convert_alpha()
platform_right = pygame.image.load('png/Tiles/G.png').convert_alpha()
water_surf = pygame.image.load('png/Tiles/Water.png').convert_alpha()
water = pygame.image.load('png/Tiles/Water2.png').convert_alpha()
sign = pygame.image.load('png/Object/Sign_2.png').convert_alpha()
brick = pygame.image.load('png/Object/brick.png').convert_alpha()
ice = pygame.image.load('png/Object/IceBox.png').convert_alpha()
stone = pygame.image.load('png/Object/Stone.png').convert_alpha()
crate = pygame.image.load('png/Object/Crate.png').convert_alpha()
case = pygame.image.load('png/Object/case.png').convert_alpha()
trampoline = pygame.image.load('png/Object/trampoline.png').convert_alpha()
key = pygame.image.load('png/Object/key.png').convert_alpha()
health = pygame.image.load('png/Object/health.png').convert_alpha()
closed_door = pygame.image.load('png/Object/closed_door.png').convert_alpha()
opened_door = pygame.image.load('png/Object/opened_door.png').convert_alpha()
tree = pygame.image.load('png/Object/Tree.png').convert_alpha()
trees = pygame.image.load('png/Object/Trees.png').convert_alpha()
cloud = pygame.image.load('png/Object/cloud.png').convert_alpha()
bullet = pygame.image.load('png/Weapon/bullet.png').convert_alpha()
transparent_piece = pygame.image.load('png/Weapon/transparent_piece.png').convert_alpha()
pistol_left = pygame.image.load('png/Weapon/pistol_left.png').convert_alpha()
pistol_right = pygame.image.load('png/Weapon/pistol_right.png').convert_alpha()
shotgun_left = pygame.image.load('png/Weapon/shotgun_left.png').convert_alpha()
shotgun_right = pygame.image.load('png/Weapon/shotgun_right.png').convert_alpha()
machine_gun_right = pygame.image.load('png/Weapon/machine_gun_right.png').convert_alpha()
machine_gun_left = pygame.image.load('png/Weapon/machine_gun_left.png').convert_alpha()
santa_stay_left = pygame.image.load('png/Characters/santa/stay_left.png').convert_alpha()
santa_stay_right = pygame.image.load('png/Characters/santa/stay_right.png').convert_alpha()
santa_head = pygame.image.load('png/Characters/santa/santa_head.png').convert_alpha()
logo = pygame.image.load('png/BG/logo.png').convert_alpha()
coins_list=[pygame.image.load('png/Object/coins/coin1.png').convert_alpha(),
       pygame.image.load('png/Object/coins/coin2.png').convert_alpha(),
       pygame.image.load('png/Object/coins/coin3.png').convert_alpha(),
       pygame.image.load('png/Object/coins/coin4.png').convert_alpha(),
       pygame.image.load('png/Object/coins/coin5.png').convert_alpha()]

santa_list_left = []
santa_list_right = []
enemy_list_left = []
enemy_list_right = []
enemy_stay_left = pygame.image.load('png/Characters/enemy/stay_left.png').convert_alpha()
enemy_stay_right = pygame.image.load('png/Characters/enemy/stay_right.png').convert_alpha()
heart_list = [pygame.image.load('png/Object/heart_1.png').convert_alpha(),
              pygame.image.load('png/Object/heart_2.png').convert_alpha(),
              pygame.image.load('png/Object/heart_3.png').convert_alpha(),
              pygame.image.load('png/Object/heart_4.png').convert_alpha()]
key_list = [pygame.image.load('png/Object/key_1.png').convert_alpha(),
            pygame.image.load('png/Object/key_2.png').convert_alpha(),
            pygame.image.load('png/Object/key_3.png').convert_alpha(),
            pygame.image.load('png/Object/key_3.png').convert_alpha()]

for i in range(10):
    enemy_list_right.append(pygame.image.load(f'png/Characters/enemy/walk_rigint_{i + 1}.png').convert_alpha())
for i in range(10):
    enemy_list_left.append(pygame.image.load(f'png/Characters/enemy/walk_left_{i + 1}.png').convert_alpha())
for i in range(13):
    santa_list_right.append(pygame.image.load(f'png/Characters/santa/walk_{i + 1}.png').convert_alpha())
for i in range(13):
    santa_list_left.append(pygame.image.load(f'png/Characters/santa/walk_{i + 1}_left.png').convert_alpha())

background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))
player_right = pygame.transform.scale(player_right, (block_size, block_size))
player_left = pygame.transform.scale(player_left, (block_size, block_size))
boss1_left = pygame.transform.scale(boss1_left, (block_size * 2, block_size * 2))
boss1_right = pygame.transform.scale(boss1_right, (block_size * 2, block_size * 2))
boss2_left = pygame.transform.scale(boss2_left, (block_size * 2, block_size * 2))
boss2_right = pygame.transform.scale(boss2_right, (block_size * 2, block_size * 2))
snow_left = pygame.transform.scale(snow_left, (block_size, block_size))
snow_mid_left = pygame.transform.scale(snow_mid_left, (block_size, block_size))
snow_mid = pygame.transform.scale(snow_mid, (block_size, block_size))
snow_mid_right = pygame.transform.scale(snow_mid_right, (block_size, block_size))
snow_right = pygame.transform.scale(snow_right, (block_size, block_size))
ground_left = pygame.transform.scale(ground_left, (block_size, block_size))
ground_mid_left = pygame.transform.scale(ground_mid_left, (block_size, block_size))
ground_mid = pygame.transform.scale(ground_mid, (block_size, block_size))
ground_mid_right = pygame.transform.scale(ground_mid_right, (block_size, block_size))
ground_right = pygame.transform.scale(ground_right, (block_size, block_size))
ground_bottom_left = pygame.transform.scale(ground_bottom_left, (block_size, block_size))
ground_bottom_mid = pygame.transform.scale(ground_bottom_mid, (block_size, block_size))
ground_bottom_right = pygame.transform.scale(ground_bottom_right, (block_size, block_size))
platform_left = pygame.transform.scale(platform_left, (block_size, block_size))
platform_mid = pygame.transform.scale(platform_mid, (block_size, block_size))
platform_right = pygame.transform.scale(platform_right, (block_size, block_size))
brick = pygame.transform.scale(brick, (block_size, block_size))
ice = pygame.transform.scale(ice, (block_size, block_size))
stone = pygame.transform.scale(stone, (block_size, block_size))
sign = pygame.transform.scale(sign, (block_size, block_size))
water_surf = pygame.transform.scale(water_surf, (block_size, block_size))
water = pygame.transform.scale(water, (block_size, block_size))
case = pygame.transform.scale(case, (block_size, block_size))
crate = pygame.transform.scale(crate, (block_size, block_size))
trampoline = pygame.transform.scale(trampoline, (block_size, block_size//2))
key = pygame.transform.scale(key, (key_size, key_size))
health = pygame.transform.scale(health,(coin_size, coin_size))
closed_door = pygame.transform.scale(closed_door, (block_size, block_size))
opened_door = pygame.transform.scale(opened_door, (block_size, block_size))
tree = pygame.transform.scale(tree, (block_size*2, block_size*2))
trees = pygame.transform.scale(trees, (block_size*2, block_size*2))
cloud = pygame.transform.scale(cloud, (block_size*2, block_size))
bullet = pygame.transform.scale(bullet, (block_size//4, block_size//8))
transparent_piece = pygame.transform.scale(transparent_piece, (block_size//4, block_size//8))
pistol_left = pygame.transform.scale(pistol_left, (int(gun_size*0.5), int(gun_size*0.5)))
pistol_right = pygame.transform.scale(pistol_right, (int(gun_size*0.5), int(gun_size*0.5)))
shotgun_left = pygame.transform.scale(shotgun_left, (gun_size, gun_size//2))
shotgun_right = pygame.transform.scale(shotgun_right, (gun_size, gun_size//2))
machine_gun_left = pygame.transform.scale(machine_gun_left, (gun_size, gun_size//2))
machine_gun_right = pygame.transform.scale(machine_gun_right, (gun_size, gun_size//2))
enemy_stay_left = pygame.transform.scale(enemy_stay_left, (block_size, block_size))
enemy_stay_right = pygame.transform.scale(enemy_stay_right, (block_size, block_size))
santa_stay_left = pygame.transform.scale(santa_stay_left, (block_size, block_size))
santa_stay_right = pygame.transform.scale(santa_stay_right, (block_size, block_size))
santa_head = pygame.transform.scale(santa_head, (4 * block_size, 4 * block_size))
logo = pygame.transform.scale(logo, (6 * block_size, 6 * block_size))

for i in range(len(coins_list)):
    coins_list[i]=pygame.transform.scale(coins_list[i], (coin_size, coin_size))
for i in range(len(enemy_list_left)):
    enemy_list_left[i] = pygame.transform.scale(enemy_list_left[i], (block_size, block_size))
    enemy_list_right[i] = pygame.transform.scale(enemy_list_right[i], (block_size, block_size))
for i in range(len(santa_list_left)):
    santa_list_left[i] = pygame.transform.scale(santa_list_left[i], (block_size, block_size))
    santa_list_right[i] = pygame.transform.scale(santa_list_right[i], (block_size, block_size))
for i in range(len(heart_list)):
    heart_list[i]=pygame.transform.scale(heart_list[i], (coin_size, coin_size))
for i in range(len(key_list)):
    key_list[i]=pygame.transform.scale(key_list[i], (key_size, key_size))    
    
class Player(pygame.sprite.Sprite):
    def __init__(self, gun, x=0, y=0):
        pygame.sprite.Sprite.__init__(self)
        self.v_speed = -5
        self.h_speed = 0
        self.jump_height = 22
        self.jump_is_allowed = False
        self.look_left = False
        self.all_health = 200
        self.health = self.all_health
        self.points = 0
        self.keys = 0
        self.image_left = player_left
        self.image_right = player_right
        self.image = self.image_right
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = self.rect.x
        self.y = self.rect.y
        self.camera_x = 0
        self.camera_y = 0
        self.gun = gun
        self.hero_png_iteration = 0
        self.got_new_gun = False

    def update(self):
        global gravity, state, state_game_over, camera_x, camera_y, stable_x, stable_y, button_press_time
        self.rotate_gun()
        if self.rect.x + camera_x > WIDTH * 0.65:
            camera_x -= 7
        elif self.rect.x + camera_x < WIDTH * 0.35:
            camera_x += 7
        camera_y = -self.rect.y + HEIGHT * 0.3

        if self.y > HEIGHT + 200:
            sound_gameover.play()
            self.kill()
            state = state_game_over

        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x -= camera_x
        mouse_y -= int(camera_y * 0.3)
        if mouse_x > self.rect.centerx:
            self.image = self.image_right
            self.gun.look_left = False
            self.look_left = False
        else:
            self.image = self.image_left
            self.gun.look_left = True
            self.look_left = True

        self.h_speed = 0
        self.v_speed = self.v_speed + gravity
        if self.v_speed > 25:
            self.v_speed = 25
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_SPACE] or keystate[pygame.K_w]:
            if self.jump_is_allowed:
                sound_jump.play()
                self.v_speed = -self.jump_height
                self.jump_is_allowed = False
        if keystate[pygame.K_a]:
            self.h_speed = -7
        if keystate[pygame.K_d]:
            self.h_speed = 7
        if self.gun.automate and keystate[pygame.K_r] and self.gun.bullets_left < self.gun.bullets_number:
            pygame.mixer.Channel(1).play(self.gun.sound_reload_fast)
            self.gun.bullets_left = self.gun.bullets_number
            button_press_time = pygame.time.get_ticks()

        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.x += self.h_speed
        self.rect.y += self.v_speed
        if not self.look_left:
            self.gun.rect.centerx = self.rect.centerx - 10
            self.gun.rect.centery = self.rect.centery - 5
        else:
            self.gun.rect.centerx = self.rect.centerx - 20
            self.gun.rect.centery = self.rect.centery - 5

    def shoot(self):
        pygame.mixer.Channel(1).play(self.gun.sound)
        bullets_list = self.gun.prepare_bullets()
        for bullet in bullets_list:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x -= camera_x
            mouse_y -= int(camera_y * 0.3)
            rel_x, rel_y = mouse_x - bullet.rect.x, mouse_y - bullet.rect.y
            angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
            bullet.image = pygame.transform.rotate(bullet.image, int(angle))
            lendth_vector = math.sqrt(rel_x**2 + rel_y**2)
            if lendth_vector != 0:
                norm_vector_x, norm_vector_y = rel_x / lendth_vector, rel_y / lendth_vector
                bullet.h_speed = int(norm_vector_x * self.gun.bullet_speed)
                bullet.v_speed = int(norm_vector_y * self.gun.bullet_speed)
                all_sprites.add(bullet)
                bullets.add(bullet)

    def rotate_gun(self):
        mouse_x, mouse_y = pygame.mouse.get_pos()
        mouse_x -= camera_x
        mouse_y -= int(camera_y * 0.3)
        rel_x, rel_y = mouse_x - self.gun.rect.centerx, mouse_y - self.gun.rect.centery
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        if self.gun.look_left:
            self.gun.image = pygame.transform.rotate(self.gun.image_left, int(angle - 180))
        else:
            self.gun.image = pygame.transform.rotate(self.gun.image_right, int(angle))

    def add_points(self):
        self.points += 1
    def add_health(self):
        if self.health <= self.all_health * 0.5:
            self.health += self.all_health * 0.5
        else:
            self.health = self.all_health
    def add_key(self):
        self.keys += 1
    def add_gun(self,gun):
        self.gun = gun
    def show_points(self):
        screen.blit(coins_list[1], (10, 10))
        score = font.render(f"{self.points}", True, COIN)
        screen.blit(score, (40, -5))

    def show_keys(self):
        key_image = pygame.transform.scale(key, (coin_size, coin_size))
        screen.blit(key_image, (10, 50))
        score = font.render(f"{self.keys}", True, (218, 165, 32))
        screen.blit(score, (40, 35))
  
class Mob(pygame.sprite.Sprite):
    def __init__(self, x, y, image_left, image_right, size, gun):
        pygame.sprite.Sprite.__init__(self)
        self.v_speed = -5
        self.h_speed = 0
        self.jump_height = 22
        self.jump_is_allowed = False
        self.look_left = False
        self.all_health = 100
        self.health = self.all_health
        self.points = 0
        self.image_left = image_left
        self.image_right = image_right
        self.image = self.image_left
        self.rect = self.image.get_rect()
        self.x = 0
        self.y = 0
        self.rect.x = x
        self.rect.y = y
        self.camera_x = 0
        self.camera_y = 0
        self.cycle = 130
        self.change = 0
        self.trigger = False
        self.trigger_general = False
        self.collided_with_block = False
        self.walk_away = 3
        self.path = []
        self.trigger_old = self.trigger
        self.gun = gun
        self.current_time = pygame.time.get_ticks()
        self.time_shoot = self.current_time - self.gun.reload
        self.enemy_png_iteration = 0

    def update(self):
        global gravity, state, state_game_over
        rand_number = random.randint(1, 4)

        self.shoot_x_ray()
        if self.y > HEIGHT + 1000:
            self.kill()
            self.gun.kill()

        self.h_speed = 0
        self.v_speed = self.v_speed + gravity

        if self.v_speed > 25:
            self.v_speed = 25

        if self.trigger and self.trigger_general:
            projection = player.rect.x - self.rect.x
            self.h_speed = rand_number if bool(projection >= 0) else -rand_number
            if pygame.time.get_ticks() - self.time_shoot > self.gun.reload:
                self.shoot()
                self.time_shoot = pygame.time.get_ticks()
            self.path = []

        if self.trigger == False and self.trigger_old == True:
            self.path.append((player.rect.x, player.rect.y))

        if self.trigger == False and self.trigger_general == True:
            self.path.append((player.rect.x, player.rect.y))
            if self.path != [] and self.rect.x != self.path[0][0] and self.rect.y != self.path[0][1]:
                projection = self.path[0][0] - self.rect.x
                self.h_speed = rand_number if bool(projection >= 0) else -rand_number
            elif self.path != [] and self.rect.x == self.path[0][0] and self.rect.y > self.path[0][1] and self.jump_is_allowed:
                self.v_speed -= self.jump_height
                self.jump_is_allowed = False

            else:
                self.path.pop(0)

        if self.trigger == False and self.trigger_general == False:
            if self.cycle >= 0:
                self.h_speed = 2 if bool(self.change) else -2
                self.cycle -= 1
            else:
                self.cycle = 130
                self.change = (self.change + 1) % 2

        if self.collided_with_block and self.jump_is_allowed:
            self.v_speed -= self.jump_height
            self.jump_is_allowed = False

        if self.h_speed > 0:
            self.gun.rect.centerx = self.rect.centerx + 14
            self.gun.rect.centery = self.rect.centery + gun_size // 8
            self.image = enemy_list_right[self.enemy_png_iteration // 3]
            self.gun.image = self.gun.image_right
            self.gun.look_left = False
        elif self.h_speed < 0:
            self.gun.rect.centerx = self.rect.centerx - 14
            self.gun.rect.centery = self.rect.centery + gun_size // 8
            self.image = enemy_list_left[self.enemy_png_iteration // 3]
            self.gun.image = self.gun.image_left
            self.gun.look_left = True
        elif self.look_left and self.h_speed == 0:
            self.image = enemy_stay_left
            self.gun.rect.centerx = self.rect.centerx - 14
            self.gun.rect.centery = self.rect.centery + gun_size // 8
            self.gun.image = self.gun.image_left
            self.gun.look_left = True
        elif self.look_left == False and self.h_speed == 0:
            self.image = enemy_stay_right
            self.gun.rect.centerx = self.rect.centerx + 14
            self.gun.rect.centery = self.rect.centery + gun_size // 8
            self.gun.image = self.gun.image_right
            self.gun.look_left = False
        
        self.enemy_png_iteration = (self.enemy_png_iteration + 1) % (3 * len(enemy_list_left))

        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.x += self.h_speed
        self.rect.y += self.v_speed
        self.trigger_old = self.trigger

    def shoot(self):
        pygame.mixer.Channel(2).play(self.gun.sound)
        bullet = Bullet(self.rect.centerx, self.rect.centery, self.gun)
        mouse_x, mouse_y = player.rect.centerx, player.rect.centery
        rel_x, rel_y = mouse_x - bullet.rect.x, mouse_y - bullet.rect.y
        angle = (180 / math.pi) * -math.atan2(rel_y, rel_x)
        bullet.image = pygame.transform.rotate(bullet.image, int(angle))
        lendth_vector = math.sqrt(rel_x**2 + rel_y**2)
        if lendth_vector != 0:
            norm_vector_x, norm_vector_y = rel_x / lendth_vector, rel_y / lendth_vector
            bullet.h_speed = int(norm_vector_x * self.gun.bullet_speed)
            bullet.v_speed = int(norm_vector_y * self.gun.bullet_speed)
            all_sprites.add(bullet)
            bullets_enemy.add(bullet)

    def shoot_x_ray(self):
        ray = X_ray(self.rect.centerx, self.rect.centery, self)
        mouse_x, mouse_y = player.rect.centerx, player.rect.centery
        rel_x, rel_y = mouse_x - ray.rect.x, mouse_y - ray.rect.y
        lendth_vector = math.sqrt(rel_x**2 + rel_y**2)
        if lendth_vector != 0:
            norm_vector_x, norm_vector_y = rel_x / lendth_vector, rel_y / lendth_vector
            ray.h_speed = int(norm_vector_x * 30)
            ray.v_speed = int(norm_vector_y * 30)
            all_sprites.add(ray)
            x_rays_enemy.add(ray)

class Boss(Mob):
    def __init__(self, x, y, image_left, image_right, size, gun, large_coef):
        super(Boss, self).__init__(x, y, image_left, image_right, size, gun)
        self.gun.image_left = pygame.transform.scale(self.gun.image_left, (gun_size, gun_size)) 
        self.gun.image_right = pygame.transform.scale(self.gun.image_right, (gun_size, gun_size))
        self.all_health = 500        
        self.health = self.all_health
        self.large_coef = large_coef
        self.holding_key = False

    def update(self):
        global gravity, state, state_game_over
        rand_number = random.randint(1, 4)

        self.shoot_x_ray()
        if self.y > HEIGHT:
            self.kill()
            self.gun.kill()

        self.h_speed = 0
        self.v_speed = self.v_speed + gravity

        if self.v_speed > 25:
            self.v_speed = 25

        if self.trigger and self.trigger_general:
            projection = player.rect.x - self.rect.x
            self.h_speed = rand_number if bool(projection >= 0) else -rand_number
            if pygame.time.get_ticks() - self.time_shoot >= self.gun.reload:
                self.shoot()
                self.time_shoot = pygame.time.get_ticks()
            self.path = []

        if self.trigger == False and self.trigger_old == True:
            self.path.append((player.rect.x, player.rect.y))

        if self.trigger == False and self.trigger_general == True:
            self.path.append((player.rect.x, player.rect.y))
            if self.path != [] and self.rect.x != self.path[0][0] and self.rect.y != self.path[0][1]:
                projection = self.path[0][0] - self.rect.x
                self.h_speed = rand_number if bool(projection >= 0) else -rand_number
            elif self.path != [] and self.rect.x == self.path[0][0] and self.rect.y > self.path[0][1] and self.jump_is_allowed:
                self.v_speed -= self.jump_height
                self.jump_is_allowed = False
            else:
                self.path.pop(0)


        if self.trigger == False and self.trigger_general == False:
            if self.cycle >= 0:
                self.h_speed = 2 if bool(self.change) else -2
                self.cycle -= 1
            else:
                self.cycle = 130
                self.change = (self.change + 1) % 2

        if self.collided_with_block and self.jump_is_allowed:
            self.v_speed -= self.jump_height
            self.jump_is_allowed = False

        if self.h_speed > 0:
            self.gun.rect.centerx = self.rect.centerx + 25
            self.gun.rect.centery = self.rect.centery
            self.image = self.image_right
            self.gun.image = self.gun.image_right
            self.gun.look_left = False
        elif self.h_speed < 0:
            self.gun.rect.centerx = self.rect.centerx - 45
            self.gun.rect.centery = self.rect.centery
            self.image = self.image_left
            self.gun.image = self.gun.image_left
            self.gun.look_left = True
        elif self.h_speed and not self.look_left:
            self.gun.rect.centerx = self.rect.centerx + 25
            self.gun.rect.centery = self.rect.centery
            self.gun.image = self.gun.image_left
            self.gun.look_left = True
        elif self.h_speed == 0 and self.look_left:
            self.gun.rect.centerx = self.rect.centerx - 45
            self.gun.rect.centery = self.rect.centery
            self.gun.image = self.gun.image_left
            self.gun.look_left = True

        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.x += self.h_speed
        self.rect.y += self.v_speed
        self.trigger_old = self.trigger

class Santa(Mob):
    def __init__(self, x, y, image_left, image_right, size, gun):
        super(Santa, self).__init__(x, y, image_left, image_right, size, gun)
        self.image_left = image_left
        self.image_right = image_right
        self.gun.image_left = transparent_piece 
        self.gun.image_right = transparent_piece
        self.santa_png_iteration = 0

    def update(self):
        global gravity, state, state_game_over
        rand_number = random.randint(1, 4)

        self.shoot_x_ray()
        if self.y > HEIGHT:
            self.kill()
            self.gun.kill()

        self.h_speed = 0
        self.v_speed = self.v_speed + gravity

        if self.v_speed > 25:
            self.v_speed = 25

        if abs(self.rect.x - player.rect.x) < block_size:
            self.h_speed = 0
            if self.look_left:
                self.image = self.image_left
            else:
                self.image = self.image_right

        else:
            if self.trigger and self.trigger_general:
                projection = player.rect.x - self.rect.x
                self.h_speed = rand_number if bool(projection >= 0) else -rand_number
                self.path = []

            if self.trigger == False and self.trigger_old == True:
                self.path.append((player.rect.x, player.rect.y))

            if self.trigger == False and self.trigger_general == True:
                self.path.append((player.rect.x, player.rect.y))
                if self.path != [] and self.rect.x != self.path[0][0] and self.rect.y != self.path[0][1]:
                    projection = self.path[0][0] - self.rect.x
                    self.h_speed = rand_number if bool(projection >= 0) else -rand_number
                elif self.path != [] and self.rect.x == self.path[0][0] and self.rect.y > self.path[0][1] and self.jump_is_allowed:
                    self.v_speed -= self.jump_height
                    self.jump_is_allowed = False
                else:
                    self.path.pop(0)

            if self.trigger == False and self.trigger_general == False:
                if self.cycle >= 0:
                    self.h_speed = 2 if bool(self.change) else -2
                    self.cycle -= 1
                else:
                    self.cycle = 130
                    self.change = (self.change + 1) % 2

            if self.collided_with_block and self.jump_is_allowed:
                self.v_speed -= self.jump_height
                self.jump_is_allowed = False

            if self.h_speed > 0:
                self.image = santa_list_right[self.santa_png_iteration // 3]
                self.gun.rect.centerx = self.rect.centerx + 25
                self.gun.rect.centery = self.rect.centery
                self.gun.image = self.gun.image_right
                self.gun.look_left = False
                self.look_left = False
            elif self.h_speed < 0:
                self.image = santa_list_left[self.santa_png_iteration // 3]
                self.gun.rect.centerx = self.rect.centerx - 45
                self.gun.rect.centery = self.rect.centery
                self.gun.image = self.gun.image_left
                self.gun.look_left = True
                self.look_left = True
            elif self.h_speed == 0 and not self.look_left:
                self.image = self.image_right
                self.gun.rect.centerx = self.rect.centerx + 25
                self.gun.rect.centery = self.rect.centery
                self.gun.image = self.gun.image_left
                self.gun.look_left = False
            elif self.h_speed == 0 and self.look_left:
                self.image = self.image_left
                self.gun.rect.centerx = self.rect.centerx - 45
                self.gun.rect.centery = self.rect.centery
                self.gun.image = self.gun.image_left
                self.gun.look_left = True

            self.santa_png_iteration = (self.santa_png_iteration + 1) % (3 * len(santa_list_right))

        self.x = self.rect.x
        self.y = self.rect.y
        self.rect.x += self.h_speed
        self.rect.y += self.v_speed
        self.trigger_old = self.trigger

class Weapon(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pistol_right
        self.image_left = pistol_left
        self.image_right = pistol_right
        self.rect = self.image.get_rect()
        self.look_left = False
        self.automate_shooting = False

    def update(self):
        global camera_x, camera_y

class WeaponPistol(Weapon):
    def __init__(self):
        super(WeaponPistol, self).__init__()
        self.image = pistol_right
        self.image_left = pistol_left
        self.image_right = pistol_right
        self.bullet_speed = 30
        self.damage = 10
        self.automate = False
        self.reload = 700
        self.sound = sound_gun

    def prepare_bullets(self):
        bullets = [Bullet(self.rect.centerx, self.rect.centery, self)]
        return bullets

class WeaponShotgun(Weapon):
    def __init__(self):
        super(WeaponShotgun, self).__init__()
        self.image = shotgun_right
        self.image_left = shotgun_left
        self.image_right = shotgun_right
        self.bullet_speed = 50
        self.damage = 10
        self.automate = False
        self.reload = 1000
        self.sound = sound_shotgun

    def prepare_bullets(self):
        bullets_list = [
            Bullet(self.rect.centerx, self.rect.centery, self),
            Bullet(self.rect.centerx, self.rect.centery + 4, self),
            Bullet(self.rect.centerx, self.rect.centery - 4, self),
            Bullet(self.rect.centerx, self.rect.centery + 8, self),
            Bullet(self.rect.centerx, self.rect.centery - 8, self),
            ]
        return bullets_list

class WeaponMachineGun(Weapon):
    def __init__(self):
        super(WeaponMachineGun, self).__init__()
        self.image = machine_gun_right
        self.image_left = pygame.transform.scale(machine_gun_left, (gun_size + 10, gun_size - 10))
        self.image_right = pygame.transform.scale(machine_gun_right, (gun_size + 10, gun_size - 10))
        self.bullet_speed = 100
        self.reload = 1500
        self.damage = 10
        self.automate = True
        self.automate_shooting = False
        self.bullets_number = 20
        self.bullets_left = self.bullets_number
        self.SPS = 8
        self.sound = sound_machinegun
        self.sound_reload_fast = sound_reload_fast

    def prepare_bullets(self):
        bullets_list = [
            Bullet(self.rect.centerx, self.rect.centery, self),
            ]
        return bullets_list

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, gun):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.v_speed = -10
        self.h_speed = 10
        self.gun = gun

    def update(self):
        global camera_x, camera_y
        self.rect.y += self.v_speed
        self.rect.x += self.h_speed
        if self.rect.bottom < -2000 or self.rect.left > WIDTH - camera_x or self.rect.right + camera_x < 0 or self.rect.top > 2000:
            self.kill()

class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jump = False
        self.shooting = False
        self.active = False
        self.have_bought = False
        self.button_sell_time = 0
        self.have_money = False
        self.counter_for_text = 0
        self.start_counting = False
        self.gun = -1

    def shoot(self):
        bullet = Bullet(self.rect.centerx - block_size, self.rect.centery, WeaponPistol())
        bullet.image = pygame.transform.rotate(bullet.image, 180)
        bullet.h_speed = -10
        bullet.v_speed = 0
        bullets_enemy.add(bullet)
        bullets.add(bullet)
        all_sprites.add(bullet)

    def buy_weapon(self):
        if player.points >= 60:
            self.have_money = True
            self.button_sell_time = pygame.time.get_ticks()
            keystate = pygame.key.get_pressed()
            if keystate[pygame.K_e]:
                if self.active:
                    self.active = False
                    player.points -= 60
                    player.gun.kill()
                    gun = self.gun
                    all_sprites.add(gun)
                    player.add_gun(gun)
                    player.got_new_gun = True
                    self.have_bought = True
        else:
            self.have_money = False
            self.button_sell_time = pygame.time.get_ticks()

    def update(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.button_sell_time < 2000 and self.have_money == False and self.have_bought == False:
            screen.blit(text_no_coin, (100, -5))
        elif current_time - self.button_sell_time < 2000 and self.have_bought == False:
            screen.blit(text_buy_gun, (100, -5))
        elif current_time - self.button_sell_time < 2000 and self.have_bought == True and self.counter_for_text < 60:
            screen.blit(text_success_purchase, (100, -5))
            self.start_counting = True
        elif self.counter_for_text == 60:
            self.start_counting = False

        if self.start_counting:
            self.counter_for_text += 1

class Door(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.jump = False

    def check_key(self):
        global event_blocks
        if player.keys == 1:
            sound_new_level.play()
            self.image = opened_door
            player.keys -= 1
            event_blocks['free_Santa'] = [self.rect.x, self.rect.y, True]

class Coin(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        global coin_iteration
        self.image = coins_list[coin_iteration // 500]
        coin_iteration = (coin_iteration + 1) % (500 * len(coins_list))

class Heart(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def update(self):
        global heart_iteration
        self.image = heart_list[heart_iteration // 150]
        heart_iteration = (heart_iteration + 1) % (150 * len(heart_list)) 

class Key(pygame.sprite.Sprite):
    def __init__(self, x, y, image):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.gravity = 2
        self.v_speed = -30
        self.x = x
        self.y = y

    def update(self):
        global key_iteration
        key_iteration = (key_iteration + 1) % (60 * len(key_list))
        self.image = key_list[key_iteration // 60]
        self.v_speed += self.gravity
        if self.v_speed >= 24:
            self.v_speed = 24
        self.rect.y += self.v_speed
        if self.rect.y >= self.y:
            self.rect.y = self.y


class X_ray(pygame.sprite.Sprite):
    def __init__(self, x, y, mob):
        pygame.sprite.Sprite.__init__(self)
        self.image = transparent_piece
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.v_speed = -10
        self.h_speed = 10
        self.mob = mob

    def update(self):
        global camera_x, camera_y
        self.rect.y += self.v_speed
        self.rect.x += self.h_speed
        if self.rect.bottom < -2000 or self.rect.left > WIDTH - camera_x or self.rect.right + camera_x < 0 or self.rect.top > 2000:
            self.kill()

class Menu:
    def __init__(self, punkts = [0, 0, 'punkt', (250, 250, 30), (250, 30, 250)]):
        self.punkts = punkts

    def render(self, poverhost, font, num_punkt):
        for i in self.punkts:
            if num_punkt == i[5]:
                poverhost.blit(font.render(i[2], 1, i[4]), (i[0], i[1] + 60))
            else:
                poverhost.blit(font.render(i[2], 1, i[3]), (i[0], i[1] + 60))

    def menu(self):
        global state, state_play, play_music_play
        igra = True
        font_menu = pygame.font.Font("fonts/super_mario_bros.otf", 50)
        pygame.key.set_repeat(0,0)
        pygame.mouse.set_visible(True)
        punkt = 0
        background_rules = pygame.image.load("png/BG/BG_Rules.png")
        while igra:
            window.fill((0, 100, 0))
            window.blit(background_image, (0, 0))
            screen.blit(window, (0, 0))
            mp = pygame.mouse.get_pos()   # learn
            for i in self.punkts:
                if mp[0] > i[0] and mp[0] < i[0] + 155 and mp[1] > i[1] and mp[1] > i[1] + 50: # learn
                    punkt = i[5]
            self.render(window, font_menu, punkt)
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    sys.exit()
                if i.type == pygame.KEYDOWN:    
                    if i.key == pygame.K_ESCAPE:    
                        sys.exit()
                    if i.key == pygame.K_UP:
                        if punkt > 0:
                            punkt -= 1
                    if i.key == pygame.K_DOWN:
                        if punkt < len(self.punkts) - 1:
                            punkt += 1
                if i.type == pygame.MOUSEBUTTONDOWN and i.button == 1:
                    if punkt == 0:
                        state = state_play
                        igra = False
                        play_music_play = True
                    elif punkt == 1:
                        rules = True
                        while rules:
                            screen.blit(background_rules, (0, 0))
                            pygame.display.flip()
                            for j in pygame.event.get():
                                if j.type == pygame.KEYDOWN:    
                                    if j.key == pygame.K_ESCAPE:  
                                        rules = False
                                        break
                    elif punkt == 2:
                        sys.exit()       
            screen.blit(window, (0, 0))
            pygame.display.flip()

#Functions
def load_game_map():
    global game_map
    game_map.clear()
    with open('map.txt', 'r') as f:
        for line in f:
            game_map.append(line)

def draw_shield_bar(length, height, x, y, health, all_health, color):
    if health < 0:
        health = 0
    BAR_LENGTH = length
    BAR_HEIGHT = height
    fill = (health / all_health) * BAR_LENGTH
    outline_rect = pygame.Rect(x, y, BAR_LENGTH, BAR_HEIGHT)
    fill_rect = pygame.Rect(x, y, fill, BAR_HEIGHT)
    pygame.draw.rect(screen, color, fill_rect)
    pygame.draw.rect(screen, WHITE, outline_rect, 2)

def automate_shoot(charachter, current_time, button_press_time):
    if charachter.gun.automate_shooting and charachter.gun.bullets_left > 0 and current_time - button_press_time > charachter.gun.reload:
        charachter.shoot()
        charachter.gun.bullets_left -= 1

    if charachter.gun.automate and charachter.gun.bullets_left <= 0:
        charachter.gun.bullets_left = charachter.gun.bullets_number
        pygame.mixer.Channel(1).play(sound_no_bullets)
        pygame.mixer.Channel(6).play(sound_reload_slow)
        button_press_time = pygame.time.get_ticks()

    return button_press_time

def collide(sprite1, sprite2):
    global HEIGHT, state_game_over, state

    if sprite1 == player and sprite2 == blocks:
        collisions = pygame.sprite.spritecollide(sprite1, sprite2, False)
        if collisions == []:
            sprite1.jump_is_allowed = False
        else:
            for collision in collisions:
                r_from_above = collision.rect.y - sprite1.y - block_size
                r_from_below = sprite1.y - collision.rect.y - block_size
                if (abs(sprite1.x + block_size//2 - collision.rect.centerx) < block_size) and ((((sprite1.rect.bottom - collision.rect.top) < 1) or ((sprite1.rect.top - collision.rect.bottom) < 1))) and (r_from_above >= 0 or r_from_below >= 0):
                    if sprite1.h_speed > 0:
                        pygame.mixer.Channel(3).play(sound_run)
                    if sprite1.v_speed > 0:
                        sprite1.rect.y = sprite1.y + r_from_above
                        sprite1.jump_is_allowed = True
                    elif sprite1.v_speed < 0:
                        sprite1.rect.y = sprite1.y - r_from_below
                    sprite1.v_speed = 0
                    if collision.jump:
                        pygame.mixer.Channel(6).play(sound_trampoline)
                        sprite1.jump_height = 32
                        sprite1.v_speed = -sprite1.jump_height
                    else:
                        sprite1.jump_height = 22

        collisions = pygame.sprite.spritecollide(sprite1, sprite2, False)
        if collisions != []:
            sprite1.gun.rect.centerx = sprite1.x + block_size // 2
        for collision in collisions:
            if sprite1.rect.left <= collision.rect.right or sprite1.rect.right >= collision.rect.left:
                sprite1.rect.x = sprite1.x
                if sprite1.h_speed > 0:
                    r_from_left = collision.rect.left - sprite1.rect.right
                    sprite1.rect.x = sprite1.x + r_from_left
                if sprite1.h_speed < 0:
                    r_from_right = sprite1.rect.left - collision.rect.right
                    sprite1.rect.x = sprite1.x - r_from_right

    if sprite1 == mobs and sprite2 == blocks:
        for mob in sprite1:
            if mob == boss1:
                size = block_size * boss1.large_coef
            elif mob == boss2:
                size = block_size * boss2.large_coef
            else:
                size = block_size

            collisions = pygame.sprite.spritecollide(mob, sprite2, False)
            if collisions == []:
                mob.jump_is_allowed = False
            else:
                mob.gun.centery = mob.y + block_size // 2
                for collision in collisions:
                    r_from_above = collision.rect.y - mob.y - size
                    r_from_below = mob.y - collision.rect.y - size
                    if (abs(mob.x + size//2 - collision.rect.centerx) < size) and ((((mob.rect.bottom - collision.rect.top) < 1) or ((mob.rect.top - collision.rect.bottom) < 1))) and (r_from_above >= 0 or r_from_below >= 0):
                        if mob.v_speed > 0:
                            mob.rect.y = mob.y + r_from_above
                            mob.jump_is_allowed = True
                        elif mob.v_speed < 0:
                            mob.rect.y = mob.y - r_from_below
                        mob.v_speed = 0
                        if collision.jump:
                            pygame.mixer.Channel(7).play(sound_trampoline)
                            mob.jump_height = 32
                            mob.v_speed = -mob.jump_height
                            mob.jump_is_allowed = False
                        else:
                            mob.jump_height = 22

            collisions = pygame.sprite.spritecollide(mob, sprite2, False)
            if collisions == []:
                mob.collided_with_block = False
            if collisions != []:
                mob.gun.centerx = mob.x + block_size // 2
            for collision in collisions:
                if mob.rect.left <= collision.rect.right or mob.rect.right >= collision.rect.left:
                    mob.rect.x = mob.x
                    if mob.h_speed > 0:
                        r_from_left = collision.rect.left - mob.rect.right
                        mob.rect.x = mob.x + r_from_left
                    if mob.h_speed < 0:
                        r_from_right = mob.rect.left - collision.rect.right
                        mob.rect.x = mob.x - r_from_right
                    mob.collided_with_block = True
                    
    elif sprite1 == player and sprite2 == coins:
        for collision in sprite2:
            if sprite1.rect.colliderect(collision.rect):
                sound_coin.play()
                collision.kill()
                sprite1.add_points()

    elif sprite1 == player and sprite2 == hearts:
        for collision in sprite2:
            if sprite1.rect.colliderect(collision.rect) and sprite1.health < sprite1.all_health:
                collision.kill()
                sprite1.add_health()

    elif sprite1 == player and sprite2 == keys:
        for collision in sprite2:
            if sprite1.rect.colliderect(collision.rect):
                sound_key.play()
                collision.kill()
                sprite1.add_key()

    elif sprite1 == player and sprite2 == door1:
        if sprite1.rect.colliderect(sprite2.rect):
            sprite2.check_key()

    elif sprite1 == player and sprite2 == strong_boxes:
        case = pygame.sprite.spritecollide(sprite1, sprite2, False)
        if case != []:
            if sprite1.rect.colliderect(case[0].rect):
                case[0].buy_weapon()
    
    elif (sprite1 == bullets or sprite1 == bullets_enemy) and sprite2 == blocks:
        hits = pygame.sprite.groupcollide(sprite1, sprite2, True, False)
        for hit in hits:
            hit.kill()

    elif sprite1 == x_rays_enemy and sprite2 == blocks:
        hits = pygame.sprite.groupcollide(sprite1, sprite2, True, False)
        for hit in hits:
            hit.mob.trigger = False
            hit.kill()

    elif sprite1 == mobs and sprite2 == bullets:
        global event_blocks
        hits = pygame.sprite.groupcollide(sprite1, sprite2, False, True)
        for m in hits.keys():
            try:
                if m == santa:
                    break
            except:
                m.health -= len(hits[m]) * (hits[m][0].gun.damage)
                if m.health <= 0:
                    if m == boss1 and m.holding_key == False:
                        boss2.holding_key = True
                    elif m == boss2 and m.holding_key == False:
                        boss1.holding_key = True
                    elif (m == boss1 or m == boss2) and m.holding_key == True:
                        event_blocks['key_have_been_fallen'] = [m.rect.centerx, m.rect.centery, True]
                    m.kill()
                    m.gun.kill()

    elif sprite1 == player and sprite2 == bullets_enemy:
        hits = pygame.sprite.spritecollide(sprite1, sprite2, False)
        for hit in hits:
            hit.kill()
            sprite1.health -= 5

    elif sprite1 == player and sprite2 == x_rays_enemy:
        hits = pygame.sprite.spritecollide(sprite1, sprite2, False)
        for hit in hits:
            hit.mob.trigger = True
            hit.mob.trigger_general = True
            hit.kill()

all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
bullets_enemy = pygame.sprite.Group()
blocks = pygame.sprite.Group()
coins = pygame.sprite.Group()
hearts = pygame.sprite.Group()
keys = pygame.sprite.Group()
x_rays_enemy = pygame.sprite.Group()
strong_boxes = pygame.sprite.Group()
event_blocks = {}
path = []

game_map = []
gravity = 1
state = state_start
waiting_command = 0
punkts =[(590, 250, "Start", (255, 255, 255), (0, 0, 0), 0),
(600, 350, "Rules", (255, 255, 255), (0, 0, 0), 1),
(620, 450, "Quit", (255, 255, 255), (250, 10, 50), 2)]
game = Menu(punkts)

done = True
while done:
    if state == state_start:
        if start_music_play:
            pygame.mixer.music.load('sound/sound_menu.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            start_music_play = False
        camera_x = 0
        camera_y = 0
        if waiting_command < 1:
            stable_x = 0
            stable_y = 0

            load_game_map()
            for i in range(len(game_map)):
                for j in range(len(game_map[i])):
                    if game_map[i][j] == '1':
                        snow_left1 = Block(block_size * j, block_size * i, snow_left)
                        blocks.add(snow_left1)
                        all_sprites.add(snow_left1)
                    if game_map[i][j] == '2':
                        snow_mid1 = Block(block_size * j, block_size * i, snow_mid)
                        blocks.add(snow_mid1)
                        all_sprites.add(snow_mid1)
                    if game_map[i][j] == '3':
                        snow_right1 = Block(block_size * j, block_size * i, snow_right)
                        blocks.add(snow_right1)
                        all_sprites.add(snow_right1)
                    if game_map[i][j] == '4':
                        ground_left1 = Block(block_size * j, block_size * i, ground_left)
                        blocks.add(ground_left1)
                        all_sprites.add(ground_left1)
                    if game_map[i][j] == '5':
                        ground_mid1 = Block(block_size * j, block_size * i, ground_mid)
                        blocks.add(ground_mid1)
                        all_sprites.add(ground_mid1)
                    if game_map[i][j] == '6':
                        ground_right1 = Block(block_size * j, block_size * i, ground_right)
                        blocks.add(ground_right1)
                        all_sprites.add(ground_right1)
                    if game_map[i][j] == '7':
                        snow_mid_right1 = Block(block_size * j, block_size * i, snow_mid_right)
                        blocks.add(snow_mid_right1)
                        all_sprites.add(snow_mid_right1)
                    if game_map[i][j] == '8':
                        ground_mid_left1 = Block(block_size * j, block_size * i, ground_mid_left)
                        blocks.add(ground_mid_left1)
                        all_sprites.add(ground_mid_left1)
                    if game_map[i][j] == '9':
                        ground_bottom_mid1 = Block(block_size * j, block_size * i, ground_bottom_mid)
                        blocks.add(ground_bottom_mid1)
                        all_sprites.add(ground_bottom_mid1)
                    if game_map[i][j] == 'A':
                        ground_mid_right1 = Block(block_size * j, block_size * i, ground_mid_right)
                        blocks.add(ground_mid_right1)
                        all_sprites.add(ground_mid_right1)
                    if game_map[i][j] == 'B':
                        snow_mid_left1 = Block(block_size * j, block_size * i, snow_mid_left)
                        blocks.add(snow_mid_left1)
                        all_sprites.add(snow_mid_left1)
                    if game_map[i][j] == 'C':
                        ground_mid_left1 = Block(block_size * j, block_size * i, ground_mid_left)
                        blocks.add(ground_mid_left1)
                        all_sprites.add(ground_mid_left1)
                    if game_map[i][j] == 'D':
                        ground_bottom_right1 = Block(block_size * j, block_size * i, ground_bottom_right)
                        blocks.add(ground_bottom_right1)
                        all_sprites.add(ground_bottom_right1)
                    if game_map[i][j] == 'E':
                        platform_left1 = Block(block_size * j, block_size * i, platform_left)
                        blocks.add(platform_left1)
                        all_sprites.add(platform_left1)
                    if game_map[i][j] == 'F':
                        platform_mid1 = Block(block_size * j, block_size * i, platform_mid)
                        blocks.add(platform_mid1)
                        all_sprites.add(platform_mid1)
                    if game_map[i][j] == 'G':
                        platform_right1 = Block(block_size * j, block_size * i, platform_right)
                        blocks.add(platform_right1)
                        all_sprites.add(platform_right1)
                    if game_map[i][j] == 'I':
                        ice1 = Block(block_size * j, block_size * i, ice)
                        water_surf1 = Block(block_size * j, 8 + block_size * i, water_surf)
                        all_sprites.add(water_surf1)
                        blocks.add(ice1)
                        all_sprites.add(ice1)
                    if game_map[i][j] == 'i':
                        ice1 = Block(block_size * j, block_size * i, ice)
                        blocks.add(ice1)
                        all_sprites.add(ice1)
                    if game_map[i][j] == '=':
                        crate1 = Block(block_size * j, block_size * i, crate)
                        blocks.add(crate1)
                        all_sprites.add(crate1)
                    if game_map[i][j] == 'w':
                        water_surf1 = Block(block_size * j, block_size * i, water_surf)
                        all_sprites.add(water_surf1)
                    if game_map[i][j] == 'W':
                        water1 = Block(block_size * j, block_size * i, water)
                        all_sprites.add(water1)
                    if game_map[i][j] == 'b':
                        brick1 = Block(block_size * j, block_size * i, brick)
                        all_sprites.add(brick1)
                    if game_map[i][j] == '>':
                        sign1 = Block(block_size * j, block_size * i, sign)
                        all_sprites.add(sign1)
                    if game_map[i][j] == '-':
                        machinegun1 = Block(block_size * j, block_size * i, brick)
                        machinegun1.shooting = True
                        blocks.add(machinegun1)
                        all_sprites.add(machinegun1)
                    if game_map[i][j] == '0':
                        cloud1 = Block(block_size * j, block_size * i, cloud)
                        all_sprites.add(cloud1)
                    if game_map[i][j] == 't':
                        tree1 = Block(block_size * j, block_size * (i-1), tree)
                        all_sprites.add(tree1)
                    if game_map[i][j] == 'T':
                        trees1 = Block(block_size * j, block_size * (i-1), trees)
                        all_sprites.add(trees1)
                    if game_map[i][j] == 's':
                        stone1 = Block(block_size * j, block_size * i, stone)
                        all_sprites.add(stone1)
                    if game_map[i][j] == 'd':
                        brick1 = Block(block_size * j, block_size * i, brick)
                        door1 = Door(block_size * j, block_size * i, closed_door)
                        all_sprites.add(brick1)
                        all_sprites.add(door1)
                    if game_map[i][j] == 'c':
                        coin1 = Coin(block_size * j + coin_size//2, block_size * i + coin_size//2, coins_list[0])
                        coins.add(coin1)
                        all_sprites.add(coin1)
                    if game_map[i][j] == 'U':
                        case1 = Block(block_size*j, block_size * i, case)
                        case1.active = True
                        case1.gun = WeaponShotgun()
                        strong_boxes.add(case1)
                        all_sprites.add(case1)
                    if game_map[i][j] == 'S':
                        case1 = Block(block_size*j, block_size * i, case)
                        case1.active = True
                        case1.gun = WeaponMachineGun()
                        strong_boxes.add(case1)
                        all_sprites.add(case1)
                    if game_map[i][j] == 'h':
                        heart1 = Heart(block_size * j + coin_size//2, block_size * i + coin_size//2, heart_list[0])
                        hearts.add(heart1)
                        all_sprites.add(heart1)
                    if game_map[i][j] == 'j':
                        tramp1 = Block(block_size * j, block_size * i + block_size//2, trampoline)
                        tramp1.jump = True
                        blocks.add(tramp1)
                        all_sprites.add(tramp1)
                    if game_map[i][j] == '|':
                        event_blocks['boss'] = [block_size * j, False]

            for i in range(len(game_map)):
                for j in range(len(game_map[i])):
                    if game_map[i][j] == 'e':
                        gun = WeaponPistol()
                        mob = Mob(block_size * j, block_size * i, enemy_stay_left, enemy_stay_right, block_size, gun)
                        mobs.add(mob)
                        all_sprites.add(mob)
                        all_sprites.add(gun)

                    if game_map[i][j] == '#':
                        gun = WeaponShotgun()
                        boss1 = Boss(block_size * j, block_size * i, boss1_left, boss1_right, block_size, gun, 2)

                    if game_map[i][j] == '!':
                        gun = WeaponShotgun()
                        boss2 = Boss(block_size * j, block_size * i, boss2_left, boss2_right, block_size, gun, 2)

            gun = WeaponPistol()
            player = Player(gun, 0, 0)
            all_sprites.add(player)
            all_sprites.add(gun)

        game.menu()
        waiting_command += 1

    if state == state_play:
        if play_music_play:
            pygame.mixer.music.load('sound/TheFatRat_Epic.mp3')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.05)
            play_music_play = False

        if boss_music_play:
            pygame.mixer.music.load('sound/awesomeness.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.3)
            boss_music_play = False

        background_pos = (camera_x // 4) % WIDTH
        screen.blit(background_image, (background_pos - WIDTH, 0))
        screen.blit(background_image, (background_pos, 0))
        sound_gameover.stop()
        pygame.mixer.music.unpause()
        current_time = pygame.time.get_ticks()

        if player.gun.automate and current_time - timer_for_shooting > 1000 // player.gun.SPS:
            button_press_time = automate_shoot(player, current_time, button_press_time)
            timer_for_shooting = pygame.time.get_ticks()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player.gun.automate == False:
                    if (event.button == 1) and (current_time - button_press_time > player.gun.reload):
                        player.shoot()
                        button_press_time = pygame.time.get_ticks()

                if player.gun.automate == True:
                    if event.button == 1:
                        player.gun.automate_shooting = True
                        timer_for_shooting = pygame.time.get_ticks() - 100

            if event.type == pygame.MOUSEBUTTONUP:
                player.gun.automate_shooting = False

        all_sprites.update()
        collide(player, blocks)
        collide(player, door1)
        collide(player, coins)
        collide(player, hearts)
        collide(player, keys)
        collide(player, strong_boxes)
        collide(bullets, blocks)
        collide(mobs, blocks)
        collide(bullets_enemy, blocks)
        collide(player, bullets_enemy)
        collide(player, x_rays_enemy)
        collide(x_rays_enemy, blocks)
        collide(mobs, bullets)
        
        for key_i in event_blocks.keys():
            if key_i == 'boss' and player.rect.x > event_blocks[key_i][0] and event_blocks[key_i][1] == False:
                mobs.add(boss1)
                mobs.add(boss2)
                all_sprites.add(boss1)
                all_sprites.add(boss2)
                all_sprites.add(boss1.gun)
                all_sprites.add(boss2.gun)
                event_blocks[key_i][1] = True
                boss_music_play = True

            if key_i == 'key_have_been_fallen' and event_blocks[key_i][2]:
                key1 = Key(event_blocks[key_i][0], event_blocks[key_i][1], key_list[0])
                keys.add(key1)
                all_sprites.add(key1)
                event_blocks[key_i][2] = False 

            if key_i == 'free_Santa' and event_blocks[key_i][2]:
                santa = Santa(event_blocks[key_i][0], event_blocks[key_i][1], santa_stay_left, santa_stay_right, block_size, WeaponPistol())
                mobs.add(santa)
                all_sprites.add(santa)
                event_blocks[key_i][2] = False
                santa_got_free = pygame.time.get_ticks()
                pygame.mixer.Channel(5).play(sound_santa)

        for fanta in all_sprites:
            screen.blit(fanta.image, (fanta.rect.x + camera_x, fanta.rect.y + int(camera_y * 0.3)))

        player.show_points()
        player.show_keys()
        draw_shield_bar(120, 20, WIDTH-130, 10, player.health, player.all_health, GREEN)
        screen.blit(health, (WIDTH-165, 5))
        for m in mobs:
            try:
                if m == santa:
                    draw_shield_bar(60, 8, m.rect.x + camera_x, m.rect.y + int(camera_y * 0.3)-15, m.health, m.all_health, GREEN)
            except:
                if m == boss1 or m == boss2:
                    draw_shield_bar(90, 8, m.rect.x + camera_x, m.rect.y + int(camera_y * 0.3)-15, m.health, m.all_health, RED)
                else:
                    draw_shield_bar(60, 8, m.rect.x + camera_x, m.rect.y + int(camera_y * 0.3)-15, m.health, m.all_health, RED)

        if player.health <= 0:
            sound_gameover.play()
            state = state_game_over 

        if santa_got_free != 0 and pygame.time.get_ticks() - santa_got_free > 2000:
            state = state_game_win
            end_music_play = True

    if state == state_game_over:
        pygame.mixer.music.pause()
        screen.blit(text_game_over, (WIDTH//2 - 400, HEIGHT//2 - 100))
        screen.blit(text_start, (WIDTH // 2 - 200, HEIGHT // 2 + 100))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False
                if event.key == pygame.K_SPACE:
                    state = state_start
                    start_music_play = True
                    waiting_command = 0
                    for sprite in all_sprites:
                        sprite.kill()

    if state == state_game_win:
        if end_music_play:
            pygame.mixer.music.load('sound/Jingle_Bells.wav')
            pygame.mixer.music.play(-1)
            pygame.mixer.music.set_volume(0.1)
            end_music_play = False
            got_here = pygame.time.get_ticks()
        screen.blit(santa_head, ((WIDTH // 3) * 2, 10))
        screen.blit(text_thanks_1, (300, 70))
        screen.blit(text_thanks_2, (300, 70 + block_size // 2))
        screen.blit(text_thanks_3, (300, 70 + 2 * block_size // 2))
        if pygame.time.get_ticks() - got_here >= 2000:
            screen.blit(text_the_end, (370, 70 + 5 * block_size // 2))
        if pygame.time.get_ticks() - got_here >= 4000:
            for i in range(len(text_authors)):
                screen.blit(text_authors[i], (778, 500 + i * (block_size // 2)))
            screen.blit(text_authors7, (200, HEIGHT - 30))
            screen.blit(text_esc, (1050, HEIGHT - 30))
            screen.blit(logo, (370, 390))            
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    done = False

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()