from PPlay.window import *
from PPlay.sprite import *

janela = Window(537, 457)
tecla = janela.get_keyboard()


# economiza linhas pra desenhar e posicionar os botões do menu
def posicao(sprite, X, Y):
    sprite.x = X
    sprite.y = Y
    sprite.draw()


# fecha a tela quando pressiona esc
def sair():
    if tecla.key_pressed("ESC"):
        return False
    else:
        return True

