#include <stdio.h>
/*
Pergunta : Do que preciso inicialmente ?
Resposta : Um tabuleiro e elementos ( X, 0 ).
*/

char tabuleiro[3][3];
char xis  = 'X';
char bola = '0';

//variavel que será utilizada em diferentes funções não relacionadas
int quantidade_de_jogadas = 0;  

/*
As funções iniciadas com is se baseiam nas funções predicado, retornam um inteiro que será usado como boleano
pois no c não há tipo primitivo boleano.
*/


//inicializa todas as casas com espaço , indica que a casa está vazia.
void inicializar_tabuleiro()
{
    int linha = 0;
    int coluna = 0;

    for(linha=0; linha<3; linha++)
    {
        for(coluna=0; coluna<3; coluna++)
        {
            tabuleiro[linha][coluna] = ' ';
        }
    }
}

//vamos montar o tabuleiro por linha , no padrao [linha] [coluna]
void mostrar_tabuleiro()
{
    printf("\n");
    printf("\t\t%2c|%2c|%2c\n",tabuleiro[0][0],tabuleiro[0][1],tabuleiro[0][2]); //linha 1
    printf("\t\t--------\n");                                                       
    printf("\t\t%2c|%2c|%2c\n",tabuleiro[1][0],tabuleiro[1][1],tabuleiro[1][2]); //linha 2
    printf("\t\t--------\n");
    printf("\t\t%2c|%2c|%2c\n",tabuleiro[2][0],tabuleiro[2][1],tabuleiro[2][2]); //linha 3
    printf("\n");
    printf("\n");
}



//Verifica se a posição selecionada não ultrapassa os limites. 
//limites entre 0 e 2. 
int is_posicao_existente(int linha, int coluna)
{   
    if( linha < 0 || linha > 2 || coluna < 0 || coluna > 2 )
    {

        printf("\n");
        printf("jogada invalida\n");
        printf("jogue novamente\n");
        printf("\n");

        //caso a jogada seja invalida retorna false
        return 0;
    }
    else
    {   
        //caso a jogada seja valida retorna true
        return 1;    
    }
    
}

//verifica se a posição não está ocupada.
int is_posicao_desocupada(int linha, int coluna)
{
    if(tabuleiro[linha][coluna] != ' ') // caso o valor não seja o inicializado posiçao ocupada.
    {
        printf("\n");
        printf("posicão ocupada\n");
        printf("jogue novamente\n");
        printf("\n");

        //caso a posicao esteja ocupada retorna false.
        return 0;
    }
    else
    {
         //caso a posicao esteja desocupada retorna true.
        return 1;
    }

}

//escolhe xis ou bola automaticamente a cada jogada.
char selecionar_elemento()
{
    //se a quantidade de jogadas for par ele representa o jogador 1
    if(quantidade_de_jogadas == 0 || quantidade_de_jogadas %2 == 0)
    {
        return xis;
    }
    else
    {
        //se for impar representa o jogador 2
        return bola;
    }
    
}

//interage com os jogadores e recebe as jogadas.
void pegar_jogadas()
{
    int posicao_existente;
    int posiçao_desocupada;

    int linha;
    int coluna; 

    while(1)// equivalente a true , cria um loop infinito.
    {
        printf("Digite uma posicao no tabuleiro (linha coluna)\n");
        scanf("%d %d",&linha,&coluna);

        printf("\n");
        printf("\n");

        posicao_existente = is_posicao_existente(linha, coluna);
        posiçao_desocupada = is_posicao_desocupada(linha, coluna);

        if( posicao_existente && posiçao_desocupada )//se a posicao existe e está desocupada 
        {
            quantidade_de_jogadas++;
            tabuleiro[linha][coluna] = selecionar_elemento();
            break;
        }
        else    // se a posicao não existe ou está ocupada pede novamente a posicao.
        {
            continue;
        }
    }    
}

//verifica se há um vencedor na diagonal primária.
int is_vencedor_na_diagonal_primaria()
{
    //se houver o mesmo simbolo por toda a diagonal primaria 
    if(tabuleiro[0][0] == 'X' && tabuleiro[1][1] == 'X' && tabuleiro[2][2] == 'X'
    ||tabuleiro[0][0] == '0' && tabuleiro[1][1] == '0' && tabuleiro[2][2] == '0')
    {
        printf("\n");
        printf("parabéns, voce venceu!");
        printf("\n");
        return 1;
    }
    else
    {
        return 0;
    }
}

//verifica se há um vencedor na diagonal secundária.
int is_vencedor_na_diagonal_secundaria()
{
    //se houver o mesmo simbolo por toda a diagonal secundaria 
    if(tabuleiro[0][2] == 'X' && tabuleiro[1][1] == 'X' && tabuleiro[2][0] == 'X' 
    ||tabuleiro[0][2] == '0' && tabuleiro[1][1] == '0' && tabuleiro[2][0] == '0')
    {
        printf("\n");
        printf("parabéns, voce venceu!");
        printf("\n");
        return 1;
    }
    else
    {
        return 0;
    }
}

//verifica se há um vencedor em alguma linha.
int is_vencedor_nas_linhas()
{
    int linha  = 0;

    for(linha = 0; linha < 3; linha++)
    {
        //se houver o mesmo elemento em todas as casas da mesma linha.
        if(tabuleiro[linha][0] == 'X' && tabuleiro[linha][1] == 'X' && tabuleiro[linha][2] == 'X'
        ||tabuleiro[linha][0] == '0' && tabuleiro[linha][1] == '0' && tabuleiro[linha][2] == '0')
        {
            printf("\n");
            printf("parabéns, voce venceu!");
            printf("\n");
            return 1;
        }
    }
    //senão
    return 0;
}


//verifica se há um vencedor em alguma coluna.
int is_vencedor_nas_colunas()
{
    int coluna = 0;

    for(coluna = 0; coluna < 3; coluna++)
    {
        //se houver o mesmo elemento em todas as casas da mesma coluna.
        if(tabuleiro[0][coluna] == 'X' && tabuleiro[1][coluna] == 'X' && tabuleiro[2][coluna] == 'X'
        ||tabuleiro[0][coluna] == '0' && tabuleiro[1][coluna] == '0' && tabuleiro[2][coluna] == '0')
        {
            printf("\n");
            printf("parabéns, voce venceu!");
            printf("\n");
            return 1;
        }
        
    }
    return 0;   
}

//verifica se deu empate.
int is_empate()
{
    if(quantidade_de_jogadas == 8)
    {
        printf("\n");
        printf("parabéns, voces empataram!");
        printf("\n");
        return 1;
    }
    else
    {
        return 0;
    }
}

//verifica se o jogo terminou por algum dos motivos acima.
int is_terminado()
{
    int vencedor_na_diagonal_primaria = 0;
    int vencedor_na_diagonal_secundaria = 0;
    int vencedor_nas_linhas = 0;
    int vencedor_nas_colunas = 0;
    int empatou = 0;  

    vencedor_na_diagonal_primaria = is_vencedor_na_diagonal_primaria() ;
    vencedor_na_diagonal_secundaria = is_vencedor_na_diagonal_secundaria() ;
    vencedor_nas_linhas = is_vencedor_nas_linhas() ;
    vencedor_nas_colunas = is_vencedor_nas_colunas() ;
    empatou = is_empate();

    //se algum dos valores for verdade termina o jogo. 
    if( vencedor_na_diagonal_primaria || vencedor_na_diagonal_secundaria 
    || vencedor_nas_linhas || vencedor_nas_colunas || empatou )
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

//executa o programa.
int main()
{
    int terminou = 0;

    inicializar_tabuleiro();

    while(1)
    {
        mostrar_tabuleiro();
        pegar_jogadas();

        terminou = is_terminado();

        if(terminou)
        {
            printf("fim de jogo!");
            break;
        }
    }   
}