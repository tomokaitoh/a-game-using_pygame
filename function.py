import sys
import pygame
import random
from object import gameObject
from setting import Settings

setting = Settings()

# 检测玩家方块与砖块之间是否接触或者碰撞


def cheak_objects(screen, character, objects, score):
    x1 = character.rect.x
    y1 = character.rect.y
    l1 = character.rect.width
    h1 = character.rect.height
    # 删除已经超过游戏边界的砖块并在最上面新增一个
    if objects[-1].rect.y >= setting.screen_height:
        del objects[-1]
        if random.randint(0, 4):
            objects.insert(0, gameObject(screen, random.randint(
                0, setting.screen_width-110), 0, 110, 20, gameObject.TYPE_BLOCK))
            character.on_N_of_Block += 1
        score[0] = score[0] + 10

    # 如果两个砖块间太远，附加跳跃提升效果
    if len(objects) > 1 and len(objects) > character.on_N_of_Block:
        if objects[character.on_N_of_Block].rect.y-objects[character.on_N_of_Block-1].rect.y >= 0.3*setting.screen_height:
            character.jump_v = 1.5*setting.character['jump_v']
            if objects[character.on_N_of_Block].rect.y-objects[character.on_N_of_Block-1].rect.y >= 0.5*setting.screen_height:
                character.jump_v = 1.8*setting.character['jump_v']
        else:
            character.jump_v = setting.character['jump_v']
    # 在玩家方块所在砖块上绘制一条边界线
    if character.onBlock and len(objects) > character.on_N_of_Block+1:
        pygame.draw.rect(screen, (153, 204, 255), (0,
                                                   objects[character.on_N_of_Block].rect.y, setting.screen_width, 5), 0)
    # 遍历所有砖块
    i = 0
    for object in objects:
        x2 = object.rect.x
        y2 = object.rect.y
        l2 = object.rect.width
        h2 = object.rect.height

        # 是否发生水平方向碰撞
        if (y1 > (y2-h1) and y1 < (y2+h2)):
            if (x1 < x2 and x2-x1 < l1):
                character.rect.x = x2-l1
                character.direction['x'] = 0
            elif (x1 > x2+l2-l1 and x1 < x2+l2):
                character.rect.x = x2+l2
                character.direction['x'] = 0

        # 如果玩家方块不在砖块上，检测是否发生竖直方向碰撞
        if character.onBlock == False:
            if x1 < x2+l2 and x1 > x2-l1:
                # 是否在砖块上方碰撞
                if y2 > y1 and y1 >= y2-h1:
                    if y2-y1 != h1:
                        character.rect.y = y2-h1
                        character.direction['y'] = 0
                        character.on_N_of_Block = i
                        character.onBlock = True
                    break
                # 是否在砖块下方碰撞
                elif y2 < y1 and y1-y2 < h2:
                    character.direction['y'] = -character.direction['y']
                    character.rect.y = y2+h2
                    break
        i += 1

# 检测玩家方块是否gameover


def cheak_gameover(character):
    if character.rect.bottom >= setting.screen_height:
        return True
    else:
        return False


def drawObject(objects):
    for object in objects:
        object.draw()

# 将玩家方块和砖块一起向下移动


def moveAll(character, objects, l):
    if character.onBlock:
        character.rect.y += l
    for object in objects:
        object.rect.y += l

# 按键按下事件


def cheak_keydown_event(event, character):
    if event.key == pygame.K_d:
        character.direction['x'] += 10
    if event.key == pygame.K_a:
        character.direction['x'] -= 10
    if event.key == pygame.K_w:
        if character.onBlock:
            character.onBlock = False
            character.direction['y'] -= character.jump_v

# 按键弹起事件


def cheak_keyup_event(event, character):
    if event.key == pygame.K_d:
        if character.direction['x'] != 0:
            character.direction['x'] -= 10
    if event.key == pygame.K_a:
        if character.direction['x'] != 0:
            character.direction['x'] += 10

# 事件监听


def cheak_event(character):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            cheak_keydown_event(event, character)
        elif event.type == pygame.KEYUP:
            cheak_keyup_event(event, character)
        elif event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
