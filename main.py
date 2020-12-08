import function as f  # 游戏内各种方法
import pygame
import sys
import os
import time
import random
import tkinter
from tkinter import messagebox
from button import Button  # 按钮类
from setting import Settings  # 游戏设置
from characters import Character
from object import gameObject

settings = Settings()


def menu():
    opinion = 0
    os.environ['SDL_VIDEO_CENTERED'] = '1'  # 窗口居中显示
    # 菜单界面初始化
    pygame.init()
    screen = pygame.display.set_mode(
        (320, 350))
    pygame.display.set_caption("Game of pygame")
    screen.fill((240, 240, 240))
    button1 = Button(screen, "Start game", 80, 120, 140, 50,text_size=18)
    button2 = Button(screen, "How to play", 80, 200, 140, 50,text_size=18)
    button3 = Button(screen, "Exit", 80, 280, 140, 50,text_size=18)
    button1.draw()
    button2.draw()
    button3.draw()
    pygame.display.flip()
    # 按钮事件监听
    while True:
        if opinion == 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT or button3.check_click(event):
                pygame.quit()
                sys.exit(0)
                break
            if button1.check_click(event):
                opinion = 1
                break
            if button2.check_click(event):
                top = tkinter.Tk()
                top.withdraw()
                top.update()
                tkinter.messagebox.showinfo(
                    'How to play', "Press 'W' to jump,\nPress 'A' and 'D' to move left and right.\nPress 'Q' to exit game.")
                top.destroy()
                break
        time.sleep(0.1)
    pygame.quit()


def start_game():
    # 初始化游戏界面
    pygame.init()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height))
    block = gameObject(screen, 0, 0, 110, 30, gameObject.TYPE_BLOCK)
    objects = []
    for i in range(0, settings.screen_height, 60):
        objects.append(gameObject(screen, random.randint(
            0, settings.screen_width-block.rect.width), i, 110, 20, gameObject.TYPE_BLOCK))
    character = Character(
        settings, screen, objects[-4].rect.x, objects[-4].rect.y-settings.character['size'])
    pygame.display.set_caption("Game of pygame")
    score = [0]  # 游戏分数 （因为函数不能改变int类型的值，所以这里用列表代替）
    # 游戏循环
    while True:
        screen.fill(settings.bg_color)
        f.cheak_event(character)
        f.cheak_objects(screen, character, objects, score)
        if f.cheak_gameover(character):
            top = tkinter.Tk()
            top.withdraw()
            top.update()
            tkinter.messagebox.showinfo(
                'Your Score', "Your score is "+str(score[0])+".")
            top.destroy()
            break
        f.drawObject(objects)
        character.draw()
        f.printData(screen,score,character)
        character.move()
        f.moveAll(character, objects, 2)
        pygame.display.flip()
        time.sleep(settings.pause)

while(1):
    menu()
    time.sleep(1.2)
    start_game()
