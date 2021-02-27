import PySimpleGUI as sg

layout_tela_principal = [
                            [sg.Text('Sistema Hospitalar',font='Any 15',text_color='Red')],
                            [sg.Button('Registrar Médico', key='registrar_medico')],
                            [sg.Button('Ver Médicos Registrados', key='ver_medicos')],
                            [sg.Button('Marcar Consulta', key='marcar_consulta')],
                            [sg.Button('Ver Consultas Marcadas', key='ver_consultas')]
                        ]