import PySimpleGUI as sg
import layout_da_interface

def obter_janela_da_tela_principal():
    return sg.Window(   title='Tela Principal',
                        layout=layout_da_interface.layout_tela_principal,
                        text_justification='center',
                        element_justification='center',
                        size=(600,600),
                        margins=(0,200)
                    )