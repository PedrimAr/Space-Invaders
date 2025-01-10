from PPlay.gameimage import GameImage
from PPlay.window import *
from PPlay.sprite import *
import random
from enemies import spawn_enemy

import atalho


def jogar(nivel):
    game_speed = 300 + nivel

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
    fase = 1
    pontos = 0

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
    enemies = [[0 for x in range(matriz_y)] for x in range(matriz_x)]
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

        for tiro in tiros_player:
            for linha in enemies:
                for coluna in linha:
                    if coluna != 0 and tiro.collided(coluna):
                        linha.remove(coluna)  # Remove o inimigo da matriz
                        if tiro in tiros_player:
                            tiros_player.remove(tiro)  # Remove o tiro correspondente

        for tiro in tiros_enemies:
            if tiro.collided(nave):
                tiros_enemies.remove(tiro)
                vida -= 1

        limite_direito = 0
        limite_esquerdo = 0

        # Movimentação dos inimigos (horizontal)
        if not all(len(linha) == 0 for linha in enemies):
            limite_esquerdo = min(coluna.x for linha in enemies for coluna in linha if coluna != 0)
            limite_direito = max(coluna.x + coluna.width for linha in enemies for coluna in linha if coluna != 0)

        atingiu_borda = False
        # Verifica se os inimigos chegaram nas bordas da janela
        if limite_esquerdo <= 0 or limite_direito >= janela.width:
            direcao_inimigos *= -1  # Inverte a direção
            atingiu_borda = True

        # Move os inimigos horizontalmente
        for linha in enemies:
            for coluna in linha:
                if coluna != 0:
                    if atingiu_borda:
                        coluna.move_y(10)
                    coluna.move_x(direcao_inimigos * 100 * delta)  # Velocidade de 100 px/s

        # Desenho dos inimigos
        if all(len(linha) == 0 for linha in enemies):
            fase += 1
            pontos += int(100/tempo)
            if fase < 4:
                matriz_x += 1  # Aumenta o número de linhas
                matriz_y += 1  # Aumenta o número de colunas
            enemies = [[0 for _ in range(matriz_y)] for _ in range(matriz_x)]
            enemies = spawn_enemy(matriz_x, matriz_y, enemies)
            game_speed += 50  # Aumenta a velocidade para deixar mais difícil
        else:
            for linha in enemies:
                for coluna in linha:
                    coluna.draw()

        # Desenho dos tiros do player
        for tiro in tiros_player:
            if tiro:
                tiro.draw()

        # Controle de disparo dos enemies
        a = int(random.uniform(0, matriz_x))
        b = int(random.uniform(0, matriz_y))
        inimigos_vivos = [coluna for linha in enemies for coluna in linha if coluna != 0]

        if inimigos_vivos and janela.time_elapsed() - ultimo_tiro_enemies > (
                cooldown_enemies + int(random.uniform(-0.7, 0.3))) * 1000:
            inimigo_aleatorio = random.choice(inimigos_vivos)
            tiro_enemies = Sprite("png/tiro_inimigo.png")
            tiro_enemies.set_position(inimigo_aleatorio.x + inimigo_aleatorio.width / 2 - tiro_enemies.width / 2, inimigo_aleatorio.y + tiro_enemies.height)
            tiros_enemies.append(tiro_enemies)
            ultimo_tiro_enemies = janela.time_elapsed()

        # Desenho dos tiros dos enemies
        for tiro in tiros_enemies:
            tiro.draw()

        # Verifica se morreu
        if vida <= 0:
            nome = str(input("Digite seu nome para salvar sua pontuação: "))
            salvar_ranking(nome, pontos)
            while True:  # Loop da tela de Game Over
                janela.set_background_color((0, 0, 0))  # Fundo preto
                janela.draw_text("GAME OVER", janela.width / 2 - 100, janela.height / 2 - 50, size=40,
                                 color=(255, 0, 0))
                janela.draw_text("Pressione ESC para sair ou R para reiniciar", janela.width / 2 - 150,
                                 janela.height / 2 + 20, size=20, color=(255, 255, 255))
                janela.update()

                # Controle de reinício ou saída
                if teclado.key_pressed("ESC"):
                    return  # Sai do loop e volta ao menu
                elif teclado.key_pressed("R"):
                    jogar(nivel)  # Reinicia o jogo
                    return

        janela.draw_text(f"FPS: {fps}", janela.width - 100, 20, 20, (255, 255, 255))
        janela.draw_text(f"VIDAS: {vida}", janela.width - 120, 50, 20, (255, 255, 255))
        janela.draw_text(f"FASE: {fase}", janela.width - 120, 80, 20, (255, 255, 255))
        janela.draw_text(f"PONTOS: {pontos}", janela.width - 120, 110, 20, (255, 255, 255))

        m_ficar = atalho.sair()
        janela.update()


def salvar_ranking(nome, pontos, arquivo="ranking.txt"):
    with open(arquivo, "a") as file:  # Abre o arquivo no modo de append
        file.write(f"Nome: {nome}, Pontos: {pontos}\n")

