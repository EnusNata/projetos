#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//cabeçalhos

void mostrar_mensagem_jogador_errou();
void mostrar_mensagem_jogador_acertou();
void mostrar_mensagem_depois_da_jogada();

void mostrar_mensagem_pontuacao_dos_jogadores();

void mostrar_mensagem_pedir_primeira_carta();
void mostrar_mensagem_pedir_segunda_carta();

void mostrar_mensagem_de_empate();
void mostrar_mensagem_de_vitoria();
void mostrar_mensagem_de_fim_de_jogo();

void mostrar_mensagem_posicao_invalida();

void mostrar_mensagem_indice_linha(int linha);
void mostrar_mensagem_indice_coluna();

int is_jogada_inicial();
int is_cartas_iguais();

int is_empate();
int is_vitoria();
int is_terminado();

//cabeçalhos

// caso todos os jogadores estejam nessa posição definimos a atual jogada como inicial. 
#define POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES -1


// estruturas principais do jogo.
typedef struct
{
    int linha;
    int coluna;

}PosicaoSelecionada;

typedef struct
{
    int identificador_do_jogador;
    int quantidade_de_pontos;
    PosicaoSelecionada posicao_primeira_carta;
    PosicaoSelecionada posicao_segunda_carta;
}Jogador;
// estruturas principais do jogo.

//cabeçalhos

int is_posicao_existente(PosicaoSelecionada posicao_selecionada);
int is_carta_invalida(PosicaoSelecionada posicao_selecionada);
int is_carta_na_posicao_oculta(PosicaoSelecionada posicao_selecionada);

//cabeçalhos

//jogadores do jogo da memória.
Jogador Jogador1;
Jogador Jogador2;
//jogadores do jogo da memória.

//ponteiro que será utilizado para definir quem é jogador atual, o jogador1 ou o jogador2.
//definido dinamicamente.
Jogador *jogador_atual;


//variaveis utilizadas para configurar as estruturas do jogo.
enum jogadores{ jogador1 = 1, jogador2 = 2};
enum status_da_carta{ OCULTAR = 0, EXIBIR = 1, VERIFICAR  = 2};
//variaveis utilizadas para configurar as estruturas do jogo.

//variaveis que representam as cartas e tratam a lógica do jogo.
int cartas[4][4];
int mostruario[4][4];
//variaveis que representam as cartas e tratam a lógica do jogo.

void identificar_jogadores()
{
    Jogador1.identificador_do_jogador = jogador1;
    Jogador2.identificador_do_jogador = jogador2;
}

void definir_posicoes_iniciais_das_cartas_dos_jogadores()
{
    Jogador1.posicao_primeira_carta.linha = POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES;
    Jogador1.posicao_primeira_carta.coluna = POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES;
    
    Jogador2.posicao_primeira_carta.linha = POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES;
    Jogador2.posicao_primeira_carta.coluna = POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES;
}

//aloca memória para o jogador atual.
void inicializar_jogador_atual()
{
    jogador_atual = (Jogador *) malloc(sizeof(Jogador));
}

void inicializar_jogadores()
{
    identificar_jogadores();
    definir_posicoes_iniciais_das_cartas_dos_jogadores();
    inicializar_jogador_atual();
}

void inicializar_cartas()
{
    // gabarito do jogo para ajudar a testar.
    cartas[0][0] = 1;
    cartas[0][1] = 2;
    cartas[0][2] = 3;
    cartas[0][3] = 4;

    cartas[1][0] = 5;
    cartas[1][1] = 6;
    cartas[1][2] = 7;
    cartas[1][3] = 8;

    cartas[2][0] = 1;
    cartas[2][1] = 2;
    cartas[2][2] = 3;
    cartas[2][3] = 4;

    cartas[3][0] = 5;
    cartas[3][1] = 6;
    cartas[3][2] = 7;
    cartas[3][3] = 8;
}

void inicializar_mostruario()
{
    int linha;
    int coluna;

    for(linha = 0; linha < 4; linha++)
    {
        for(coluna = 0; coluna < 4; coluna++)
        {
            // o jogo inicia com todas as cartas ocultas.
            mostruario[linha][coluna] = OCULTAR;
        }
    }
}


void mostrar_mesa()
{
    int linha;
    int coluna;

    mostrar_mensagem_indice_coluna();
    for(linha = 0; linha < 4; linha++)
    {
        //inicia cada linha 2 tabs a direita.
        printf("\t\t");
        mostrar_mensagem_indice_linha(linha);

        for(coluna = 0; coluna < 4; coluna++)
        {
            // se a carta já foi escolhida corretamente ou foi escolhida durante essa jogada.
            if( (mostruario[linha][coluna] == EXIBIR)  || (mostruario[linha][coluna] == VERIFICAR) ) 
            {
                printf("[%d]",cartas[linha][coluna]); //mostra a carta
            }
            else //senão
            {
                printf("[*]"); // oculta a carta
            }
        }
        printf("\n\n");
    }
}


Jogador* pegar_proximo_jogador()
{
    int identidade_jogador_atual;
    
    identidade_jogador_atual = jogador_atual->identificador_do_jogador;

    //se o jogador acertou continua como jogador atual. 
    if(is_cartas_iguais())
    {
        if(identidade_jogador_atual == jogador1)//se o jogador que acertou é o jogador 1.
        {
            return &Jogador1;
        }
        else    //se o jogador que acertou é o jogador 2.
        {
            return &Jogador2;
        }
        
    }
    else  // se o jogador errou é a vez do outro
    {
        if(identidade_jogador_atual == jogador1)//se o jogador que errou é o jogador 1.
        {
            return &Jogador2;
        }
        else    //se o jogador que errou é o jogador 2.
        {
            return &Jogador1;
        }
    }
}

Jogador* pegar_jogador_atual()
{
    if(is_jogada_inicial())
    {
        return &Jogador1;
    }
    else
    {
        return pegar_proximo_jogador();
    }
    
}

void marcar_carta_como_selecionada(PosicaoSelecionada posicao_selecionada)
{
    mostruario[posicao_selecionada.linha][posicao_selecionada.coluna] = VERIFICAR;
}
 
void exibir_cartas_selecionadas()
{
    mostruario[jogador_atual->posicao_primeira_carta.linha][jogador_atual->posicao_primeira_carta.coluna] = EXIBIR;
    mostruario[jogador_atual->posicao_segunda_carta.linha][jogador_atual->posicao_segunda_carta.coluna] = EXIBIR;
}

void ocultar_cartas_selecionadas()
{
    mostruario[jogador_atual->posicao_primeira_carta.linha][jogador_atual->posicao_primeira_carta.coluna] = OCULTAR;
    mostruario[jogador_atual->posicao_segunda_carta.linha][jogador_atual->posicao_segunda_carta.coluna] = OCULTAR;
    
}

void atualizar_pontuacao_do_jogador()
{
    jogador_atual->quantidade_de_pontos++;
}

void atualizar_status_do_jogador()
{
    if(is_cartas_iguais())
    {
        exibir_cartas_selecionadas();
        atualizar_pontuacao_do_jogador();
    }
    else
    {
        ocultar_cartas_selecionadas();
    }
} 

void pegar_posicao_primeira_carta()
{
    scanf("%d",&jogador_atual->posicao_primeira_carta.linha);
    scanf("%d",&jogador_atual->posicao_primeira_carta.coluna);

    jogador_atual->posicao_primeira_carta.linha--;
    jogador_atual->posicao_primeira_carta.coluna--;
}

PosicaoSelecionada pegar_posicao_primeira_carta_selecionada()
{
    PosicaoSelecionada posicao_selecionada;

    posicao_selecionada.linha = jogador_atual->posicao_primeira_carta.linha;
    posicao_selecionada.coluna = jogador_atual->posicao_primeira_carta.coluna;

    return posicao_selecionada;
}

void pegar_primeira_jogada()
{
    PosicaoSelecionada posicao_selecionada;

    do
    {
        mostrar_mensagem_pedir_primeira_carta();
        pegar_posicao_primeira_carta();    
        posicao_selecionada = pegar_posicao_primeira_carta_selecionada();
        

        if(is_carta_invalida(posicao_selecionada))
        {
            mostrar_mensagem_posicao_invalida();
        }

    } while (is_carta_invalida(posicao_selecionada));
    
    marcar_carta_como_selecionada(posicao_selecionada);

}

void pegar_posicao_segunda_carta()
{
    scanf("%d",&jogador_atual->posicao_segunda_carta.linha);
    scanf("%d",&jogador_atual->posicao_segunda_carta.coluna);

    jogador_atual->posicao_segunda_carta.linha--;
    jogador_atual->posicao_segunda_carta.coluna--;
}

PosicaoSelecionada pegar_posicao_segunda_carta_selecionada()
{
    PosicaoSelecionada posicao_selecionada;

    posicao_selecionada.linha = jogador_atual->posicao_segunda_carta.linha;
    posicao_selecionada.coluna = jogador_atual->posicao_segunda_carta.coluna;

    return posicao_selecionada;
}

void pegar_segunda_jogada()
{
    PosicaoSelecionada posicao_selecionada;

    do
    {
        mostrar_mensagem_pedir_segunda_carta();
        pegar_posicao_segunda_carta();
        
        posicao_selecionada = pegar_posicao_segunda_carta_selecionada();
        

        if(is_carta_invalida(posicao_selecionada))
        {
            mostrar_mensagem_posicao_invalida();    
        }

    } while (is_carta_invalida(posicao_selecionada));
    
    marcar_carta_como_selecionada(posicao_selecionada);
}

void pausar_para_ver_a_mesa()
{
    sleep(3);
}

void pegar_jogadas()
{
    jogador_atual = pegar_jogador_atual();

    pegar_primeira_jogada();
    mostrar_mesa();
    pausar_para_ver_a_mesa();

    pegar_segunda_jogada();
    mostrar_mesa();
    pausar_para_ver_a_mesa();

    atualizar_status_do_jogador();
    mostrar_mensagem_depois_da_jogada();
    pausar_para_ver_a_mesa();
    mostrar_mesa();
}

int main()
{
    int terminou = 0;

    inicializar_jogadores();
    inicializar_cartas();
    inicializar_mostruario();

    mostrar_mesa();

    do
    {
        pegar_jogadas();
        terminou = is_terminado();

        if(terminou)
        {
            mostrar_mensagem_de_fim_de_jogo();
        }
    } while (!terminou);    //enquanto não terminou.   
}

/*
AS FUNÇÕES ABAIXO SÃO FUNÇÕES QUE MOSTRARÃO MENSAGENS AO USUÁRIO,
VARIAM DESDE UMA SIMPLES DEMONSTRAÇÃO DE INDICE ATÉ MOSTRAR AS PONTUAÇÕES DOS JOGADORES.
*/

void mostrar_mensagem_indice_linha(int linha)
{
    printf("%d", linha + 1);
}

void mostrar_mensagem_indice_coluna()
{
    printf("\t\t");
    printf("  1 ");
    printf(" 2 ");
    printf(" 3 ");
    printf(" 4 ");
    printf("\n");
}

void mostrar_mensagem_posicao_invalida()
{
        printf("\n\nA POSICAO ESCOLHIDA JA FOI SELECIONADA OU NAO EXISTE\n");
        printf("JOGUE NOVAMENTE!\n\n");
}

void mostrar_mensagem_de_vitoria()
{
    printf("\n\n\nPARABÉNS JOGADOR%d, VOCÊ VENCEU!\n\n\n",jogador_atual->identificador_do_jogador);

}

void mostrar_mensagem_de_empate()
{
    printf("\n\n\nQUE PENA, VOCÊS EMPATARAM!\n\n\n");
}

void mostrar_mensagem_de_fim_de_jogo()
{
    if(is_vitoria())
    {
        mostrar_mensagem_de_vitoria();
    }
    else
    {
        if(is_empate())
        {
            mostrar_mensagem_de_empate();
        }
    }
}

void mostrar_mensagem_pedir_primeira_carta()
{
    printf("DIGITE A POSICAO DA PRIMEIRA CARTA (linha coluna)\n");
}

void mostrar_mensagem_pedir_segunda_carta()
{
    printf("DIGITE A POSICAO DA SEGUNDA CARTA (linha coluna)\n");
}

void mostrar_mensagem_pontuacao_dos_jogadores()
{
    printf("\t\tPONTUAÇÕES\n\n");
    printf("JOGADOR 1 = %d PONTOS.\n",Jogador1.quantidade_de_pontos);
    printf("JOGADOR 2 = %d PONTOS.\n",Jogador2.quantidade_de_pontos);
    printf("\n\n");
}

void mostrar_mensagem_jogador_acertou()
{
    printf("\nO JOGADOR ATUAL ACERTOU, CONTINUE JOGANDO!\n\n");
}

void mostrar_mensagem_jogador_errou()
{
    printf("\nO JOGADOR ATUAL ERROU, VEZ DO PROXIMO JOGADOR!\n\n");
}

void mostrar_mensagem_depois_da_jogada()
{
    if(is_cartas_iguais())
    {
        mostrar_mensagem_jogador_acertou();
    }
    else
    {
        mostrar_mensagem_jogador_errou();
    }
    mostrar_mensagem_pontuacao_dos_jogadores();
}

/*
AS FUNÇÕES ABAIXO SÃO FUNÇÕES PREDICADO,
RETORNAM UM VALOR BOLEANO QUE REPRESENTA VERDADEIRO (1) OU FALSO (0).
*/

int is_jogada_inicial()
{
    if(
        Jogador1.posicao_primeira_carta.linha == POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES  &&
        Jogador1.posicao_primeira_carta.coluna == POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES &&
        Jogador2.posicao_primeira_carta.linha == POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES  &&   
        Jogador2.posicao_primeira_carta.coluna == POSICAO_INICIAL_DAS_CARTAS_DOS_JOGADORES 
    )
    {
        return 1;
    }
    else
    {
        return 0;
    }
    
}

int is_cartas_iguais()
{
    if( cartas[jogador_atual->posicao_primeira_carta.linha][jogador_atual->posicao_primeira_carta.coluna] 
    ==  cartas[jogador_atual->posicao_segunda_carta.linha][jogador_atual->posicao_segunda_carta.coluna]
    )
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int is_posicao_existente(PosicaoSelecionada posicao_selecionada)
{
    if( (posicao_selecionada.linha >= 0 && posicao_selecionada.linha <= 3) && 
        (posicao_selecionada.coluna >= 0 && posicao_selecionada.coluna <= 3)
    )
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int is_carta_na_posicao_oculta(PosicaoSelecionada posicao_selecionada)
{
    if( mostruario[posicao_selecionada.linha][posicao_selecionada.coluna] == OCULTAR )
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int is_carta_invalida(PosicaoSelecionada posicao_selecionada)
{
    if( is_posicao_existente(posicao_selecionada) && is_carta_na_posicao_oculta(posicao_selecionada)
    )
    {
        return 0;
    }
    else
    {
        return 1;
    }
}

int is_vitoria()
{
    if(Jogador1.quantidade_de_pontos == 5 || Jogador2.quantidade_de_pontos == 5)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int is_empate()
{
    if(Jogador1.quantidade_de_pontos == 4 && Jogador2.quantidade_de_pontos == 4)
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int is_terminado()
{
    if(is_vitoria() || is_empate())
    {
        return 1;
    }
    else
    {
        return 0;
    }
}