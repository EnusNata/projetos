import PySimpleGUI as sg
import tabelas
import banco_de_dados
import layouts_do_metodo_salvar_medico
import layouts_do_metodo_salvar_consulta
import auxiliares_ao_metodo_salvar_medico
import auxiliares_ao_metodo_salvar_consulta

def salvar_medico():
    janela = auxiliares_ao_metodo_salvar_medico.obter_janela_de_registro_do_medico()

    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        if evento == 'registrar':
            auxiliares_ao_metodo_salvar_medico.registrar(valores)
            janela.close()

def salvar_consulta():
    janela = auxiliares_ao_metodo_salvar_consulta.obter_janela_de_registro_da_consulta\
        (layouts_do_metodo_salvar_consulta.layout_da_janela_marcar_consulta)
    while True:
        evento, valores = janela.read()
        if evento == sg.WIN_CLOSED:
            break
        if evento == 'selecionar_paciente':
            auxiliares_ao_metodo_salvar_consulta.selecionar_paciente(janela)
        if evento == 'selecionar_medico':
            auxiliares_ao_metodo_salvar_consulta.selecionar_medico(janela)
        if evento == 'marcar':
            auxiliares_ao_metodo_salvar_consulta.marcar(valores)
            janela.close()