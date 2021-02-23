import PySimpleGUI as sg
import pathlib
import funcoes_auxiliares as fa

def novo_arquivo():
    '''quando um novo arquivo é criado todos os campos são resetados.'''

    informacoes_do_arquivo = dict()
    informacoes_do_arquivo['texto_do_arquivo'] = ''
    informacoes_do_arquivo['caminho_do_arquivo'] = 'Novo Arquivo'
    return informacoes_do_arquivo

def abrir_arquivo(informacoes_do_arquivo_atual):
    '''quando um arquivo é aberto devemos: 
    1 - obter o caminho do arquivo,
    2 - abrir o arquivo
    3 - obter o texto e o caminho do arquivo.'''

    informacoes_do_arquivo = dict()

    caminho_do_arquivo = fa.obter_caminho_do_arquivo_em_abrir_arquivo()

    if fa.existir_arquivo(caminho_do_arquivo):
        arquivo = fa.obter_arquivo(caminho_do_arquivo)

        informacoes_do_arquivo['texto_do_arquivo'] = arquivo.read_text()
        informacoes_do_arquivo['caminho_do_arquivo'] = arquivo.absolute()
    else:
        informacoes_do_arquivo = informacoes_do_arquivo_atual
    
    return informacoes_do_arquivo

def salvar(informacoes_do_arquivo_atual, valores):
    '''quando um arquivo é "salvo" devemos salvar as informações no arquivo atual(se existir).'''

    informacoes_do_arquivo = dict()
    informacoes_do_arquivo['caminho_do_arquivo'] = informacoes_do_arquivo_atual['caminho_do_arquivo']
    informacoes_do_arquivo['texto_do_arquivo']   = valores['texto_arquivo']

    if informacoes_do_arquivo_atual['caminho_do_arquivo'] == 'Novo Arquivo':
        informacoes_do_arquivo = salvar_como(informacoes_do_arquivo, valores)

    if fa.existir_arquivo(informacoes_do_arquivo['caminho_do_arquivo']) \
    and informacoes_do_arquivo['caminho_do_arquivo'] != 'Novo Arquivo':
        arquivo = fa.obter_arquivo(informacoes_do_arquivo['caminho_do_arquivo'])
        informacoes_do_arquivo['caminho_do_arquivo'] = arquivo.absolute()

        fa.salvar_texto_no_arquivo(arquivo, informacoes_do_arquivo['texto_do_arquivo'])
    else:
        informacoes_do_arquivo = informacoes_do_arquivo_atual

    return informacoes_do_arquivo

def salvar_como(informacoes_do_arquivo_atual,valores):
    '''quando um arquivo é salvo como, utilizamos um popup para obter o caminho do arquivo.'''

    informacoes_do_arquivo = dict()
    informacoes_do_arquivo['caminho_do_arquivo'] = informacoes_do_arquivo_atual['caminho_do_arquivo']
    informacoes_do_arquivo['texto_do_arquivo']   = valores['texto_arquivo']

    informacoes_do_arquivo['caminho_do_arquivo'] = fa.obter_caminho_do_arquivo_em_salvar_como()

    if fa.existir_arquivo(informacoes_do_arquivo['caminho_do_arquivo']):
        informacoes_do_arquivo = salvar(informacoes_do_arquivo, valores)
    else:
        informacoes_do_arquivo = informacoes_do_arquivo_atual
    
    return informacoes_do_arquivo