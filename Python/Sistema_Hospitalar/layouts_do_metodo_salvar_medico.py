import PySimpleGUI as sg

layout_de_registro_do_medico = \
        [
            [sg.Text('Digite o nome e o crm do médico')],
            [sg.Text('Nome', size=(5, 1)), sg.Input(key='nome')],
            [sg.Text('Crm', size=(5, 1)), sg.Input(key='crm')],
            [sg.Button('Registrar', key='registrar')]
        ]