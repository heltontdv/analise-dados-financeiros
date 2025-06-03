import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para carregar os dados
def carregar_dados(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)

        # Limpa espaços em branco nos nomes das colunas
        df.columns = df.columns.str.strip()

        print("Dados carregados com sucesso!")
        print(df.head())
        return df
    except Exception as e:
        print("Erro ao carregar o arquivo:", e)
        return None

# Função para exibir estatísticas básicas
def estatisticas_dados(df):
    print("\nEstatísticas Descritivas:")
    print(df.describe(include='all'))

# Função para converter a coluna de data
def tratar_datas(df):
    df['Data'] = pd.to_datetime(df['Data'])
    return df

# Função para adicionar média móvel
def adicionar_media_movel(df, janela=3):
    df['MediaMovel'] = df['Valor'].rolling(window=janela).mean()
    return df

# Função para exibir gráfico
def exibir_grafico(df):
    plt.figure(figsize=(10, 6))
    sns.lineplot(data=df, x='Data', y='Valor', label='Valor')
    sns.lineplot(data=df, x='Data', y='MediaMovel', label='Média Móvel', linestyle='--')
    plt.title('Análise de Tendência Financeira')
    plt.xlabel('Data')
    plt.ylabel('Valor')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# Função principal
def main():
    caminho = 'dados_financeiros.csv'
    df = carregar_dados(caminho)

    if df is not None:
        df = tratar_datas(df)
        estatisticas_dados(df)
        df = adicionar_media_movel(df)
        exibir_grafico(df)

# Executar
if __name__ == "__main__":
    main()
