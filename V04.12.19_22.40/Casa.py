class Casa:

    def __init__(self):

        self.__agente = False
        self.__poco = False
        self.__ouro = False
        self.__wumpus = False
        self.__sense = []

    def isAgente(self, state):
        self.__agente = state

    def isPoco(self, state):
        self.__poco = state

    def isOuro(self, state):
        self.__ouro = state

    def isWumpus(self, state):
        self.__wumpus = state

    def addSense(self, sensacao):
        self.__sense.append(sensacao)

    def getAgente(self):
        return self.__agente

    def getPoco(self):
        return self.__poco

    def getOuro(self):
        return self.__ouro

    def getWumpus(self):
        return self.__wumpus

    def getSense(self):
        return self.__sense

    def printGeral(self):
        print(self.getAgente(),self.getOuro(), self.getWumpus(),  self.getPoco(), self.getSense())
