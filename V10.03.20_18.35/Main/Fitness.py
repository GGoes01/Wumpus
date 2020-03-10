class Fitness:

    def __init__(self, pontos, movimentos_bons, movimentos_ruins, movimento_sem_ouro, tamanho):
        self.__p = pontos
        self.__mb = movimentos_bons
        self.__mr = movimentos_ruins
        self.__mso = movimento_sem_ouro
        self.__n = tamanho

    def calcular_fitness(self):

        k = 20 + 6*(self.__n - 4)

        fitness = (self.__p + k*self.__mb/(1 + self.__mso))/(1 + self.__mr)

        return fitness
