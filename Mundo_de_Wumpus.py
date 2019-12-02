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

            media = (len(movimento_mae) + len(movimento_pai))/2

            nova_celula_a.set_tamanho(int(media))
            nova_celula_b.set_tamanho(int(media))

            nova_celula_a.set_movimento(movimento_nca + nova_celula_a.gerar_movimento())
            nova_celula_b.set_movimento(movimento_ncb + nova_celula_b.gerar_movimento())

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

        ambiente = Ambiente(self.__tamanho)
        amb = ambiente.gerarAmbiente()

        pop = Populacao(100, 0)
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

            for ag in vet_ag:
                if ag.get_movimento() == []:
                    ag.set_pontucao(-10)
                    fitness = fit(ag.get_pontuacao(), 0)
                    ag.set_fitness(fitness.calcular_fitness())
                    ag.set_tamanho(random.randint(10, 64))
                    ag.set_movimento(ag.gerar_movimento())

            for agente in vet_ag:
                pos = [0, 0]
                pos_ant = [0, 0]
                rodada = 0

                agente.viver()

                agente.reset_nice_moves()

                agente.reset_pontuacao()
                fitness, pontuacao = agente.pecado_inicial(agente)
                agente.set_fitness(fitness)
                agente.set_pontucao(pontuacao)

                acao_ant = ''

                for acao in agente.get_movimento():

                    movimento_bom = True

                    if agente.get_vida():
                        amb[pos_ant[0]][pos_ant[1]].isAgente(False)
                        agente.add_caminho_percorrido(list(pos))

                        if acao == 'n':
                            pos[0] -= 1
                        elif acao == 's':
                            pos[0] += 1
                        elif acao == 'l':
                            pos[1] += 1
                        elif acao == 'o':
                            pos[1] -= 1

                        if 0 > pos[0] or 3 < pos[0] or 0 > pos[1] or 3 < pos[1]:
                            agente.set_pontucao(-300)
                            agente.morrer()
                            movimento_bom = False
                        else:
                            amb[pos[0]][pos[1]].isAgente(True)

                        if acao_ant == 'fn' and acao == 'n':
                            agente.set_pontucao(5)

                        elif acao_ant == 'fn' and acao != 'n':
                            agente.set_pontucao(-20)
                            movimento_bom = False

                        elif acao_ant == 'fs' and acao == 's':
                            agente.set_pontucao(5)

                        elif acao_ant == 'fs' and acao != 's':
                            agente.set_pontucao(-20)
                            movimento_bom = False

                        elif acao_ant == 'fl' and acao == 'l':
                            agente.set_pontucao(5)

                        elif acao_ant == 'fl' and acao != 'l':
                            agente.set_pontucao(-20)
                            movimento_bom = False

                        elif acao_ant == 'fo' and acao == 'o':
                            agente.set_pontucao(5)

                        elif acao_ant == 'fo' and acao != 'o':
                            agente.set_pontucao(-20)
                            movimento_bom = False

                        if movimento_bom:
                            agente.set_nice_moves(rodada)
                            agente.set_pontucao(5)
                        else:
                            agente.set_pontucao(-10)

                        acao_ant = acao
                        pos_ant = pos.copy()
                        rodada += 1

                fitness = fit(agente.get_pontuacao(), len(agente.get_nice_moves()))  # FITNESS AQUI!!!
                agente.set_fitness(fitness.calcular_fitness())

            memoria_temp = mem()
            memoria_temp.ordenar_memoria(vet_ag.copy())
            vet_memoria_temp = memoria_temp.get_memoria()

            for contador in range(len(vet_memoria_temp)):
                ja_existe = False

                for contador_b in range(len(vet_mem)):
                    if vet_memoria_temp[contador].get_id() == vet_mem[contador_b].get_id():
                        ja_existe = True

                if not ja_existe:
                    if vet_memoria_temp[contador].get_fitness() > vet_mem[-1].get_fitness():
                        vet_mem[-1] = vet_memoria_temp[contador]
                        memoria.ordenar_memoria(vet_mem.copy())
                        vet_mem = memoria.get_memoria()

            vet_ag = list(vet_mem)
            num_eliminados = int(len(vet_ag)*0.6)

            for contador in range(num_eliminados):
                vet_ag.pop(-1)

            nova_pop = Populacao(num_eliminados, geracao)
            vet_nova_pop = nova_pop.gerar_populacao()

            vet_ag += list(vet_nova_pop)

            escolhida = vet_mem[0]
            print(f"Id: {escolhida.get_id()} - Fitness: {escolhida.get_fitness()} - Pontuação: {escolhida.get_pontuacao()} - Movimento: {escolhida.get_movimento()}")

