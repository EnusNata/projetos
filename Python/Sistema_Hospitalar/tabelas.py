import PySimpleGUI as sg
import banco_de_dados
import auxiliares_aos_metodos_selecionar
import auxiliares_aos_metodos_ver
    
def selecionar_paciente():
    registro_selecionado = 0

    tabela_paciente = banco_de_dados.obter_pacientes_registrados()
    janela = auxiliares_aos_metodos_selecionar.obter_janela_selecionar_paciente()

    while True:
        evento, valores = janela.read()

        if evento == sg.WIN_CLOSED:
            break

        if evento == registro_selecionado:
            registro_do_paciente = auxiliares_aos_metodos_selecionar.obter_registro_selecionado(tabela_paciente['registros'], valores[0])
            dados_do_paciente = auxiliares_aos_metodos_selecionar.obter_dados_do_paciente_selecionado(registro_do_paciente)

            janela.close()

            return dados_do_paciente

def selecionar_medico():
    registro_selecionado = 0

    tabela_medico = banco_de_dados.obter_medicos_registrados()
    janela = auxiliares_aos_metodos_selecionar.obter_janela_selecionar_medico()

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break

        if evento == registro_selecionado:
            registro_do_medico = auxiliares_aos_metodos_selecionar.obter_registro_selecionado(tabela_medico['registros'], valores[0])
            dados_do_medico = auxiliares_aos_metodos_selecionar.obter_dados_do_medico_selecionado(registro_do_medico)

            janela.close()
            return dados_do_medico

def ver_medico():
    tabela_medico = banco_de_dados.obter_medicos_registrados()
    janela = auxiliares_aos_metodos_ver.obter_janela_ver_medico()

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        janela.close()

def ver_consulta():
    tabela_consulta = banco_de_dados.obter_consultas_registradas()
    janela = auxiliares_aos_metodos_ver.obter_janela_ver_consulta()

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        janela.close()