import sqlite3 as sq

def conectar_ao_banco():
    return sq.connect('SistemaHospitalar.db', detect_types=sq.PARSE_COLNAMES)

def obter_registros(consulta):
    connection = conectar_ao_banco()
    cursor = connection.cursor()

    #pegar nome das colunas começo
    cursor.execute(consulta)
    nomes_das_colunas = []

    for tuple_column in cursor.description:
        for column in tuple_column:
            if column != None:
                nomes_das_colunas.append(column)
    #pegar nome das colunas final

    #pegar registros inicio
    cursor.execute(consulta)
    registros_da_tabela = cursor.fetchall()
    # pegar registros fim

    informacoes_da_tabela = dict()

    informacoes_da_tabela['colunas'] = nomes_das_colunas
    informacoes_da_tabela['registros'] = registros_da_tabela
    return informacoes_da_tabela

def obter_medicos_registrados():
    informacoes_da_tabela_medico = dict()
    consulta = "select * from MEDICO"
    informacoes_da_tabela_medico = obter_registros(consulta)
    return informacoes_da_tabela_medico

def obter_pacientes_registrados():
    informacoes_da_tabela_paciente = dict()
    consulta = "select * from PACIENTE"
    informacoes_da_tabela_paciente = obter_registros(consulta)
    return informacoes_da_tabela_paciente

def obter_consultas_registradas():
    informacoes_da_tabela_consulta = dict()
    consulta = '''  select  p.nome as paciente, 
                            p.codigo, 
                            m.nome as medico, 
                            m.crm,
                            c.data, 
                            c.hora 
                    from consulta c 
                        join paciente p 
                            using(codigo) 
                        join medico m 
                            using(crm)'''

    informacoes_da_tabela_consulta = obter_registros(consulta)
    return informacoes_da_tabela_consulta

def obter_codigos_dos_pacientes_registrados():
    informacoes_da_tabela_paciente = dict()
    codigos_dos_pacientes = list()
    consulta = "select codigo from PACIENTE"
    informacoes_da_tabela_paciente = obter_registros(consulta)

    lista_de_tuplas = informacoes_da_tabela_paciente['registros']
    for tupla in lista_de_tuplas:
        for codigo in tupla:
            codigos_dos_pacientes.append(codigo)
    return codigos_dos_pacientes

def salvar_alteracoes_no_banco_de_dados(connection, cursor):
    cursor.fetchall()
    connection.commit()
    connection.close()

def registrar_medico_no_banco_de_dados(dados_do_medico):
    connection = conectar_ao_banco()
    cursor = connection.cursor()
    cursor.execute('insert into MEDICO values(?,?)', (dados_do_medico['nome'], dados_do_medico['crm']) )
    salvar_alteracoes_no_banco_de_dados(connection, cursor)

def registrar_paciente_no_banco_de_dados(dados_do_paciente):
    connection = conectar_ao_banco()
    cursor = connection.cursor()
    cursor.execute('insert into PACIENTE values(?,?)', (dados_do_paciente['codigo'], dados_do_paciente['nome']))
    salvar_alteracoes_no_banco_de_dados(connection, cursor)

def registrar_consulta_no_banco_de_dados(dados_da_consulta):
    connection = conectar_ao_banco()
    cursor = connection.cursor()
    cursor.execute('insert into CONSULTA values(?,?,?,?)', (dados_da_consulta['data'], dados_da_consulta['horario'], dados_da_consulta['crm'], dados_da_consulta['codigo']))
    salvar_alteracoes_no_banco_de_dados(connection, cursor)