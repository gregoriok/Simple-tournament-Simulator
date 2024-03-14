import os
import msvcrt
import random

times = []
partidas = []
resultados = {}
def exibir_opcoes():
    print('1. Cadastrar time')
    print('2. Listar times')
    print('3. Sortear partidas')
    print('4. Exibir partidas')
    print('5. Simular jogos')
    print('6. Sair')

def exibir_times():
    os.system('cls')
    print('Times cadastrados: \n',times)
    print('\nDigite qualquer tecla para retornar ao menu')
    msvcrt.getch()
    
def cadastrar_time():
    os.system('cls')
    time = (input('\nDigite o nome do time que deseja inserir: '))
    times.append(time)

def fechar_aplicacao():
    print('\nEncerrando aplicação')
    exit()

def simular_partida(partida):
    # Simula a partida e retorna o vencedor
    print(f"Partida: {partida[0]} vs {partida[1]}")
    vencedor = input("Insira o nome do vencedor: ")
    return vencedor


def exibir_partidas():
    print("Chaveamento das partidas:")
    for i, partida in enumerate(partidas, start=1):
        print(f"Partida {i}: {partida[0]} vs {partida[1]}")
    print("\nResultados das partidas:")
    for partida, vencedor in resultados.items():
        print(f"{partida[0]} vs {partida[1]}: Vencedor - {vencedor}")
    print('\nDigite qualquer tecla para retornar ao menu')
    msvcrt.getch()


def simular_jogos():
    global partidas, resultados
    resultados_local = {}
    for partida in partidas:
            resultados_local[partida] = simular_partida(partida)
    partidas = atualizar_chaveamento(partidas, resultados_local)


def atualizar_chaveamento(partidas, resultados_local):
    novo_chaveamento = []
    ultimo_time = None
    for partida in partidas:
        if partida in resultados_local:  
            vencedor = resultados_local[partida]
            if ultimo_time is not None:
                 novo_chaveamento[-1] = (novo_chaveamento[-1][0], vencedor)
                 ultimo_time = None
            else:
                novo_chaveamento.append((vencedor, None))
                ultimo_time = vencedor

            resultados.update(resultados_local)
            del resultados_local[partida]
        else:
            if ultimo_time is not None:
                novo_chaveamento[-1] = (novo_chaveamento[-1][0], ultimo_time)
            novo_chaveamento.append(partida)
    return novo_chaveamento

def sortear_partidas():
    random.shuffle(times)

    num_partidas = len(times) // 2
    
    for i in range(num_partidas):
        time1 = times[i]
        time2 = times[i + num_partidas]
        partida = (time1, time2)
        partidas.append(partida)

def escolher_opcao():
    try:
        opcao_selecionada = int(input('\nSelecione a opção desejada: '))
        match opcao_selecionada:
            case 1:
                cadastrar_time()
            case 2:
                exibir_times()
            case 3:
                sortear_partidas()
            case 4:
                exibir_partidas()
            case 5:
                simular_jogos()
            case 6:
                fechar_aplicacao()
            case _:
                print("Opção inválida")
    except ValueError:
        print('opção invalida')

def main():
    while True:
        os.system('cls')
        exibir_opcoes()
        escolher_opcao()


if __name__ == '__main__':
    main()