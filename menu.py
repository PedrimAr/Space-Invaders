from PPlay.window import *
from PPlay.sprite import *

import jogar
import dificuldade
import atalho


janela = Window(537, 457)
janela.set_title("Space Invaders - Paulo Mota e Pedro Rangel")

mouse = janela.get_mouse()

menu = Sprite("png/menu.png", 1)
menu.x = 0
menu.y = 0

# sprites dos botões
btn_jogar = Sprite("png/jogar.png", 1)
btn_difi = Sprite("png/dificuldade.png", 1)
btn_ranking = Sprite("png/ranking.png", 1)
btn_sair = Sprite("png/sair.png", 1)

# variaveis que vão alterar a tela
ini_jogar = False
ini_difi = False
ini_rank = False
b_sair_do_jogo = False

troca_timer = 0

# nivel de dificuldade
nivel = 2

pontuacao = None

while not b_sair_do_jogo:

    janela.set_title("Space Invaders - Paulo Mota")
    menu.draw()

    # se o mouse "está sobre o botão", exibe o botão iluminado //
    # se "botão é pressionado" ativa o inicializador de troca de tela
    if mouse.is_over_area([95, 215], [440, 255]):
        atalho.posicao(btn_jogar, 95, 215)
        if mouse.is_button_pressed(1):
            ini_jogar = True

    # Verifica se pressionou o botaode de defilculdade
    if mouse.is_over_area([95, 265], [440, 305]):
        atalho.posicao(btn_difi, 95, 265)
        if mouse.is_button_pressed(1):
            ini_difi = True

    # Verifica se pressionou o botaode de ranking
    if mouse.is_over_area([95, 315], [440, 355]):
        atalho.posicao(btn_ranking, 95, 315)
        if mouse.is_button_pressed(1):
            ini_rank = True

    # Verifica se pressionou o botaode sair
    if mouse.is_over_area([95, 365], [440, 405]):
        atalho.posicao(btn_sair, 95, 365)
        if mouse.is_button_pressed(1):
            b_sair_do_jogo = True

    # ativa a outra tela
    if ini_jogar or ini_difi or ini_rank:
        troca_timer += janela.delta_time()

        if troca_timer >= 1 and ini_jogar:
            jogar.jogar()
            ini_jogar = False
            troca_timer = 0

        if troca_timer >= 1 and ini_difi:
            nivel = dificuldade.tela()
            ini_difi = False
            troca_timer = 0

    janela.update()



