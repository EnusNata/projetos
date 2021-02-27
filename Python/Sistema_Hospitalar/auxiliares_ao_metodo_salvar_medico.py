import PySimpleGUI as sg
import banco_de_dados
import auxiliares_a_ambos_os_metodos_salvar
import layouts_do_metodo_salvar_medico


def obter_janela_de_registro_do_medico():
    return sg.Window(   'Registrar medico',
                        layouts_do_metodo_salvar_medico.layout_de_registro_do_medico
                    )

def obter_dados_de_registro_do_medico(valores):
    dados_do_medico = dict()
    dados_do_medico['nome'] = valores['nome']
    dados_do_medico['crm'] = valores['crm']
    return dados_do_medico

def registrar(valores):
    dados_do_medico = dict()
    dados_do_medico = obter_dados_de_registro_do_medico(valores)
    banco_de_dados.registrar_medico_no_banco_de_dados(dados_do_medico)
    auxiliares_a_ambos_os_metodos_salvar.mostrar_mensagem_de_registrado_com_sucesso()