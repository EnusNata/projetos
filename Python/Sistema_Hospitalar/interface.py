import PySimpleGUI as sg
import tabelas
import registrar_informacoes as ri
import auxiliares_a_interface

janela = auxiliares_a_interface.obter_janela_da_tela_principal()

while True:
    evento , valores = janela.read()

    if evento == sg.WIN_CLOSED:
        break

    if evento == 'registrar_medico':
        ri.salvar_medico()

    if evento == 'ver_medicos':
        tabelas.ver_medico()

    if evento == 'marcar_consulta':
        ri.salvar_consulta()

    if evento == 'ver_consultas':
        tabelas.ver_consulta()