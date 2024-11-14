# Imports
from PPlay.window import *
from PPlay.sprite import *
from PPlay.gameimage import *

# Definição de janela (900, 600)
janela = Window(900, 600)

# Definição da tela de fundo
fundo = GameImage("imagens/fundoGalaxia.png")

# Game Loop
while True:
    fundo.draw()
    janela.update()
