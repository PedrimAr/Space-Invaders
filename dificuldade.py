from PPlay.window import *
from PPlay.sprite import *

import atalho


def tela():
    janela = Window(537, 457)
    janela.set_title("Dificuldade")

    dificuldade = Sprite("png/tela-difi.png", 1)
    dificuldade.x = 0
    dificuldade.y = 0

    mouse = janela.get_mouse()
    tecla = janela.get_keyboard()

    btn_facil = Sprite("png/facil.png", 1)
    btn_medio = Sprite("png/medio.png", 1)
    btn_dificil = Sprite("png/dificil.png", 1)

    m_ficar = True

    sair_difi = False
    escolhida_difi = 0

    troca_timer = 0

    while m_ficar:

        dificuldade.draw()

        m_ficar = atalho.sair()

        if mouse.is_over_area([95, 215], [440, 255]):
            atalho.posicao(btn_facil, 95, 215)
            if mouse.is_button_pressed(1):
                sair_difi = True

        if mouse.is_over_area([95, 265], [440, 305]):
            atalho.posicao(btn_medio, 95, 265)
            if mouse.is_button_pressed(1):
                escolhida_difi = 50
                sair_difi = True

        if mouse.is_over_area([95, 315], [440, 355]):
            atalho.posicao(btn_dificil, 95, 315)
            if mouse.is_button_pressed(1):
                escolhida_difi = 100
                sair_difi = True

        if sair_difi:
            troca_timer += janela.delta_time()
            if troca_timer >= 1:
                return escolhida_difi

        janela.update()

