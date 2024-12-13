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

    vida = 5

    tiros_player = []
    cooldown_player = 0.5
    ultimo_tiro_player = 0

    tiros_enemies = []
    cooldown_enemies = 0.7
    ultimo_tiro_enemies = 0

    # Tamanho limite da matriz de inimigos
    max_size = 5

    # Número de linhas e colunas da matriz de inimigos
    matriz_x = int(random.uniform(2, max_size))
    matriz_y = int(random.uniform(3, max_size))

    # Definição da matriz de inimigos
    enemies = [[0 for x in range(matriz_x + 1)] for x in range(matriz_y + 1)]
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

        janela.draw_text("FPS: " + str(fps), janela.width - 100, 20, 20, (255, 255, 255))
        janela.draw_text("VIDAS: " + str(vida), janela.width - 120, 50, 20, (255, 255, 255))

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

        # Controle de disparo do player
        if teclado.key_pressed("SPACE") and janela.time_elapsed() - ultimo_tiro_player > cooldown_player * 1000:
            tiro_player = Sprite("png/tiro.png")
            tiro_player.set_position(nave.x + nave.width / 2 - tiro_player.width / 2, nave.y - tiro_player.height)
            tiros_player.append(tiro_player)
            ultimo_tiro_player = janela.time_elapsed()

        # Controle de disparo dos enemies
        if janela.time_elapsed() - ultimo_tiro_enemies > (cooldown_enemies + int(random.uniform(-0.7, 0.3))) * 1000:
            tiro_enemies = Sprite("png/tiro_inimigo.png")
            a = int(random.uniform(0, matriz_x))
            b = int(random.uniform(0, matriz_y))
            tiro_enemies.set_position(enemies[a][b].x + nave.width / 2 - tiro_enemies.width / 2, enemies[a][b].y - tiro_enemies.height)
            tiros_enemies.append(tiro_enemies)
            ultimo_tiro_enemies = janela.time_elapsed()


        # Movimentação dos projéteis do player
        for tiro in tiros_player:
            tiro.move_y(-300 * delta)
            if tiro.y + tiro.height < 0:
                tiros_player.remove(tiro)

        # Movimentação dos projéteis dos enemies
        for tiro in tiros_enemies:
            tiro.move_y(300 * delta)
            if tiro.y > janela.height:
                tiros_enemies.remove(tiro)



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

        for tiro in tiros_player:
            if tiro.y <= enemies[matriz_x - 1][matriz_y - 1].y + enemies[matriz_x - 1][matriz_y - 1].height:
                for linha in range(matriz_x):
                    for coluna in range(matriz_y):
                        inimigo = enemies[linha][coluna]
                        if tiro.collided(inimigo):
                            enemies[linha][coluna] = 0
                            tiro = 0

        for tiro in tiros_enemies:
            if tiro.collided(nave):
                tiros_enemies.remove(tiro)
                vida -= 1

        # Desenho dos inimigos
        for linha in range(matriz_x):
            for coluna in range(matriz_y):
                if enemies[linha][coluna] != 0:
                    enemies[linha][coluna].draw()

        # Desenho dos tiros do player
        for tiro in tiros_player:
            if tiro != 0:
                tiro.draw()

        # Desenho dos tiros dos enemies
        for tiro in tiros_enemies:
            if tiro != 0:
                tiro.draw()

        m_ficar = atalho.sair()
        janela.update()