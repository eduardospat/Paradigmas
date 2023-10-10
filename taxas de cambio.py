import requests

def obter_taxas_de_cambio(chave_api, moeda_base='EUR'):
    url = f'http://data.fixer.io/api/latest'
    params = {'access_key': chave_api, 'base': moeda_base}
    response = requests.get(url, params=params)

    if response.status_code != 200: #404 - nao encontrado
        print(f"Erro na solicitação: {response.status_code}")
        return None

    data = response.json()
    
    if not data.get('success', False):
        error_info = data.get('error', {})
        error_code = error_info.get('code', 'N/A')

        if error_code == 104:
            print("Limite mensal de requisições excedido")
        else:
            print("Erro na solicitação")


        return None

    return data
    """
    Obtém as taxas de câmbio da Fixer.io usando uma chave de API e uma moeda base.
    Args:
        chave_api (str): Chave de API para autenticação.
        moeda_base (str): Moeda base para a qual as taxas de câmbio são solicitadas.
    """

def criar_linha_taxa(moeda, taxa):
    return f"{moeda}:{taxa}"
    """
    Cria uma linha formatada para exibir uma taxa de câmbio de forma iterativa.
    Args:
        moeda (str): Código da moeda.
        taxa (float): Taxa de câmbio.
    """

def criar_linha_informacoes(data):
    return [
        f"$ success: {data.get('success', 'N/A')}",  # Programação funcional usando list comprehension e função get.
        f"$ base currency: {data.get('base', 'N/A')}",
        f"$ date: {data.get('date', 'N/A')}",
    ]
    """
    Cria linhas formatadas para exibir informações gerais.
    Args:
        data (dict): Dados contendo informações gerais.
    """

def criar_linha_taxas(data):
    rates = data.get('rates', {})
    return [criar_linha_taxa(moeda, taxa) for moeda, taxa in rates.items()]  # Programação funcional usando list comprehension.
    """
    Cria linhas formatadas para exibir taxas de câmbio.
    Args:
        data (dict): Dados contendo taxas de câmbio.
    """

def escrever_em_arquivo(dados, nome_arquivo='taxas.txt'):
    with open(nome_arquivo, 'w') as arquivo:
        arquivo.write('\n'.join(dados) + '\n')  # Programação declarativa usando o método join.
    """
    Escreve as linhas em um arquivo.
    Args:
        dados (list): Lista de linhas a serem escritas.
        nome_arquivo (str): Nome do arquivo.
    """

def fornecer_dados(chave_api, moeda_base='EUR'):
    dados = obter_taxas_de_cambio(chave_api, moeda_base)

    if dados:
        informacoes = criar_linha_informacoes(dados)
        taxas = criar_linha_taxas(dados)
        
        print("Escrevendo dados no arquivo...")
        escrever_em_arquivo(informacoes + taxas)
        print("Dados escritos no arquivo.")

if __name__ == "__main__":    ## se o arquivo for executado diretamente, o nome da variavel __name__ é __main__ (Boas práticas de acordo com um coléga de curso, Diogo Bohrer, não faz Paradigmas)
    chave_api = '93924142ec51183fed773d2762485ee3'
    moeda_base = 'EUR'
    fornecer_dados(chave_api, moeda_base)
