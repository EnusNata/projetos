from funcoes_auxiliares import *

def resumir_livro(informacoes_necessarias):

    '''Recebe um dicionário com: 
    nome do arquivo de entrada, 
    nome do arquivo de saída, 
    nome do livro que desejo resumir,
    e salva todos os textos contidos 
    no arquivo de entrada com o nome
    do livro desejado no arquivo de saída'''

    nome_arquivo_entrada = informacoes_necessarias['nome_arquivo_entrada']
    nome_arquivo_saida = informacoes_necessarias['nome_arquivo_saida']
    nome_livro_desejado = informacoes_necessarias['nome_livro_desejado']

    metadados_livro_atual = dict()

    arquivo_entrada = open(file=nome_arquivo_entrada,mode='r',encoding='utf-8')
    texto_arquivo_entrada = list()
    texto_arquivo_entrada = arquivo_entrada.readlines()
    arquivo_entrada.close()

    texto_livro_atual = list()
    texto_selecionado = str()
    resumo = list()

    while len(texto_arquivo_entrada) != 0:

        contador = 0
        while contador < 5:
            texto_livro_atual.append(texto_arquivo_entrada.pop(0))
            contador = contador + 1

        metadados_livro_atual = obter_metadados_livro_atual(texto_livro_atual)

        texto_selecionado = obter_texto_selecionado(nome_livro_desejado,metadados_livro_atual)
        resumo = adicionar_texto_ao_resumo(texto_selecionado,resumo)

        while len(texto_livro_atual) != 0:
            texto_livro_atual.pop(0)

    arquivo_saida = open(file=nome_arquivo_saida, mode="w", encoding="utf-8")
    while len(resumo) != 0:
        arquivo_saida.write(resumo.pop(0))
    arquivo_saida.close()