import re

pegar_parenteses_internos = r'[(]{1}[^\(\)]+[)]{1}'
pegar_soma = r'((?:-?\d+(?:\.\d+)?)\s\+\s(?:-?\d+(?:\.\d+)?))'
pegar_subtracao = r'((?:-?\d+(?:\.\d+)?)\s\-\s(?:-?\d+(?:\.\d+)?))'
pegar_multiplicacao = r'((?:-?\d+(?:\.\d+)?)\s\*\s(?:-?\d+(?:\.\d+)?))'
pegar_divisao = r'((?:-?\d+(?:\.\d+)?)\s\/\s(?:-?\d+(?:\.\d+)?))'

def resolver_parenteses(expressao):
    expressao_resolvida = expressao

    while re.findall( pegar_parenteses_internos , expressao_resolvida ):

        lista_parenteses = re.findall( pegar_parenteses_internos , expressao_resolvida )

        parenteses_interno = lista_parenteses[0]
        expressao_parenteses_interno = parenteses_interno[1:-1] #remove o parenteses para resolver a expressao.
        resultado_parenteses_interno = resolver_expressao(expressao_parenteses_interno)

        expressao_resolvida = expressao_resolvida.replace( parenteses_interno, str(resultado_parenteses_interno), 1 )
    return expressao_resolvida


def resolver_multiplicacao(expressao):
    expressao_resolvida = expressao
    
    while re.findall( pegar_multiplicacao , expressao_resolvida ):
        
        #esse retorno é uma lista.
        multiplicacoes = re.findall( pegar_multiplicacao , expressao_resolvida )

        #ao chegar nesse modulo todas as multiplicacao devem possuir mesma prioridade.
        operacao_multiplicacao = multiplicacoes[0]
        resultado_multiplicacao =  eval(operacao_multiplicacao)

        #devemos resolver uma operacao, substituí-la
        expressao_resolvida = expressao_resolvida.replace(operacao_multiplicacao, str(resultado_multiplicacao), 1)
    return expressao_resolvida

def resolver_divisao(expressao):
    expressao_resolvida = expressao
    
    while re.findall( pegar_divisao , expressao_resolvida ):
        
        divisoes = re.findall( pegar_divisao , expressao_resolvida )

        operacao_divisao = divisoes[0]
        resultado_divisao =  eval(operacao_divisao)

        expressao_resolvida = expressao_resolvida.replace(operacao_divisao, str(resultado_divisao), 1)
    return expressao_resolvida

def resolver_soma(expressao):
    expressao_resolvida = expressao

    while re.findall( pegar_soma , expressao_resolvida ):
        
        somas = re.findall( pegar_soma , expressao_resolvida )

        operacao_soma = somas[0]
        resultado_soma = eval(operacao_soma)

        expressao_resolvida = expressao_resolvida.replace( operacao_soma, str(resultado_soma) , 1) 
    return expressao_resolvida

def resolver_subtracao(expressao):
    expressao_resolvida = expressao

    while re.findall( pegar_subtracao , expressao_resolvida ):
        
        subtracoes = re.findall( pegar_subtracao , expressao_resolvida )

        operacao_subtracao = subtracoes[0]
        resultado_subtracao = eval(operacao_subtracao)

        expressao_resolvida = expressao_resolvida.replace( operacao_subtracao, str(resultado_subtracao) , 1) 
    return expressao_resolvida

def resolver_expressao(expressao):

    resultado_parenteses = resolver_parenteses(expressao)

    resultado_multiplicacao = resolver_multiplicacao(resultado_parenteses)

    resultado_divisao = resolver_divisao(resultado_multiplicacao)

    resultado_soma = resolver_soma(resultado_divisao)

    resultado_subtracao = resolver_subtracao(resultado_soma)

    resultado_final = resultado_subtracao

    return resultado_final