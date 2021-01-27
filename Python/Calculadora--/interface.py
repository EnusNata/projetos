import PySimpleGUI as sg
import funcoes_auxiliares as fa
import funcoes_calculo as fc

expression = str()
result_expression = str()
result_final = float()

#layout
layout =    [
                [sg.Text('',key='saida',size=(20,1),background_color='Black',text_color='Red',font=("Helvetica", 19))],
                [sg.Button(' cl ',key='cl'),sg.Button(' + ', key='+'),sg.Button(' - ', key='-' ), sg.Button(' <- ',key='<-')],
                [sg.Button(' 7 ', key='7' ),sg.Button(' 8 ', key='8'),sg.Button(' 9 ', key='9' ), sg.Button(' . ', key='.' )],
                [sg.Button(' 4 ', key='4' ),sg.Button(' 5 ', key='5'),sg.Button(' 6 ', key='6' ), sg.Button(' * ', key='*')],
                [sg.Button(' 1 ', key='1' ),sg.Button(' 2 ', key='2'),sg.Button(' 3 ', key='3' ), sg.Button(' / ', key='/' )],
                [sg.Button(' ( ', key='(' ),sg.Button(' 0 ', key='0'),sg.Button(' ) ', key=')' ), sg.Button(' = ', key='=')]
            ]

#janela
window = sg.Window('Calculadora Básica', layout, default_button_element_size=(5,2),auto_size_buttons=False)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED:
        break
    if event in('0','1','2','3','4','5','6','7','8','9','.'):
        expression = fa.formatar_saida_numeros(expression,event)
        fa.atualizar_exibicao(expression,window)
    if event in('+','-','*','/'):
        expression = fa.formatar_saida_operadores(expression,event)
        fa.atualizar_exibicao(expression,window)
    if event == '(':
        expression = fa.formatar_saida_abertura_parenteses(expression,event)
        fa.atualizar_exibicao(expression,window)
    if event == ')':
        expression = fa.formatar_saida_fechamento_parenteses(expression,event)
        fa.atualizar_exibicao(expression,window)
    if event == '<-':
        expression = fa.formatar_saida_apagar(expression)
        fa.atualizar_exibicao(expression,window)
    if event == 'cl':
        expression = fa.formatar_saida_limpar(expression)
        fa.atualizar_exibicao(expression,window)
    if event == '=':
        result_expression = fc.resolver_expressao(expression)
        
        if fa.expressao_validada(result_expression):
            result_final = fa.converter_resultado(result_expression)
            expression = fa.formatar_saida_resultado(expression,result_final)
            fa.atualizar_exibicao(expression,window)
        else:
            expression = fa.montar_mensagem_de_erro()
            fa.atualizar_exibicao(expression,window)