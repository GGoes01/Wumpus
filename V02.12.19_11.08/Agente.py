from AmbienteBruto import Ambiente as amb
from Fitness import Fitness as fit
import random


class Agente:

    def __init__(self, tamanho_caminho):
        self.__vida = True
        self.__ouro = False
        self.__flecha = True
        self.__id = ''
        self.__fitness = 0
        self.__tamanho = tamanho_caminho
        self.__movimento = []
        self.__pontuacao = 0
        self.__movimentos_validos = []
        self.__caminho_percorrido = []
        self.__sense = []

    def viver(self):
        self.__vida = True

    def get_vida(self):
        return self.__vida

    def pegar_ouro(self):
        self.__ouro = True
        self.set_pontucao(300)

    def morrer(self):
        self.__vida = False
        self.set_pontucao(-25)

    def gerar_movimento(self):
        poss = ['n', 's', 'l', 'o', 'p', 'fn', 'fs', 'fl', 'fo']
        movimento = []

        for x in range(self.__tamanho):
            movimento.append(random.choice(poss))

        return movimento

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_fitness(self):
        return self.__fitness

    def set_fitness(self, fitness):
        self.__fitness = fitness

    def get_tamanho(self):
        return self.__tamanho

    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho

    def get_movimento(self):
        return self.__movimento

    def set_movimento(self, movimento):
        self.__movimento = list(movimento)

    def get_pontuacao(self):
        return self.__pontuacao

    def set_pontucao(self, valor):
        self.__pontuacao += valor

    def reset_pontuacao(self):
        self.__pontuacao = 0

    def get_nice_moves(self):
        return self.__movimentos_validos

    def set_nice_moves(self, indice):
        self.__movimentos_validos.append(indice)

    def reset_nice_moves(self):
        self.__movimentos_validos = []

    def get_caminho_percorrido(self):
        return self.__caminho_percorrido

    def add_caminho_percorrido(self, casa):
        self.__caminho_percorrido.append(casa)

    def get_sense(self):
        return self.__sense

    def set_sense(self, sense):
        self.__sense = sense

    def pecado_inicial(self, celula):
        movimento = celula.get_movimento()
        penalidade = 0

        num_pegar = movimento.count('p')
        num_disparos = movimento.count('fn') + movimento.count('fs') + movimento.count('fl') + movimento.count('fo')

        if num_pegar != 1 or num_disparos != 1:
            penalidade = -1000 * (num_disparos + num_pegar)

        if num_pegar == 1 and num_disparos == 1:

            penalidade = 25

        fitness = fit(penalidade, 0)

        return fitness.calcular_fitness(), penalidade
