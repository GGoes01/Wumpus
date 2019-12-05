from Casa import Casa
import random


class Ambiente():

    __casasPreenchidas = []  # Vetor que armazenará as casas já ocupadas por elementos
    __casasPocos = []  # Vetor que armazenará as casas ocupadas por poços
    __casaOuro = []  # Casa do ouro
    __casaWumpus = []  # Casa do Wumpus

    # Método construtor, que pede como parâmetro a dimensão da matriz NxN
    def __init__(self, tamanho):
        self.tamanho = tamanho

    def gerarSensacoes(self, matriz):
        posOuro = self.getOuro()
        posWumpus = self.getWumpus()
        posPoco = self.getPoco()

        matriz[posOuro[0]][posOuro[1]].addSense("Brilho")

        if 0 < posWumpus[0] < self.tamanho - 1:
            matriz[posWumpus[0] + 1][posWumpus[1]].addSense("Fedor")
            matriz[posWumpus[0] - 1][posWumpus[1]].addSense("Fedor")

        elif posWumpus[0] == 0:
            matriz[posWumpus[0] + 1][posWumpus[1]].addSense("Fedor")

        elif posWumpus[0] == self.tamanho - 1:
            matriz[posWumpus[0] - 1][posWumpus[1]].addSense("Fedor")

        if 0 < posWumpus[1] < self.tamanho - 1:
            matriz[posWumpus[0]][posWumpus[1] + 1].addSense("Fedor")
            matriz[posWumpus[0]][posWumpus[1] - 1].addSense("Fedor")

        elif posWumpus[1] == 0:
            matriz[posWumpus[0]][posWumpus[1] + 1].addSense("Fedor")

        elif posWumpus[1] == self.tamanho - 1:
            matriz[posWumpus[0]][posWumpus[1] - 1].addSense("Fedor")

        for a in range(len(posPoco)):
            if 0 < posPoco[a][0] < self.tamanho - 1:
                matriz[posPoco[a][0] + 1][posPoco[a][1]].addSense("Brisa")
                matriz[posPoco[a][0] - 1][posPoco[a][1]].addSense("Brisa")

            elif posPoco[a][0] == 0:
                matriz[posPoco[a][0] + 1][posPoco[a][1]].addSense("Brisa")

            elif posPoco[a][0] == self.tamanho - 1:
                matriz[posPoco[a][0] - 1][posPoco[a][1]].addSense("Brisa")

            if 0 < posPoco[a][1] < self.tamanho - 1:
                matriz[posPoco[a][0]][posPoco[a][1] + 1].addSense("Brisa")
                matriz[posPoco[a][0]][posPoco[a][1] - 1].addSense("Brisa")

            elif posPoco[a][1] == 0:
                matriz[posPoco[a][0]][posPoco[a][1] + 1].addSense("Brisa")

            elif posPoco[a][1] == self.tamanho - 1:
                matriz[posPoco[a][0]][posPoco[a][1] - 1].addSense("Brisa")

        return matriz

    # Método que gera os elementos(poços, ouro, Wumpus) do ambiente
    def gerarElementos(self, matriz):

        qtdePocos = self.tamanho - 1

        # Cria um vetor com todas as casas possíveis disponíveis
        casas = [[posLinha, posColuna] for posLinha in range(self.tamanho) for posColuna in range(self.tamanho)]
        # Remove a casa [0, 0]
        casas.pop(0)

        # De acordo com o número de poços:
        for a in range(qtdePocos):
            poco = random.choice(casas)  # Escolhe uma das casas disponíveis
            casas.pop(casas.index(poco))  # Remove a casa escolhida
            self.preencherCasa(poco)  # Armazena a casa escolhida
            self.setPoco(poco)  # Junta à lista de casas-poço
            matriz[poco[0]][poco[1]].isPoco(True)  # Define na matriz principal que há um poço naquela casa
            # print(matriz[poco[0]][poco[1]])

        wumpus = random.choice(casas)  # Escolhe uma das casas disponíveis pra ser o wumpus
        casas.pop(casas.index(wumpus))
        self.preencherCasa(wumpus)
        self.setWumpus(wumpus)
        matriz[wumpus[0]][wumpus[1]].isWumpus(True)

        ouro = random.choice(casas)
        casas.pop(casas.index(ouro))
        self.preencherCasa(ouro)
        self.setOuro(ouro)
        matriz[ouro[0]][ouro[1]].isOuro(True)

        return matriz

    # Método que cria o ambiente
    def gerarAmbiente(self):
        # Cria uma matriz ambiente com todas as informações zeradas
        amb = [[Casa() for x in range(self.tamanho)] for y in range(self.tamanho)]
        amb = self.gerarElementos(amb)  # Adiciona os elementos(poços, ouro, Wumpus) ao ambiente
       # amb = self.gerarSensacoes(amb)  # Adiciona as sensações(fedor, brilho, brisa) ao ambiente

        return amb

    def preencherCasa(self, posicao):
        self.__casasPreenchidas.append(posicao)

    def setPoco(self, posicaoPoco):
        self.__casasPocos.append(posicaoPoco)

    def setWumpus(self, posicaoWumpus):
        self.__casaWumpus = posicaoWumpus

    def setOuro(self, posicaoOuro):
        self.__casaOuro = posicaoOuro

    def getPoco(self):
        return self.__casasPocos

    def getWumpus(self):
        return self.__casaWumpus

    def getOuro(self):
        return self.__casaOuro

    def getCasasPreenchidas(self):
        return self.__casasPreenchidas

