import pandas as pd

# 1. Carregar a base de dados
def carregar_dados(caminho):
    return pd.read_csv(caminho, encoding='latin1', delimiter=';')

# 2. Função para listar candidatos por município e cargo
def listar_candidatos_por_municipio(df, codigo_municipio, codigo_cargo):
    try:
        codigo_municipio = int(codigo_municipio)
        codigo_cargo = int(codigo_cargo)
    except ValueError:
        print('Código inválido. Insira valores numéricos.')
        return None

    candidatos = df[(df['SG_UE'] == codigo_municipio) & (df['CD_CARGO'] == codigo_cargo)]
    if candidatos.empty:
        print('Nenhum candidato encontrado para o município e cargo fornecidos.')
    else:
        return candidatos[['NM_CANDIDATO', 'NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'NR_PARTIDO']]

# 3. Função para exibir informações de um candidato específico
def exibir_informacoes_candidato(df, codigo_candidato):
    try:
        codigo_candidato = int(codigo_candidato)
    except ValueError:
        print('Código inválido. Insira um valor numérico.')
        return None

    candidato = df[df['SQ_CANDIDATO'] == codigo_candidato]
    if candidato.empty:
        print('Candidato não encontrado.')
    else:
        return candidato[['NM_CANDIDATO', 'NM_URNA_CANDIDATO', 'NR_CANDIDATO', 'NR_PARTIDO']]

# 4. Menu interativo
def menu(df):
    while True:
        print("\nMenu:")
        print("1. Listar candidatos por município e cargo")
        print("2. Exibir informações de um candidato")
        print("3. Gerar página HTML com estatísticas")
        print("4. Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            codigo_municipio = input("Digite o código do município: ")
            codigo_cargo = input("Digite o código do cargo (por exemplo, 11 para prefeito, 12 para vice-prefeito e 13 para vereador): ")
            candidatos = listar_candidatos_por_municipio(df, codigo_municipio, codigo_cargo)
            if candidatos is not None:
                print(candidatos.to_string(index=False))
        
        elif escolha == '2':
            codigo_candidato = input("Digite o código do candidato (SQ_CANDIDATO): ")
            informacoes = exibir_informacoes_candidato(df, codigo_candidato)
            if informacoes is not None:
                print(informacoes.to_string(index=False))
        elif escolha == '3':
            print('Escolha ainda não programada kkkkkk')
        elif escolha == '4':
            print("Saindo...")
            break
        
        else:
            print("Opção inválida! Tente novamente.")

# 5. Execução do programa
if __name__ == "__main__":
    caminho = 'Eleitorado/consulta_cand_2024_PB.csv'  # Substitua pelo caminho do seu arquivo
    df = carregar_dados(caminho)
    menu(df)
