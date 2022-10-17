import re

def obter_metadados_livro_atual(texto_livro_atual):
    '''Recebe um lista com a estrutura de uma nota ou destaque e retorna um dicionário nomeando cada linha por indice'''

    metadados_livro_atual = dict()

    metadados_livro_atual['nome'] = texto_livro_atual[0]
    metadados_livro_atual['destaque_ou_nota'] = texto_livro_atual[1]
    metadados_livro_atual['formatacao'] = texto_livro_atual[2]
    metadados_livro_atual['texto'] = texto_livro_atual[3]
    metadados_livro_atual['fim'] = texto_livro_atual[4]

    return metadados_livro_atual

def is_livro_desejado(nome_livro_desejado, nome_livro_atual):
    '''Informa se o livro atual é o livro desejado, retorna um boolean'''

    nome_livro_desejado_um = nome_livro_desejado+"\n"
    nome_livro_desejado_dois = "\ufeff"+nome_livro_desejado+"\n"

    if nome_livro_atual == nome_livro_desejado_um or nome_livro_atual == nome_livro_desejado_dois:
        return True
    else:
        return False

def is_destaque(destaque_ou_nota):
    '''verifica se a estrutura contem um destaque ou highlight, retorna um boolean'''

    constante_destaque_um = "- Seu destaque ou posição"
    constante_destaque_dois = "- Your Highlight on"
    if re.findall(constante_destaque_um, destaque_ou_nota) or re.findall(constante_destaque_dois, destaque_ou_nota):
        return True
    else:
        return False

def obter_texto_selecionado(nome_livro_desejado, metadados_livro_atual):
    '''retorna o texto que desejo , ou uma constante que será usada como flag'''

    mensagem = "nao salvar"

    if is_livro_desejado(nome_livro_desejado, metadados_livro_atual['nome']) and is_destaque(metadados_livro_atual['destaque_ou_nota']):
        return metadados_livro_atual['texto']
    else:
        return mensagem

def adicionar_texto_ao_resumo(texto, resumo):
    '''adiciona o texto ao resumo, adiciona uma linha e retorna o resumo.'''

    formatacao = "\n"

    if texto != "nao salvar":
        resumo.append(texto)
        resumo.append(formatacao)

        return resumo
    else:
        return resumo