from PPlay.gameimage import GameImage
from PPlay.window import *
from PPlay.sprite import *
import random
from enemies import spawn_enemy

import atalho

game_speed = 400

def jogar():
    # entra num game loop vazio, que sai novamente para o menu ao pressionar ESC
    janela = Window(537, 457)
    janela.set_title("ATENÇÃO, hora de atirar! ESC para voltar ao menu inicial!")

    # Definição da imagem de fundo
    fundo = GameImage("png/fundo_jogar.jpg")

    # Definição do sprite de nave
    nave = Sprite("png/nave.png", 1)
    nave.x = janela.width / 2 - nave.width / 2
    nave.y = janela.height - nave.height
    vel_nave = game_speed

    # Definição do sprite de nave inimiga
    enemy = Sprite("png/nave_inimiga.png", 1)
    vel_enemy = game_speed
    dir_enemy = 1

    enemy_shoot_delay = 1 / game_speed
    nave.shoot_delay = 1 / game_speed * 0.5
    nave.shoot_tick = nave.shoot_delay

    # Tamanho limite da matriz de inimigos
    max_size = 10

    # Número de linhas e colunas da matriz de inimigos
    matriz_x = int(random.uniform(3, max_size))
    matriz_y = int(random.uniform(1, max_size))

    # Definição da matriz de inimigos
    enemies = [[0 for x in range(10)] for x in range(10)]
    enemies = spawn_enemy(matriz_x, matriz_y, enemies)

    # Estabelecendo input do teclado
    teclado = Window.get_keyboard()

    m_ficar = True

    while m_ficar:
        # Desenho da imagem de fundo
        fundo.draw()

        # Desenho da nave
        nave.draw()

        # Movimentação horizontal da nave
        if teclado.key_pressed("a") and nave.x >= 0:
            nave.move_x(-1 * vel_nave * janela.delta_time())
        elif teclado.key_pressed("d") and nave.x <= janela.width - nave.width:
            nave.move_x(vel_nave * janela.delta_time())

        for linha in range(matriz_x):
            for coluna in range(matriz_y):
                if enemies[linha][coluna] != 0:
                    enemies[linha][coluna].draw()

        m_ficar = atalho.sair()
        janela.update()
