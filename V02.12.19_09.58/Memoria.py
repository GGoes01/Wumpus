class Memoria:
    def __init__(self):
        self.__memoria = []

    def get_memoria(self):
        return self.__memoria

    def ordenar_memoria(self, vetor_celulas):
        vetor = list(vetor_celulas)
        for contador in range(len(vetor)):
            for contador2 in range(contador + 1, len(vetor)):
                if vetor[contador].get_fitness() < vetor[contador2].get_fitness():
                    aux = vetor[contador2]
                    vetor[contador2] = vetor[contador]
                    vetor[contador] = aux
                    contador2 = contador + 1

        self.__memoria = vetor

