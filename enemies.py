from PPlay.sprite import *
import random

game_speed = 400


def spawn_enemy(i, j, matriz_enemies):
    boss_x = int(random.uniform(0, i - 1))
    boss_y = int(random.uniform(0, j - 1))
    for x in range(i):
        for y in range(j):
            if x == boss_x and y == boss_y:
                enemy = Sprite("png/nave_boss.png", 1)
                enemy.life = 2
            else:
                enemy = Sprite("png/nave_inimiga.png", 1)
                enemy.life = 1

            enemy.set_position(x * (enemy.width + 10) + 50, y * (enemy.height + 10) + 10)
            # Define a direção do movimento, no caso para baixo
            enemy.direction = 1
            # Define randomicamente o intervalo entre os disparos
            enemy.shoot_delay = random.uniform(0, 15) / game_speed
            # Zera a variável de controle de disparos
            enemy.shoot_tick = 0
            # Coloca o inimigo recém criado na matriz
            matriz_enemies[x][y] = enemy

    return matriz_enemies
