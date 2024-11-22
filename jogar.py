from PPlay.gameimage import GameImage
from PPlay.window import *
from PPlay.sprite import *

import atalho

def jogar():
    # entra num game loop vazio, que sai novamente para o menu ao pressionar ESC
    janela = Window(537, 457)
    janela.set_title("ATENÇÃO, hora de atirar! ESC para voltar ao menu inicial!")

    # Definição da imagem de fundo
    fundo = GameImage("png/fundo_jogar.jpg")

    # Definição do sprite de nave
    nave = Sprite('png/nave.png', 1)
    nave.x = janela.width / 2 - nave.width / 2
    nave.y = janela.height - nave.height
    velX = velY = 400

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
            nave.move_x(-1 * velX * janela.delta_time())
        elif teclado.key_pressed("d") and nave.x <= janela.width - nave.width:
            nave.move_x(velX * janela.delta_time())


        m_ficar = atalho.sair()
        janela.update()
