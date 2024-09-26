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

#Código do município = SG_UE
#Código do cargo = CD_CARGO
#Nome do candidato = NM_CANDIDATO
#Nome do candidato na urna = NM_URNA_CANDIDATO
#Número do candidato = NR_CANDIDATO
#Número do partido = NR_PARTIDO

while True:
    opcao = menu(opcao_1)
    if opcao == "opcao_1":
        def listar_candidatos(csv):
            codigo_municipio = input('Digite o código do município: ')
            codigo_cargo = input('Digite o código do cargo: ') 
            try:
                codigo_municipio = int(codigo_municipio)
                codigo_cargo = int(codigo_cargo)
            except ValueError:
                    print('Código inválido. Insira valores númericos.')

            candidatos_filtrados = csv[(csv['SG_UE'] == codigo_municipio) & (csv["CD_CARGO"] == codigo_cargo)]
            if candidatos_filtrados.empty:
                print('Nenhum candidato encontrado para o município e cargo fornecidos.')
            else:
                print('Candidatos encontrados: ')
                for index, candidato in candidatos_filtrados.iterrows():
                    print(f'Nome: {candidato["NM_CANDIDATO"]}')
                    print(f'Nome na Urna: {candidato["NM_URNA_CANDIDATO"]}')
                    print(f'Número: {candidato["NR_CANDIDATO"]}')
                    print(f'Partido: {candidato["NR_PARTIDO"]}')
                    print('-'* 30)