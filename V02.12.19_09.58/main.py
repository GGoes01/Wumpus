from AmbienteBruto import Ambiente
from Agente import Agente
from Mundo_de_Wumpus import Jogo
import random
from Casa import Casa
from Populacao import Populacao
from Memoria import Memoria as mem
from Fitness import Fitness as fit


jogo = Jogo(1000, 4)
jogo.executar()
