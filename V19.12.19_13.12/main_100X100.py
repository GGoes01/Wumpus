from Mundo_de_Wumpus import Jogo
from matplotlib import pyplot as plt

num_gen = 2000
num_execucoes = 25

file_wumpus = open("dados_wumpus.txt", "w")
jogo_100x100 = Jogo(num_gen, 100)

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

plt.figure(1)
plt.plot(maximos, 'blue', linewidth=0.8)
plt.plot(minimos, 'red', linewidth=0.8)
plt.plot(medias, 'indigo', linewidth=0.8)
plt.title('Valores Máximos/Médios/Mínimos')
plt.grid(True)
plt.savefig("graficos/max_med_min_100X100.png")

plt.figure(2)
plt.plot(sucessos, 'darkgreen', linewidth=0.8)
plt.title('Agentes Bem-Sucedidos/Geração')
plt.grid(True)
plt.savefig("graficos/sucessos_100X100.png")

plt.figure(3)
plt.plot(mortes_wumpus, 'black', linewidth=0.8)
plt.title('Mortes para Wumpus/Geração')
plt.grid(True)
plt.savefig("graficos/morte_wumpus_100X100.png")

plt.figure(4)
plt.plot(mortes_poco, 'black', linewidth=0.8)
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
