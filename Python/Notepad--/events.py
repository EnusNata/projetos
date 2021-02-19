import PySimpleGUI as sg
import pathlib

def new_file(window):
    '''quando um novo arquivo é criado todos os campos são resetados (incluindo o path_file).'''
    window['texto_arquivo'].update(value='')
    window['caminho_arquivo'].update(value='Novo Arquivo')

def open_file(window,path_file_open):
    '''quando um arquivo é aberto devemos receber o nome do arquivo, obter seu caminho e atualizar os campos com suas informações.'''
    if path_file_open:
        object_path = pathlib.Path(path_file_open)  # cria um objeto referente ao arquivo na string.
        window['texto_arquivo'].update(value=object_path.read_text())
        window['caminho_arquivo'].update(value=object_path.absolute())

def save_file(values,path_file_open):
    '''quando um arquivo é salvo salvamos o texto do arquivo em um arquivo especificado pelo caminho (objeto path).'''
    if path_file_open:
        object_path = pathlib.Path(path_file_open)  # cria um objeto referente ao arquivo na string.
        object_path.write_text(values['texto_arquivo'])
    else :
        save_file_as(values,path_file_open)

def save_file_as(values,path_file_open):
    '''quando um arquivo é "salvo como" devemos salvar as informações no arquivo especificado pelo objeto path.'''
    if path_file_open:
        object_path = pathlib.Path(path_file_open)
        object_path.write_text(values['texto_arquivo'])