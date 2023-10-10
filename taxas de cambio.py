import requests

def obter_taxas_de_cambio(chave_api, moeda_base='EUR'):
    """
    Obtém as taxas de câmbio da Fixer.io usando uma chave de API e uma moeda base.

    Args:
        chave_api (str): Chave de API para autenticação.
        moeda_base (str): Moeda base para a qual as taxas de câmbio são solicitadas.

    Returns:
        Dados JSON contendo as taxas de câmbio.
    """
    url = f'http://data.fixer.io/api/latest'
    params = {'access_key': chave_api, 'base': moeda_base}
    response = requests.get(url, params=params)

    return response.json() if response.status_code == 200 else None  #404 - nao encontrado

def criar_linha_taxa(moeda, taxa):
    """
    Cria uma linha formatada para exibir uma taxa de câmbio de forma iterativa.

    Args:
        moeda (str): Código da moeda.
        taxa (float): Taxa de câmbio.
    """
    return f"{moeda}: {taxa}"

def criar_linha_informacoes(data):
    """
    Cria linhas formatadas para exibir informações gerais.

    Args:
        data (dict): Dados contendo informações gerais.
    """
    return [
        f"$ success: {data.get('success', 'N/A')}",  # Programação funcional usando list comprehension e função get.
        f"$ base: {data.get('base', 'N/A')}",
        f"$ date: {data.get('date', 'N/A')}",
    ]

def criar_linha_taxas(data):
    """
    Cria linhas formatadas para exibir taxas de câmbio.

    Args:
        data (dict): Dados contendo taxas de câmbio.

    Returns:
        list: Lista de linhas formatadas.
    """
    rates = data.get('rates', {})
    return [criar_linha_taxa(moeda, taxa) for moeda, taxa in rates.items()]  # Programação funcional usando list comprehension.

def escrever_em_arquivo(dados, nome_arquivo='output.txt'):
    """
    Escreve as linhas em um arquivo.

    Args:
        dados (list): Lista de linhas a serem escritas.
        nome_arquivo (str): Nome do arquivo.

    Returns:
        None
    """
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('\n'.join(dados) + '\n')  # Programação declarativa usando o método join.

def fornecer_dados(chave_api, moeda_base='EUR'):
    """
    Função principal para fornecer dados de câmbio, formatar e escrever em um arquivo.

    Args:
        chave_api (str): Chave de API para autenticação.
        moeda_base (str): Moeda base para a qual as taxas de câmbio são solicitadas.

    Returns:
        None
    """
    dados = obter_taxas_de_cambio(chave_api, moeda_base)

    if dados:
        informacoes = criar_linha_informacoes(dados)
        taxas = criar_linha_taxas(dados)
        
        print("Escrevendo dados no arquivo...")
        escrever_em_arquivo(informacoes + taxas)
        print("Dados escritos no arquivo.")

if __name__ == "__main__":
    chave_api = '93924142ec51183fed773d2762485ee3'
    moeda_base = 'EUR'
    fornecer_dados(chave_api, moeda_base)
