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

    tiros = []
    cooldown_tiro = 0.5
    tempo_ultimo_tiro = 0

    # Tamanho limite da matriz de inimigos
    max_size = 5

    # Número de linhas e colunas da matriz de inimigos
    matriz_x = int(random.uniform(2, max_size))
    matriz_y = int(random.uniform(3, max_size))

    # Definição da matriz de inimigos
    enemies = [[None for x in range(10)] for x in range(10)]
    enemies = spawn_enemy(matriz_x, matriz_y, enemies)
    direcao_inimigos = 1

    # Estabelecendo input do teclado
    teclado = Window.get_keyboard()

    m_ficar = True

    frames = 0
    tempo = 0
    fps = 0

    while m_ficar:
        # Desenho da imagem de fundo
        fundo.draw()

        # Desenho da nave
        nave.draw()

        delta = janela.delta_time()
        tempo += delta
        frames += 1
        if tempo >= 1.0:
            fps = frames
            frames = 0
            tempo = 0

        janela.draw_text(str(fps), janela.width - 50, 20, 20, (255, 255, 255))

        # Movimentação horizontal da nave
        if teclado.key_pressed("a") and nave.x >= 0:
            nave.move_x(-1 * vel_nave * janela.delta_time())
        elif teclado.key_pressed("d") and nave.x <= janela.width - nave.width:
            nave.move_x(vel_nave * janela.delta_time())

        # Movimentação vertical da nave
        if teclado.key_pressed("w") and nave.y >= 0:
            nave.move_y(-1 * vel_nave * janela.delta_time())
        elif teclado.key_pressed("s") and nave.y <= janela.height - nave.height:
            nave.move_y((vel_nave * janela.delta_time()))

        # Controle de disparo
        if teclado.key_pressed("SPACE") and janela.time_elapsed() - tempo_ultimo_tiro > cooldown_tiro * 1000:
            tiro = Sprite("png/tiro.png")
            tiro.set_position(nave.x + nave.width / 2 - tiro.width / 2, nave.y - tiro.height)
            tiros.append(tiro)
            tempo_ultimo_tiro = janela.time_elapsed()

        # Movimentação dos projéteis
        for tiro in tiros[:]:
            tiro.move_y(-300 * delta)
            if tiro.y + tiro.height < 0:
                tiros.remove(tiro)

        '''
        # Movimentação dos inimigos
        move_y = False
        for linha in range(matriz_x):
            for coluna in range(matriz_y):
                if enemies[linha][coluna].x + enemies[linha][coluna].width >= janela.width or enemies[linha][coluna].x <= 0:
                    direcao_inimigos *= -1
                    move_y = True
                    break

        for linha in range(matriz_x):
            for coluna in range(matriz_y):
                enemies[linha][coluna].move_x(direcao_inimigos * game_speed * delta)
                if move_y:
                    enemies[linha][coluna].move_y(10)
        '''

        for tiro in tiros[:]:
            if tiro.y <= enemies[matriz_x - 1][matriz_y - 1].y + enemies[matriz_x - 1][matriz_y - 1].height:
                for linha in range(matriz_x):
                    for coluna in range(matriz_y):
                        inimigo = enemies[linha][coluna]
                        if tiro.collided(inimigo):
                            enemies[linha][coluna] = None
                            tiro = 0

        # Desenho dos inimigos
        for linha in range(matriz_x):
            for coluna in range(matriz_y):
                if enemies[linha][coluna] != None:
                    enemies[linha][coluna].draw()

        # Desenho dos tiros
        for tiro in tiros:
            if tiro != 0:
                tiro.draw()

        m_ficar = atalho.sair()
        janela.update()