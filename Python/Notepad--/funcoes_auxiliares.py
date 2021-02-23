import PySimpleGUI as sg
import pathlib

def atualizar_janela_com_texto_do_arquivo(janela, texto):
    janela['texto_arquivo'].update(value = texto)

def atualizar_janela_com_caminho_do_arquivo(janela, caminho_do_arquivo):
    janela['caminho_arquivo'].update(value = caminho_do_arquivo)

def atualizar_janela(janela, informacoes_do_arquivo):
    atualizar_janela_com_caminho_do_arquivo(janela, informacoes_do_arquivo['caminho_do_arquivo'])
    atualizar_janela_com_texto_do_arquivo(janela, informacoes_do_arquivo['texto_do_arquivo'])

def salvar_texto_no_arquivo(arquivo, texto):
    arquivo.write_text(texto)

def obter_arquivo(caminho_do_arquivo):
    return pathlib.Path(caminho_do_arquivo)

def obter_caminho_do_arquivo_em_abrir_arquivo():
    return sg.popup_get_file('Abrir', no_window=True)

def obter_caminho_do_arquivo_em_salvar_como():
    return sg.popup_get_file('Salvar Como', no_window=True, save_as=True)

def existir_arquivo(caminho_do_arquivo):
    arquivo_existe = bool()

    try:
        arquivo = pathlib.Path(caminho_do_arquivo)
        arquivo_existe = True
    except:
        arquivo_existe = False

    return arquivo_existe