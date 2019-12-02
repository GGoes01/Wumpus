import random

y = 30  # Tamanho do cromossomo

agmov = [0 for x in range (y)] # agmov é vetor de movimentação do agente

poss = ['n', 's', 'l', 'o', 'p', 'f', 'null']  # poss vem de possibilities, vetor de possibilidades de ações

random.shuffle(poss)

for x in range (y):
	agmov[x] = random.choice(poss)

print(agmov)

