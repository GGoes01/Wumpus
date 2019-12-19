from Agente import Agente
from Fitness import Fitness as fit
import random


class Populacao:
    def __init__(self, quantidade, geracao, tamanho):
        self.__quantidade = quantidade
        self.__geracao = geracao
        self.__tamanho = tamanho

    def gerar_populacao(self):
        vetor_populacao = []

        for contador in range(self.__quantidade):
            celula = Agente(random.randint(0, self.__tamanho**2))
            celula.set_movimento(celula.gerar_movimento())

            fitness, pontuacao = celula.pecado_inicial(celula)

            celula.set_pontucao(pontuacao)
            celula.set_fitness(fitness)

            vetor_populacao.append(celula)

            for cel in vetor_populacao:
                indice = vetor_populacao.index(cel)
                id = str(self.__geracao) + '_00_' + str(indice)
                cel.set_id(id)

        return vetor_populacao
