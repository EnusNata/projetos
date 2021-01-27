def formatar_saida_numeros(expressao,evento):
    expressao = expressao + evento
    return expressao

def formatar_saida_operadores(expressao,evento):
    expressao = expressao + ' ' + evento + ' '
    return expressao

def formatar_saida_abertura_parenteses(expressao,evento):
    expressao = expressao + ' ' + evento
    return expressao

def formatar_saida_fechamento_parenteses(expressao,evento):
    expressao = expressao + evento + ' '
    return expressao

def formatar_saida_resultado(expressao,resultado):
    expressao = expressao + ' ' + '=' + ' ' + str(resultado)
    return expressao

def formatar_saida_apagar(expressao):
    expressao = expressao[:-1]
    return expressao

def formatar_saida_limpar(expressao):
    expressao = ''
    return expressao

def atualizar_exibicao(expressao,janela):
    janela['saida'].update(value = expressao)

def expressao_validada(resultado_expressao):
    try:
        resultado_valido = float(resultado_expressao)
        return True
    except ValueError:
        return False

def converter_resultado(resultado_expressao):
    return float(resultado_expressao)

def montar_mensagem_de_erro():
    erro = 'Expressão Invalida'
    return erro