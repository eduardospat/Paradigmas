# Taxas de Câmbio
Este projeto consiste em um conversor de moedas que utiliza a API Fixer.io para obter as taxas de câmbio mais recentes.
## Funcionalidades
**Obtenção de Taxas de Câmbio:**  Utiliza a API Fixer.io para obter as taxas de câmbio mais recentes.

**Formatação e Saída:**   Cria linhas formatadas para exibir informações gerais e taxas de câmbio, e escreve esses dados em um arquivo.

## Como Executar
**Instale as Dependências:**
   Certifique-se de ter o Python instalado em seu sistema. Você pode instalar as dependências necessárias executando:
   ```bash
   pip install requests
  ```
**Execute o Programa:**
Execute o programa navegando para o diretório de seu arquivo, ou informando o caminho juntamente do comando "python":
```bash
cd caminho/do/diretorio/do/arquivo
python taxas_de_cambio.py
```
ou
```bash
python caminho/do/diretorio/do/arquivo/taxas_de_cambio.py
```
Observação: Incluir chaves de API diretamente no código não é uma prática segura para ambientes de produção ou ao compartilhar código publicamente. Esta abordagem é usada apenas para fins de aprendizado ou execução pessoal.

## Processo de Desenvolvimento
**Escolhas de Implementação:**

Utilizei a biblioteca requests para fazer solicitações HTTP pela simplicidade.
Utilizei f-strings para formatação de strings, tornando o código mais legível.
Adotei a abordagem funcional sempre que possível, usando list comprehensions.
Optei por criar funções pequenas e modulares para facilitar a manutenção e a compreensão do código. 
Adotei um estilo de programação funcional sempre que possível, visando clareza.

**Erros e Correções:**

Encontrei um problema ao tentar acessar as taxas de câmbio da resposta da API. Fiz a correção usando data.get('rates', {}).  
Demorei um bom tempo até encontrar o Fixer.io, até então nenhum outro site tinha uma documentação clara e objetiva, além de fornecer uma chave de API gratuita.  
Levei também um certo tempo até entender um pouco a biblioteca "requests", até então não estava conseguindo fazer a chamada da API, mais um certo tempo até suceder em obter os dados para o câmbio.

## Screencast
[VÍDEO](https://drive.google.com/file/d/1lNAtoEXTleCR_Jj1MAMJkLeK4ut-QEVH/view?usp=sharing)

## Referências
[Documentação da API Fixer.io](https://fixer.io/documentation)  
[Documentação da Biblioteca Requests](https://docs.python-requests.org/en/latest/)  
[Guia Markdown](https://www.markdownguide.org/getting-started/)  
[Guia da Biblioteca Python Requests](https://realpython.com/python-requests/)  
[Abrir Arquivos em Python](https://www.freecodecamp.org/portuguese/news/como-escrever-em-um-arquivo-em-python-open-read-append-e-outras-funcoes-de-manipulacao-explicadas/)

