import PySimpleGUI as sg
import banco_de_dados

tabela_medico = banco_de_dados.obter_medicos_registrados()
tabela_consulta = banco_de_dados.obter_consultas_registradas()

layout_ver_medico   =   [
                            [   sg.Table(   values=tabela_medico['registros'], 
                                            headings=tabela_medico['colunas'], 
                                            enable_events=True,
                                            justification='center'
                                        )
                            ]
                ]

layout_ver_consulta =   [
                            [   sg.Table(   values=tabela_consulta['registros'], 
                                            headings=tabela_consulta['colunas'], 
                                            justification='center'
                                        )
                            ]
                        ]
