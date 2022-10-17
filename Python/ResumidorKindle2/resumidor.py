import re

def resumir_livro(informacoes_necessarias):

    # OBTEM OS NOMES DOS ARQUIVOS DE ENTRADA , SAIDA E DO LIVRO
    nome_arquivo_entrada = informacoes_necessarias['nome_arquivo_entrada']
    nome_arquivo_saida = informacoes_necessarias['nome_arquivo_saida']
    nome_livro_desejado = informacoes_necessarias['nome_livro_desejado']
    # OBTEM OS NOMES DOS ARQUIVOS DE ENTRADA , SAIDA E DO LIVRO

    
    #ABRE O ARQUIVO PARA LEITURA
    arquivo_entrada = open( file=nome_arquivo_entrada , mode='r' , encoding='utf-8' )

    #TODOS OS TEXTOS DO ARQUIVO , LOCAL ONDE SERÁ REALIZADA A BUSCA  
    texto_arquivo_entrada = list()
    texto_arquivo_entrada = arquivo_entrada.readlines()

    #FECHA O ARQUIVO DE LEITURA
    arquivo_entrada.close()

    #TEXTO DO LIVRO SENDO LIDO NO LOOP
    texto_livro_atual = list()

    #TEXTO DO LIVRO QUE DESEJO
    texto_selecionado = str()

    #RESUMO FINAL COM TODOS OS TEXTOS DO LIVRO
    resumo = list()
    
    #LE 5 LINHAS DO ARQUIVO, - A ESTRUTURA DE UM DESTAQUE OU NOTA - 
    while len(texto_arquivo_entrada) != 0:
        contador = 0
        while contador < 5:
            texto_livro_atual.append(texto_arquivo_entrada.pop(0))
            contador = contador + 1
    #LE 5 LINHAS DO ARQUIVO, - A ESTRUTURA DE UM DESTAQUE OU NOTA -

        #ESTRUTURA DO DESTAQUE OU NOTA
        '''
        texto_livro_atual[0] = NOME DO LIVRO
        texto_livro_atual[1] = TEXTO INFORMATIVO NOTA OU HIGHLIGHT
        texto_livro_atual[2] = VAZIO, QUEBRA DE LINHA
        texto_livro_atual[3] = TEXTO QUE DESEJO
        texto_livro_atual[4] = FIM DA NOTA , MARCADOR DE FINAL
        '''
        #ESTRUTURA DO DESTAQUE OU NOTA

        #FORMATOS QUE O NOME DO LIVRO ASSUME NO ARQUIVO NA PRIMEIRA VEZ EM QUE APARECE E DA SEGUNDA EM DIANTE
        nome_livro_desejado_formatado_um = nome_livro_desejado+"\n"
        nome_livro_desejado_formatado_dois = "\ufeff"+nome_livro_desejado+"\n"
        #FORMATOS QUE O NOME DO LIVRO ASSUME NO ARQUIVO NA PRIMEIRA VEZ EM QUE APARECE E DA SEGUNDA EM DIANTE

        #FORMATOS QUE O DESTAQUE OU HIGHLIGHT PODEM ASSUMIR
        destaque_formato_um = "- Seu destaque ou posição"
        destaque_formato_dois = "- Your Highlight on"
        #FORMATOS QUE O DESTAQUE OU HIGHLIGHT PODEM ASSUMIR

        #VERIFICA SE O LIVRO ATUAL É O QUE DESEJO E SE É UM DESTAQUE OU HIGHLIGHT,  E SE FOR, SELECIONA O TEXTO 
        if (texto_livro_atual[0] == nome_livro_desejado_formatado_um or texto_livro_atual[0] == nome_livro_desejado_formatado_dois) and (re.findall(destaque_formato_um, texto_livro_atual[1]) or re.findall(destaque_formato_dois, texto_livro_atual[1])):
            texto_selecionado = texto_livro_atual[3]
        #VERIFICA SE O LIVRO ATUAL É O QUE DESEJO E SE É UM DESTAQUE OU HIGHLIGHT,  E SE FOR, SELECIONA O TEXTO    

            #ADICIONA O TEXTO AO ARQUIVO E PULA UMA LINHA
            resumo.append(texto_selecionado)
            resumo.append("\n")
            #ADICIONA O TEXTO AO ARQUIVO E PULA UMA LINHA

        #REMOVE O DESTAQUE OU NOTA ATUAL        
        while len(texto_livro_atual) != 0:
            texto_livro_atual.pop(0)

    #ABRE O ARQUIVO PARA GRAVACAO
    arquivo_saida = open( file=nome_arquivo_saida , mode="w" , encoding="utf-8" )

    #GRAVA O RESUMO NO ARQUIVO DE SAÍDA
    while len(resumo) != 0:
        arquivo_saida.write(resumo.pop(0))

    #FECHO O ARQUIVO DE GRAVACAO
    arquivo_saida.close()