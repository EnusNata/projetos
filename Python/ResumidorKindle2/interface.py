import PySimpleGUI as sg
import resumidor


#CRIA O LAYOUT
layout = [
    [sg.Text('Nome Do Livro',size=(17,1)),sg.Input(key='nome_livro_desejado')],
    [sg.Text('Arquivo De Entrada',size=(17,1)),sg.Input(key='nome_arquivo_entrada'),sg.FileBrowse(button_text='Procurar',size=(10,1))],
    [sg.Text('Arquivo De Saida',size=(17,1)),sg.Input(key='nome_arquivo_saida'),sg.SaveAs(button_text='Definir',size=(10,1))],
    [sg.OK(button_text='Resumir'),sg.Cancel(button_text='Cancelar')]
]

#CRIA A JANELA
window = sg.Window(title='Resumir livro',layout=layout)

#LÊ AS INFORMAÇÕES VINDAS DA JANELA EM LOOP
while True:
    event, values = window.read()
    if event in(sg.WIN_CLOSED,'Cancelar'):
        break
    if event == 'Resumir':

        #ARMAZENA AS INFORMAÇÕES QUE PRECISO EM UM DICIONÁRIO
        informacoes_necessarias = dict()
        informacoes_necessarias['nome_livro_desejado'] = values['nome_livro_desejado']
        informacoes_necessarias['nome_arquivo_entrada'] = values['nome_arquivo_entrada']
        informacoes_necessarias['nome_arquivo_saida'] = values['nome_arquivo_saida']

        #RESUMI LIVRO, MOSTRA POPUP E FECHA JANELA 
        resumidor.resumir_livro(informacoes_necessarias)
        sg.popup('Livro Resumido Com Sucesso',title='Concluido')
        break

window.close()