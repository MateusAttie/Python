import pygame
from pygame.locals import *
from sys import exit, path
path.append("../lib/")
from simpvectlib import *
from math import *
import socket
import time
#TCP_IP = '192.168.43.208'
#TCP_PORT = 8090
TCP_IP = 'localhost'
TCP_PORT = 8090
BUFFER_SIZE = 1024
MESSAGE = 'stop'
prev_msg = 'start'
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

background_image_filename = '../assets/bcg.bmp'
sprite_image_filename = '../assets/car_sprite.png'

pygame.init()
screen = pygame.display.set_mode((640, 480), 0, 32)

background = pygame.image.load(background_image_filename).convert()
sprite = pygame.image.load(sprite_image_filename).convert_alpha()

clock = pygame.time.Clock()

sprite_pos = Vector2d(0,0)
sprite_speed = 120
sprite_rotation = 0
sprite_rotation_speed = 150


while 1==1:
    for event in pygame.event.get():
        if event.type == QUIT:
            s.close()
            pygame.quit()
            exit()
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                s.close()
                pygame.quit()
                exit
    pressed_keys = pygame.key.get_pressed()

    rotation_direction = 0
    movement_direction = 0

    if pressed_keys[K_UP]:
        movement_direction = 1
        MESSAGE = "front"
        
        
    elif pressed_keys[K_DOWN]:
        movement_direction = -1
        MESSAGE = "back"
        
        
    elif pressed_keys[K_LEFT]:
        rotation_direction=1
        MESSAGE = "left"
        
        
    elif pressed_keys[K_RIGHT]:
        rotation_direction=-1
        MESSAGE = "right"
        
    if not (pressed_keys[K_UP] or pressed_keys[K_DOWN] or pressed_keys[K_LEFT] or pressed_keys[K_RIGHT]):
        MESSAGE = "stop"
        
        
    if MESSAGE != prev_msg:
        if MESSAGE == "stop":
            time.sleep(0.4)
        s.sendto(MESSAGE.encode('utf-8'),(TCP_IP, TCP_PORT))
        prev_msg = MESSAGE
    
    screen.blit(background, (0,0))
    rotate_sprite =pygame.transform.rotate(sprite, sprite_rotation)
    w, h = rotate_sprite.get_size()
    sprite_draw_pos = Vector2d(sprite_pos.x-w/2, sprite_pos.y-h/2)
    screen.blit(rotate_sprite, (sprite_draw_pos.x, sprite_draw_pos.y))
    
    time_passed = clock.tick(30)
    time_passed_seconds = time_passed/1000.0

    sprite_rotation += rotation_direction * sprite_rotation_speed * time_passed_seconds

    heading_x = sin(sprite_rotation*pi/180.0)
    heading_y = cos(sprite_rotation*pi/180.0)
    heading=Vector2d(heading_x,heading_y)
    heading *= movement_direction

    sprite_pos = sprite_pos + heading * sprite_speed * time_passed_seconds
    sprite_pos.check(640,480)
    
    pygame.display.update()
    
