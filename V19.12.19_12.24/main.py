from Mundo_de_Wumpus import Jogo
from matplotlib import pyplot as plt

num_gen = 2000
num_execucoes = 100

file_wumpus = open("dados_wumpus.txt", "w")

jogo_4x4 = Jogo(num_gen, 4)
jogo_5x5 = Jogo(num_gen, 5)
jogo_10x10 = Jogo(num_gen, 10)
jogo_100x100 = Jogo(num_gen, 100)
jogo_1000x1000 = Jogo(num_gen, 1000)

maximos = [0]*num_gen
minimos = [0]*num_gen
medias = [0]*num_gen
sucessos = [0]*num_gen
mortes_wumpus = [0]*num_gen
mortes_poco = [0]*num_gen

num_sucesso = 0
porc_sucesso = 0.0

for execucao in range(num_execucoes):
    print(execucao)
    dados_brutos, melhor_agente = jogo_4x4.executar()

    if melhor_agente.get_ouro() and melhor_agente.get_caminho_percorrido()[-1] == [0, 0]:
        num_sucesso += 1

    for contador in range(num_gen):
        maximos[contador] += dados_brutos[0][contador]/num_execucoes

    for contador in range(num_gen):
        minimos[contador] += dados_brutos[1][contador]/num_execucoes

    for contador in range(num_gen):
        medias[contador] += dados_brutos[2][contador]/num_execucoes

    for contador in range(num_gen):
        sucessos[contador] += dados_brutos[3][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[4][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[5][contador]/num_execucoes

porc_sucesso = num_sucesso/num_execucoes
print(porc_sucesso)
file_wumpus.write(str(num_gen)+" "+str(num_execucoes)+"\n4X4\n")
file_wumpus.write(str(porc_sucesso)+"\n")

plt.figure(1)
plt.plot(maximos, 'blue', linewidth=0.8)
plt.plot(minimos, 'red', linewidth=0.8)
plt.plot(medias, 'indigo', linewidth=0.8)
plt.xlabel('Fitness')
plt.ylabel('Geração')
plt.title('Valores Máximos/Médios/Mínimos')
plt.grid(True)
plt.savefig("graficos/max_med_min_4x4.png")

plt.figure(2)
plt.plot(sucessos, 'darkgreen', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Agentes Bem-Sucedidos/Geração')
plt.grid(True)
plt.savefig("graficos/sucessos_4x4.png")

plt.figure(3)
plt.plot(mortes_wumpus, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Wumpus/Geração')
plt.grid(True)
plt.savefig("graficos/morte_wumpus_4x4.png")

plt.figure(4)
plt.plot(mortes_poco, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Poços/Geração')
plt.grid(True)
plt.savefig("graficos/morte_poco_4x4.png")

# ____________________________________________________________________________________________________________________ #

maximos = [0]*num_gen
minimos = [0]*num_gen
medias = [0]*num_gen
sucessos = [0]*num_gen
mortes_wumpus = [0]*num_gen
mortes_poco = [0]*num_gen

num_sucesso = 0
porc_sucesso = 0.0

for execucao in range(num_execucoes):
    print(execucao)
    dados_brutos, melhor_agente = jogo_5x5.executar()

    if melhor_agente.get_ouro() and melhor_agente.get_caminho_percorrido()[-1] == [0, 0]:
        num_sucesso += 1

    for contador in range(num_gen):
        maximos[contador] += dados_brutos[0][contador]/num_execucoes

    for contador in range(num_gen):
        minimos[contador] += dados_brutos[1][contador]/num_execucoes

    for contador in range(num_gen):
        medias[contador] += dados_brutos[2][contador]/num_execucoes

    for contador in range(num_gen):
        sucessos[contador] += dados_brutos[3][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[4][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[5][contador]/num_execucoes

porc_sucesso = num_sucesso/num_execucoes
print(porc_sucesso)
file_wumpus.write("5X5\n")
file_wumpus.write(str(porc_sucesso)+"\n")

plt.figure(5)
plt.plot(maximos, 'blue', linewidth=0.8)
plt.plot(minimos, 'red', linewidth=0.8)
plt.plot(medias, 'indigo', linewidth=0.8)
plt.xlabel('Fitness')
plt.ylabel('Geração')
plt.title('Valores Máximos/Médios/Mínimos')
plt.grid(True)
plt.savefig("graficos/max_med_min_5x5.png")

plt.figure(6)
plt.plot(sucessos, 'darkgreen', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Agentes Bem-Sucedidos/Geração')
plt.grid(True)
plt.savefig("graficos/sucessos_5x5.png")

plt.figure(7)
plt.plot(mortes_wumpus, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Wumpus/Geração')
plt.grid(True)
plt.savefig("graficos/morte_wumpus_5x5.png")

plt.figure(8)
plt.plot(mortes_poco, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Poços/Geração')
plt.grid(True)
plt.savefig("graficos/morte_poco_5x5.png")

# ____________________________________________________________________________________________________________________ #

maximos = [0]*num_gen
minimos = [0]*num_gen
medias = [0]*num_gen
sucessos = [0]*num_gen
mortes_wumpus = [0]*num_gen
mortes_poco = [0]*num_gen

num_sucesso = 0
porc_sucesso = 0.0

for execucao in range(num_execucoes):
    print(execucao)
    dados_brutos, melhor_agente = jogo_10x10.executar()

    if melhor_agente.get_ouro() and melhor_agente.get_caminho_percorrido()[-1] == [0, 0]:
        num_sucesso += 1

    for contador in range(num_gen):
        maximos[contador] += dados_brutos[0][contador]/num_execucoes

    for contador in range(num_gen):
        minimos[contador] += dados_brutos[1][contador]/num_execucoes

    for contador in range(num_gen):
        medias[contador] += dados_brutos[2][contador]/num_execucoes

    for contador in range(num_gen):
        sucessos[contador] += dados_brutos[3][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[4][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[5][contador]/num_execucoes

porc_sucesso = num_sucesso/num_execucoes
print(porc_sucesso)
file_wumpus.write("10X10\n")
file_wumpus.write(str(porc_sucesso)+"\n")

plt.figure(9)
plt.plot(maximos, 'blue', linewidth=0.8)
plt.plot(minimos, 'red', linewidth=0.8)
plt.plot(medias, 'indigo', linewidth=0.8)
plt.xlabel('Fitness')
plt.ylabel('Geração')
plt.title('Valores Máximos/Médios/Mínimos')
plt.grid(True)
plt.savefig("graficos/max_med_min_10X10.png")

plt.figure(10)
plt.plot(sucessos, 'darkgreen', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Agentes Bem-Sucedidos/Geração')
plt.grid(True)
plt.savefig("graficos/sucessos_10X10.png")

plt.figure(11)
plt.plot(mortes_wumpus, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Wumpus/Geração')
plt.grid(True)
plt.savefig("graficos/morte_wumpus_10X10.png")

plt.figure(12)
plt.plot(mortes_poco, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Poços/Geração')
plt.grid(True)
plt.savefig("graficos/morte_poco_10X10.png")

# ____________________________________________________________________________________________________________________ #

maximos = [0]*num_gen
minimos = [0]*num_gen
medias = [0]*num_gen
sucessos = [0]*num_gen
mortes_wumpus = [0]*num_gen
mortes_poco = [0]*num_gen

num_sucesso = 0
porc_sucesso = 0.0

for execucao in range(num_execucoes):
    print(execucao)
    dados_brutos, melhor_agente = jogo_100x100.executar()

    if melhor_agente.get_ouro() and melhor_agente.get_caminho_percorrido()[-1] == [0, 0]:
        num_sucesso += 1

    for contador in range(num_gen):
        maximos[contador] += dados_brutos[0][contador]/num_execucoes

    for contador in range(num_gen):
        minimos[contador] += dados_brutos[1][contador]/num_execucoes

    for contador in range(num_gen):
        medias[contador] += dados_brutos[2][contador]/num_execucoes

    for contador in range(num_gen):
        sucessos[contador] += dados_brutos[3][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[4][contador]/num_execucoes

    for contador in range(num_gen):
        mortes_wumpus[contador] += dados_brutos[5][contador]/num_execucoes

porc_sucesso = num_sucesso/num_execucoes
print(porc_sucesso)
file_wumpus.write("100X100\n")
file_wumpus.write(str(porc_sucesso)+"\n")

plt.figure(13)
plt.plot(maximos, 'blue', linewidth=0.8)
plt.plot(minimos, 'red', linewidth=0.8)
plt.plot(medias, 'indigo', linewidth=0.8)
plt.xlabel('Fitness')
plt.ylabel('Geração')
plt.title('Valores Máximos/Médios/Mínimos')
plt.grid(True)
plt.savefig("graficos/max_med_min_100X100.png")

plt.figure(14)
plt.plot(sucessos, 'darkgreen', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Agentes Bem-Sucedidos/Geração')
plt.grid(True)
plt.savefig("graficos/sucessos_100X100.png")

plt.figure(15)
plt.plot(mortes_wumpus, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Wumpus/Geração')
plt.grid(True)
plt.savefig("graficos/morte_wumpus_100X100.png")

plt.figure(16)
plt.plot(mortes_poco, 'black', linewidth=0.8)
plt.xlabel('Quantidade')
plt.ylabel('Geração')
plt.title('Mortes para Poços/Geração')
plt.grid(True)
plt.savefig("graficos/morte_poco_100X100.png")


'''
0 - maximos
1 - minimos
2 - medias
3 - sucessos
4 - mortes_wumpus
5 - mortes_poco
'''
file_wumpus.close()
