import PySimpleGUI as sg
import banco_de_dados

tabela_paciente = banco_de_dados.obter_pacientes_registrados()
tabela_medico = banco_de_dados.obter_medicos_registrados()

layout_selecionar_paciente =    [
                                    [   sg.Table(   values=tabela_paciente['registros'], 
                                                    headings=tabela_paciente['colunas'], 
                                                    enable_events=True, 
                                                    justification='center' 
                                                )
                                    ]
                                ]

layout_selecionar_medico =  [
                                [   sg.Table(   values=tabela_medico['registros'], 
                                                headings=tabela_medico['colunas'], 
                                                enable_events=True, 
                                                justification='center'
                                            )
                                ]
                ]