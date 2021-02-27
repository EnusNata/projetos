import PySimpleGUI as sg
import layouts_dos_metodos_ver

def obter_janela_ver_medico():
    return sg.Window(   'Medicos registrados', 
                        layouts_dos_metodos_ver.layout_ver_medico,
                        keep_on_top=True
                    )

def obter_janela_ver_consulta():
    return sg.Window(   'Consultas marcadas', 
                        layouts_dos_metodos_ver.layout_ver_consulta,
                        keep_on_top=True
                    )