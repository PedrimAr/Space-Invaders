# Imports
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *
from PPlay.mouse import *
from PPlay.keyboard import *

# Definição de janela (900, 600)
janela = Window(900, 600)

# Definição da tela de fundo
fundo = GameImage("imagens/fundoGalaxia.png")

# Definição do input do mouse como variável
mouse = Mouse()

# Definição do input do teclado como variável
teclado = Keyboard()

# Definição da Sprite dos botões
botao_1 = Sprite("imagens/botao.png")
botao_1.x = janela.width / 2 - botao_1.width / 2
botao_1.y = 150

botao_2 = Sprite("imagens/botao.png")
botao_2.x = janela.width / 2 - botao_2.width / 2
botao_2.y = 250

botao_3 = Sprite("imagens/botao.png")
botao_3.x = janela.width / 2 - botao_3.width / 2
botao_3.y = 350

botao_4 = Sprite("imagens/botao.png")
botao_4.x = janela.width / 2 - botao_4.width / 2
botao_4.y = 450

# Definição da variável referente ao estado do jogo (0 = Menu, 1 = Gameplay, 2 = Tela de dificuldade)
estado = 0

# Game Loop
while True:
    if estado != 1:
        # Desenho da tela de fundo
        fundo.draw()

        # Escrita do título
        janela.draw_text("Space Invaders", janela.width / 2 - 175, 30, 50, (255, 255, 255), "Arial", True, True)

        # Desenho dos botões
        botao_1.draw()
        botao_2.draw()
        botao_3.draw()
        botao_4.draw()

        # Seleção do botão "Sair"
        if mouse.is_over_object(botao_4) and mouse.is_button_pressed(1):
            janela.close()

        if estado == 0:
            # Escrita dos botões
            janela.draw_text("Jogar", janela.width / 2 - 35, 155, 30, (255, 255, 255), "Arial")
            janela.draw_text("Dificuldade", janela.width / 2 - 60, 255, 30, (255, 255, 255), "Arial")
            janela.draw_text("Ranking", janela.width / 2 - 45, 355, 30, (255, 255, 255), "Arial")
            janela.draw_text("Sair", janela.width / 2 - 25, 455, 30, (255, 255, 255), "Arial")

            # Seleção do botão "Sair"
            if mouse.is_over_object(botao_4) and mouse.is_button_pressed(1):
                janela.close()

            # Seleção do botão "Jogar"
            elif mouse.is_over_object(botao_1) and mouse.is_button_pressed(1):
                estado = 1

            # Seleção do botão "Dificuldade"
            elif mouse.is_over_object(botao_2) and mouse.is_button_pressed(1):
                estado = 2

        if estado == 2:
            # Escrita dos botões de dificuldade
            janela.draw_text("Fácil", janela.width / 2 - 30, 155, 30, (255, 255, 255), "Arial")
            janela.draw_text("Médio", janela.width / 2 - 35, 255, 30, (255, 255, 255), "Arial")
            janela.draw_text("Difícil", janela.width / 2 - 35, 355, 30, (255, 255, 255), "Arial")
            janela.draw_text("Sair", janela.width / 2 - 25, 455, 30, (255, 255, 255), "Arial")

            # Ao pressionar Esc, volta ao Menu
            if teclado.key_pressed("esc"):
                estado = 0

    if estado == 1:
        janela.set_background_color([0, 0, 0])

        # Ao pressionar Esc, volta ao Menu
        if teclado.key_pressed("esc"):
            estado = 0

    # Update da janela
    janela.update()
