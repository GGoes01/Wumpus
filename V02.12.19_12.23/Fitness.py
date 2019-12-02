class Fitness:

    def __init__(self, pontos, movimentos_bons):
        self.__p = pontos
        self.__mb = movimentos_bons

    def calcular_fitness(self):
        fitness = self.__mb*5 + self.__p

        return fitness
