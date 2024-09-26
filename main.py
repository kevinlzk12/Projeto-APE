import pandas as pd

# Ler arquivo CSV

csv = pd.read_csv('Eleitorado\consulta_cand_2024_PB.csv', encoding='latin1', delimiter=';' )

def menu():
    print('Menu de opções:')
    print('1 - Listar candidatos por município e cargo')
    print('2 - Exibi informações de um candidato')
    print('3 - Gerar página HTML com estatísticas')
    print('4 - Sair')
    return input('Escolha uma opção: ')

while True:
    opcao = menu()
    match opcao: 
        case 1:
            