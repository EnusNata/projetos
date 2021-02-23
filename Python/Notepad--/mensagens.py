import PySimpleGUI as sg

def mostrar_mensagem_salvo_com_sucesso():
    sg.popup_ok('Salvo com sucesso',title='Sucesso',keep_on_top=True, modal=True)

def mostrar_mensagem_aberto_com_sucesso():
    sg.popup_ok('Aberto com sucesso',title='Sucesso',keep_on_top=True, modal=True)

def mostrar_mensagem_arquivo_nao_encontrado():
    sg.popup_ok('Arquivo não encontrado',title='Erro',keep_on_top=True, modal=True)

def mostrar_mensagem_impossivel_salvar_arquivo():
    sg.popup_ok('Impossível salvar arquivo',title='Erro',keep_on_top=True, modal=True)