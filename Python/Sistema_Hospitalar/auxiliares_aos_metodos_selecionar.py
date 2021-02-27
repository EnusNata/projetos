import PySimpleGUI as sg
import layouts_dos_metodos_selecionar

def obter_janela_selecionar_paciente():
    return sg.Window(   'Pacientes registrados', 
                        layouts_dos_metodos_selecionar.layout_selecionar_paciente, 
                        keep_on_top=True
                    )

def obter_janela_selecionar_medico():
    return sg.Window(   'Medicos registrados',
                        layouts_dos_metodos_selecionar.layout_selecionar_medico, 
                        keep_on_top=True
                    )

def obter_registro_selecionado(registros, registro_selecionado):
    indice_selecionado = int()
    registro = list()

    for indice in registro_selecionado:
        indice_selecionado = indice

    registro = registros[indice_selecionado]

    return registro

def obter_dados_do_paciente_selecionado(registro_do_paciente):
    dados_do_paciente = dict()
    dados_do_paciente['codigo'] = registro_do_paciente[0]
    dados_do_paciente['nome'] = registro_do_paciente[1]
    return dados_do_paciente

def obter_dados_do_medico_selecionado(registro_do_medico):
    dados_do_medico = dict()
    dados_do_medico['crm']  = registro_do_medico[0]
    dados_do_medico['nome'] = registro_do_medico[1]
    return dados_do_medico

