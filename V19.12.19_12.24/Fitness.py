class Fitness:

    def __init__(self, pontos, movimentos_bons, movimentos_ruins, movimento_sem_ouro):
        self.__p = pontos
        self.__mb = movimentos_bons
        self.__mr = movimentos_ruins
        self.__mso = movimento_sem_ouro

    def calcular_fitness(self):
        fitness = (self.__p + 30*self.__mb/(1 + self.__mso))/(1 + self.__mr)

        return fitness
