import PySimpleGUI as sg
import events

path_file_open = None

sg.ChangeLookAndFeel('BrownBlue')

layout_menu =   [
                    ['Arquivo', ['Novo','Abrir','Salvar','Salvar Como','------','Sair']]
                ]

layout_window = [
                    [sg.MenuBar(layout_menu)],
                    [sg.Text('Novo Arquivo', size=(90,1), key='caminho_arquivo')],
                    [sg.Multiline(size=(90,25),key='texto_arquivo')]
                ]

window = sg.Window('Notepad--', layout=layout_window, margins=(0,0), resizable=True, return_keyboard_events=True, finalize=True)

window.maximize()
window['texto_arquivo'].expand(expand_x=True, expand_y=True)

while True:
    event, values = window.read()

    if event in ('Sair',None):
        break
    if event == 'Novo':
        events.new_file(window)
    if event == 'Abrir':
        path_file_open = sg.popup_get_file('Abrir',no_window=True) #retorna string com o path do arquivo
        window['caminho_arquivo'].update(value=path_file_open)
        events.open_file(window,path_file_open)
    if event == 'Salvar':
        events.save_file(values,path_file_open)
    if event == 'Salvar Como':
        path_file_open = sg.popup_get_file('Salvar Como', no_window=True ,save_as=True)
        window['caminho_arquivo'].update(value=path_file_open)
        events.save_file_as(values,path_file_open)