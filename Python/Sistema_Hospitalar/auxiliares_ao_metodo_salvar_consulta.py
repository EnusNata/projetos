import PySimpleGUI as sg
import banco_de_dados
import tabelas
import auxiliares_a_ambos_os_metodos_salvar

def obter_lista_de_horarios_para_consulta():
    horas = ['08', '09', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']
    minutos = ['00', '15', '30', '45']
    horarios_para_consulta = []
    for hora in horas:
        for minuto in minutos:
            horarios_para_consulta.append( hora + ':' + minuto + ':' + '00')
    return horarios_para_consulta

def obter_janela_de_registro_da_consulta(l_marcar_consulta):
    return sg.Window('Marcar consulta', l_marcar_consulta)

def houve_um_registro_selecionado(registro_selecionado):
    if registro_selecionado == sg.WIN_CLOSED:
        return False
    else:
        return True

def obter_dados_do_paciente_selecionado(paciente_selecionado):
    dados_do_paciente = dict()
    dados_do_paciente['codigo'] = paciente_selecionado['codigo']
    dados_do_paciente['nome'] = paciente_selecionado['nome']
    return dados_do_paciente

def atualizar_janela_com_os_dados_do_paciente_selecionado(janela, dados_do_paciente):
    janela['nome_paciente'].update(dados_do_paciente['nome'])
    janela['codigo'].update(dados_do_paciente['codigo'])

def obter_dados_do_medico_selecionado(medico_selecionado):
    dados_do_medico = dict()
    dados_do_medico['crm'] = medico_selecionado['crm']
    dados_do_medico['nome'] = medico_selecionado['nome']
    return dados_do_medico

def atualizar_janela_com_os_dados_do_medico_selecionado(janela, dados_do_medico):
    janela['crm'].update(dados_do_medico['crm'])
    janela['nome_medico'].update(dados_do_medico['nome'])

def obter_dados_do_paciente_em_marcar(valores):
    dados_do_paciente = dict()
    dados_do_paciente['codigo'] = valores['codigo']
    dados_do_paciente['nome'] = valores['nome_paciente']
    return dados_do_paciente

def obter_dados_da_consulta_em_marcar(valores):
    dados_da_consulta = dict()
    dados_da_consulta['data'] = valores['data']
    dados_da_consulta['horario'] = valores['horario']
    dados_da_consulta['crm'] = valores['crm']
    dados_da_consulta['codigo'] = valores['codigo']
    return dados_da_consulta

def paciente_nao_esta_registrado(codigo_do_paciente, codigos_dos_pacientes_registrados):
    if codigo_do_paciente not in codigos_dos_pacientes_registrados:
        return True
    else:
        return False

def selecionar_paciente(janela):
    dados_do_paciente = dict()
    paciente_selecionado = tabelas.selecionar_paciente()
    if houve_um_registro_selecionado(paciente_selecionado):
        dados_do_paciente = obter_dados_do_paciente_selecionado(paciente_selecionado)
        atualizar_janela_com_os_dados_do_paciente_selecionado(janela, dados_do_paciente)
    # se não houve, dados_do_paciente permanece vazio.

def selecionar_medico(janela):
    dados_do_medico = dict()
    medico_selecionado = tabelas.selecionar_medico()
    if houve_um_registro_selecionado(medico_selecionado):
        dados_do_medico = obter_dados_do_medico_selecionado(medico_selecionado)
        atualizar_janela_com_os_dados_do_medico_selecionado(janela, dados_do_medico)
    # se não houve, dados_do_medico permanece vazio.

def marcar(valores):
    dados_do_paciente = dict()
    dados_da_consulta = dict()
    dados_do_paciente = obter_dados_do_paciente_em_marcar(valores)
    dados_da_consulta = obter_dados_da_consulta_em_marcar(valores)
    codigos_dos_pacientes = banco_de_dados.obter_codigos_dos_pacientes_registrados()
    if paciente_nao_esta_registrado(int(dados_do_paciente['codigo']), codigos_dos_pacientes):
        banco_de_dados.registrar_paciente_no_banco_de_dados(dados_do_paciente)
    # se o paciente já está registrado, ele não é registrado novamente.
    banco_de_dados.registrar_consulta_no_banco_de_dados(dados_da_consulta)
    auxiliares_a_ambos_os_metodos_salvar.mostrar_mensagem_de_registrado_com_sucesso()
