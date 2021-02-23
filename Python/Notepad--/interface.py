import PySimpleGUI as sg
import eventos
import funcoes_auxiliares
import mensagens

informacoes_do_arquivo = dict()
informacoes_do_arquivo = eventos.novo_arquivo()

sg.ChangeLookAndFeel('BrownBlue')

layout_menu =   [
                    ['Arquivo', ['Novo','Abrir','Salvar','Salvar Como','------','Sair']]
                ]

layout_window = [
                    [sg.MenuBar(layout_menu)],
                    [sg.Text('Novo Arquivo', size=(90,1), key='caminho_arquivo')],
                    [sg.Multiline(size=(90,25),key='texto_arquivo')]
                ]

janela = sg.Window( 'Notepad--', 
                    layout=layout_window, 
                    margins=(0,0), 
                    resizable=True, 
                    return_keyboard_events=True,
                    finalize=True)

janela.maximize()
janela['texto_arquivo'].expand(expand_x=True, expand_y=True)

while True:
    evento, valores = janela.read()

    if evento in ('Sair',sg.WIN_CLOSED):
        break

    if evento == 'Novo':
        informacoes_do_arquivo = eventos.novo_arquivo()

        funcoes_auxiliares.atualizar_janela(janela, informacoes_do_arquivo)
        mensagens.mostrar_mensagem_aberto_com_sucesso()

    if evento == 'Abrir':
        informacoes_do_arquivo = eventos.abrir_arquivo(informacoes_do_arquivo)
        
        if informacoes_do_arquivo['caminho_do_arquivo'] != 'Novo Arquivo':
            funcoes_auxiliares.atualizar_janela(janela, informacoes_do_arquivo)
        else:
            mensagens.mostrar_mensagem_arquivo_nao_encontrado()

    if evento == 'Salvar':
        informacoes_do_arquivo = eventos.salvar(informacoes_do_arquivo, valores)

        if informacoes_do_arquivo['caminho_do_arquivo'] != 'Novo Arquivo':
            funcoes_auxiliares.atualizar_janela(janela, informacoes_do_arquivo)
            mensagens.mostrar_mensagem_salvo_com_sucesso()
        else:
            mensagens.mostrar_mensagem_impossivel_salvar_arquivo()

    if evento == 'Salvar Como':
        informacoes_do_arquivo = eventos.salvar_como(informacoes_do_arquivo, valores)

        if informacoes_do_arquivo['caminho_do_arquivo'] != 'Novo Arquivo':
            funcoes_auxiliares.atualizar_janela(janela, informacoes_do_arquivo)
            mensagens.mostrar_mensagem_salvo_com_sucesso()
        else:
            mensagens.mostrar_mensagem_impossivel_salvar_arquivo()