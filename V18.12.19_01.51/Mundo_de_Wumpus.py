from AmbienteBruto import Ambiente
from Agente import Agente
import random
from Casa import Casa
from Populacao import Populacao
from Memoria import Memoria as mem
from Fitness import Fitness as fit


class Jogo:

    def reproduzir(self, vetor_celulas, geracao):
        novo_vetor = []

        for contador in range(0, len(vetor_celulas), 2):

            celula_mae = vetor_celulas[contador]
            celula_pai = vetor_celulas[contador + 1]
            nova_celula_a = Agente(0)
            nova_celula_b = Agente(0)

            movimento_mae = celula_mae.get_movimento()
            movimento_pai = celula_pai.get_movimento()

            mvalidos_mae = celula_mae.get_nice_moves()
            mvalidos_pai = celula_pai.get_nice_moves()

            movimento_nca = []
            movimento_ncb = []

            if len(mvalidos_mae) > 0:
                for contador2 in range(len(mvalidos_mae)):
                    movimento_nca.append(movimento_mae[contador2])

            if len(mvalidos_pai) > 0:
                for contador2 in range(len(mvalidos_pai)):
                    movimento_ncb.append(movimento_pai[contador2])

            nova_celula_a.set_tamanho(random.randint(0, int(self.__tamanho**2)))
            nova_celula_b.set_tamanho(random.randint(0, int(self.__tamanho**2)))
            nova_celula_a.set_movimento(movimento_nca[:] + nova_celula_a.gerar_movimento())
            nova_celula_b.set_movimento(movimento_ncb[:] + nova_celula_b.gerar_movimento())

            pos_mae = vetor_celulas.index(celula_mae)
            pos_pai = vetor_celulas.index(celula_pai)

            id_a = str(geracao) + '_' + str(pos_mae) + str(pos_pai) + '_' + str(len(vetor_celulas) + contador)
            id_b = str(geracao) + '_' + str(pos_mae) + str(pos_pai) + '_' + str(len(vetor_celulas) + contador + 1)

            nova_celula_a.set_id(id_a)
            nova_celula_b.set_id(id_b)

            fitness_a, pontuacao_a = nova_celula_a.pecado_inicial(nova_celula_a)
            fitness_b, pontuacao_b = nova_celula_a.pecado_inicial(nova_celula_b)

            nova_celula_a.set_fitness(fitness_a)
            nova_celula_b.set_fitness(fitness_b)

            nova_celula_a.set_pontucao(pontuacao_a)
            nova_celula_b.set_pontucao(pontuacao_b)

            novo_vetor.append(nova_celula_a)
            novo_vetor.append(nova_celula_b)

        vetor_celulas += novo_vetor[:]

        return vetor_celulas

    def __init__(self, geracoes, tamanho_ambiente):
        self.__ger = geracoes
        self.__tamanho = tamanho_ambiente

    def executar(self):

        maximos = []
        minimos = []
        medias = []
        mortes_poco = []
        mortes_wumpus = []
        sucessos = []
        ouros = []

        ambiente = Ambiente(self.__tamanho)
        amb = ambiente.gerarAmbiente()

        pop = Populacao(100, 0, self.__tamanho)
        vet_ag = pop.gerar_populacao()

        # for agente in vet_ag:
        #     indice = vet_ag.index(agente)
        #     id = '0_00_' + str(indice)
        #     agente.set_id(id)

        memoria = mem()
        memoria.ordenar_memoria(vet_ag)
        vet_mem = memoria.get_memoria()

        for geracao in range(self.__ger):

            vet_ag = self.reproduzir(vet_ag.copy(), geracao)

            num_mortes_poco = 0
            num_mortes_wumpus = 0
            num_sucesso = 0
            num_ouro = 0

            for ag in vet_ag:
                if ag.get_movimento() == []:
                    ag.set_pontucao(2)
                    fitness = fit(ag.get_pontuacao(), 0, 0, 0)
                    ag.set_fitness(fitness.calcular_fitness())
                    ag.set_tamanho(random.randint(10, 64))
                    ag.set_movimento(ag.gerar_movimento())

            for agente in vet_ag:
                pos = [0, 0]  # Define a posição inicial como [0, 0]
                pos_ant = [0, 0]  # Define a posição anterior como [0, 0]
                rodada = 0  # Começa pela rodada 0
                acao_ant = ''  # Define a ação anterior como nula
                caminho_ate_ouro = 0  # Define o caminho até o ouro como nulo
                wumpus_vivo = True

                agente.viver()  # Revive o agente
                agente.recarregar()  # Recarrega a 'aljava'

                agente.reset_nice_moves()  # Define os movimentos bons como 0
                agente.reset_caminho_percorrido()  # Define o caminho percorrido como nulo
                agente.reset_pontuacao()  # Define a pontuação como 0
                agente.reset_ouro()  # Tira o ouro do agente

                fitness, pontuacao = agente.pecado_inicial(agente)  # Aplica as pontuações iniciais
                agente.set_fitness(fitness)  # Define o fitness inicial
                agente.set_pontucao(pontuacao)  # Define a pontuação inicial
                agente.add_caminho_percorrido(list(pos))  # Adiciona [0, 0] ao caminho percorrido

                mov_sem_ouro = 0

                for acao in agente.get_movimento():

                    # Se o agente estiver com o ouro e tiver andado mais casas do que precisou para chegar até o ouro
                    if agente.get_ouro() and len(agente.get_caminho_percorrido()) > caminho_ate_ouro*2:
                        movimento_bom = False  # Qualquer movimento será considerado ruim

                    else:  # Caso contrário
                        movimento_bom = True  # O movimento a seguir tem a possibilidade de ser bom

                    if agente.get_vida():  # Executa enquanto o agente estiver vivo
                        amb[pos_ant[0]][pos_ant[1]].isAgente(False)  # Remove o agente da sua posição anterior

                        if acao == 'n':  # Anda pro norte
                            pos[0] -= 1
                        elif acao == 's':  # Anda pro sul
                            pos[0] += 1
                        elif acao == 'l':  # Anda pro leste
                            pos[1] += 1
                        elif acao == 'o':  # Anda pro oeste
                            pos[1] -= 1

                        # Se o agente andar para fora da matriz
                        if 0 > pos[0] or 3 < pos[0] or 0 > pos[1] or 3 < pos[1]:
                            agente.set_pontucao(0)  # Recebe pontução nula
                            agente.morrer()  # Morre
                            movimento_bom = False  # O movimento é ruim

                        else:  # Caso contrário
                            agente.add_caminho_percorrido(list(pos))  # A posição atual é adicionada à lista de casas
                            amb[pos[0]][pos[1]].isAgente(True)  # A casa recebe o agente

                            # Se o agente quiser disparar e possuir flecha
                            if (acao == 'fn' or acao == 'fs' or acao == 'fl' or acao == 'fo') and agente.get_flecha():
                                agente.disparar()  # Pode disparar

                                if acao == 'fn':
                                    if ambiente.getWumpus() == [pos[0] - 1, pos[1]]:
                                        wumpus_vivo = False
                                        agente.set_pontucao(256)

                                    else:
                                        movimento_bom = False
                                        agente.set_pontucao(2)

                                elif acao == 'fs':
                                    if ambiente.getWumpus() == [pos[0] + 1, pos[1]]:
                                        wumpus_vivo = False
                                        agente.set_pontucao(256)

                                    else:
                                        movimento_bom = False
                                        agente.set_pontucao(2)

                                elif acao == 'fl':
                                    if ambiente.getWumpus() == [pos[0], pos[1] + 1]:
                                        wumpus_vivo = False
                                        agente.set_pontucao(256)

                                    else:
                                        movimento_bom = False
                                        agente.set_pontucao(2)

                                elif acao == 'fo':
                                    if ambiente.getWumpus() == [pos[0], pos[1] - 1]:
                                        wumpus_vivo = False
                                        agente.set_pontucao(256)

                                    else:
                                        movimento_bom = False
                                        agente.set_pontucao(2)

                            elif(acao == 'fn' or acao == 'fs' or acao == 'fl' or acao == 'fo') and not agente.get_flecha():
                                movimento_bom = False  # Pode disparar, porém o movimento é ruim

                            if pos == ambiente.getWumpus() and wumpus_vivo:
                                num_mortes_wumpus += 1
                                agente.morrer()
                                agente.set_pontucao(1)
                                movimento_bom = False

                            for casa in ambiente.getPoco():
                                if pos == casa:  # Se a posição atual for igual à de um poço
                                    num_mortes_poco += 1
                                    agente.morrer()  # O agente morre
                                    agente.set_pontucao(2)  # Recebe 2pts
                                    movimento_bom = False  # O movimento é considerado ruim

                            if acao == 'p':  # Se a ação atual for "pegar"
                                # Se houver ouro na casa e a quantidade de pegar for == 1
                                if pos == ambiente.getOuro() and agente.get_movimento().count('p') == 1:
                                    num_ouro += 1
                                    agente.pegar_ouro()  # O agente pega o ouro
                                    # É definido o tamanho do caminho até o ouro
                                    caminho_ate_ouro = len(agente.get_caminho_percorrido())
                                else:  # Caso contrário
                                    agente.set_pontucao(1)  # O agente recebe 1pt
                                    movimento_bom = False  # O movimento é considerado ruim

                        if not agente.get_ouro():
                            mov_sem_ouro += 1

                        if movimento_bom:
                            agente.set_nice_moves(rodada)
                            agente.set_pontucao(4)

                        else:
                            agente.set_bad_moves(rodada)
                            agente.set_pontucao(2)

                        acao_ant = acao
                        pos_ant = pos.copy()
                        rodada += 1

                if agente.get_ouro() and agente.get_caminho_percorrido()[-1] == [0, 0]:
                    num_sucesso += 1
                    if len(agente.get_caminho_percorrido()) < self.__tamanho*5:
                        agente.set_pontucao(2048)

                    else:
                        agente.set_pontucao(1024)

                elif agente.get_ouro() and agente.get_caminho_percorrido()[-1] != [0, 0]:
                    agente.set_pontucao(1)

                if agente.get_flecha():
                    agente.set_pontucao(129)

                fitness = fit(agente.get_pontuacao(), len(agente.get_nice_moves()), len(agente.get_bad_moves()), mov_sem_ouro)  # FITNESS AQUI!!!
                agente.set_fitness(fitness.calcular_fitness())

            memoria_temp = mem()
            memoria_temp.ordenar_memoria(vet_ag.copy())
            vet_memoria_temp = memoria_temp.get_memoria()

            fitness_maximo = vet_memoria_temp[0].get_fitness()
            pontuacao_maxima = vet_memoria_temp[0].get_pontuacao()

            maximos.append([fitness_maximo, pontuacao_maxima])

            fitness_minimo = vet_memoria_temp[-1].get_fitness()
            pontuacao_minima = vet_memoria_temp[-1].get_pontuacao()

            minimos.append([fitness_minimo, pontuacao_minima])

            total_fitness = 0
            total_pontuacao = 0

            for celula in vet_memoria_temp:
                total_fitness += celula.get_fitness()
                total_pontuacao += celula.get_pontuacao()

            media_fitness = total_fitness/len(vet_memoria_temp)
            media_pontuacao = total_pontuacao/len(vet_memoria_temp)

            medias.append([media_fitness, media_pontuacao])

            sucessos.append(num_sucesso)
            ouros.append(num_ouro)
            mortes_poco.append(num_mortes_poco)
            mortes_wumpus.append(num_mortes_wumpus)

            for contador in range(len(vet_memoria_temp)):
                ja_existe = False

                for contador_b in range(len(vet_mem)):
                    if vet_memoria_temp[contador].get_id() == vet_mem[contador_b].get_id():
                        ja_existe = True

                if not ja_existe:
                    if vet_memoria_temp[contador].get_fitness() > vet_mem[0].get_fitness():
                        vet_mem[-1] = vet_mem[0]
                        vet_mem[0] = vet_memoria_temp[contador]
                        memoria.ordenar_memoria(vet_mem.copy())
                        vet_mem = memoria.get_memoria()

                    elif vet_memoria_temp[contador].get_fitness() > vet_mem[-1].get_fitness():
                        vet_mem[-1] = vet_memoria_temp[contador]
                        memoria.ordenar_memoria(vet_mem.copy())
                        vet_mem = memoria.get_memoria()

            vet_ag = list(vet_mem)
            num_eliminados = int(len(vet_ag)*0.6)

            for contador in range(num_eliminados):
                vet_ag.pop(-1)

            nova_pop = Populacao(num_eliminados, geracao, self.__tamanho)
            vet_nova_pop = nova_pop.gerar_populacao()

            vet_ag += list(vet_nova_pop)

            vet_mem[0].imprimir_agente()

        print(f"Poços: {ambiente.getPoco()}\nOuro: {ambiente.getOuro()}\nWumpus: {ambiente.getWumpus()}")
        vet_mem[0].imprimir_agente()
        dados = [maximos, minimos, medias, sucessos, ouros, mortes_wumpus, mortes_poco]

        return dados
