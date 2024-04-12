import pandas as pd

def encontrar_posicao_numero(string):
    for i, char in enumerate(string):
        if char.isdigit():
            return i
    return -1


def separador(lista_dados):

    nova_lista_dados =[]

    for dado in lista_dados:
        #Encontra a primeira posição de um número na string atual
        primeira_posicao_numero = encontrar_posicao_numero(dado)

        #Verifica se um número foi encontrado na string atual
        if primeira_posicao_numero != -1:
            # Separe os valores e adicione-os à nova lista
            nome = dado[:primeira_posicao_numero]
            numero = dado[primeira_posicao_numero:]
            nova_lista_dados.append((nome, numero))
        else:
            #Adicione a string original à nova lista se nenhum número for encontrado
            nova_lista_dados.append((dado,""))

    #Criando um dataframe com as informações
    schema = {
    'name': str,
    'numero': str
    }

    valores_separados = pd.DataFrame(nova_lista_dados, columns=schema.keys())
    return valores_separados




lista_dados = ['Pedro624.124.290-98', 'Maria314.153.692-94', 'Gabriela']
dados_separados = separador(lista_dados)

print(dados_separados)

    