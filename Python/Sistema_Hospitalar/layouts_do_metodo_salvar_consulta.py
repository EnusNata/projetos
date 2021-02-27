import PySimpleGUI as sg
import auxiliares_ao_metodo_salvar_consulta

horarios_para_consulta = auxiliares_ao_metodo_salvar_consulta.obter_lista_de_horarios_para_consulta()


layout_do_paciente =    [
                            [   sg.Text('Nome', size=(7, 1)),
                                sg.Input(key='nome_paciente'),
                                sg.Button('Selecionar', key='selecionar_paciente')
                            ] ,
                            [   sg.Text('Codigo', size=(7, 1)),
                                sg.Input(key='codigo')
                            ]
                        ]

layout_do_medico =      [
                            [   sg.Text('Nome', size=(7, 1)),
                                sg.Input(key='nome_medico') ,
                                sg.Button('Selecionar', key='selecionar_medico')
                            ] ,
                            [   sg.Text('Crm', size=(7, 1)),
                                sg.Input(key='crm')
                            ]
                        ]

layout_da_consulta =    [
                            [   sg.Text('Horario', size=(7, 1)),
                                sg.DropDown(    values=horarios_para_consulta,
                                                default_value=horarios_para_consulta[0],
                                                key='horario'
                                            )
                            ],
                            [   sg.Text('Data', size=(7, 1)),
                                sg.Input(key='data'),
                                sg.CalendarButton(  'Calendario',
                                                    target='data',
                                                    format='%Y-%m-%d'
                                                 )
                                ]
                            ]

layout_da_janela_marcar_consulta =  [
                                        [sg.Frame('Paciente', layout=layout_do_paciente)],
                                        [sg.Frame('Medico', layout=layout_do_medico)],
                                        [sg.Frame('Consulta', layout_da_consulta)],
                                        [sg.Button('Marcar', key='marcar')]
                                    ]