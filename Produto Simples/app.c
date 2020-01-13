#include <stdio.h>

int main(){
    //declaração de variáveis 
    int PROD, A, B;
    //entrada para 'A'
    scanf("%i", &A);
    //entrada para 'B'
    scanf("%i", &B);
    //efetua o produto entre 'A' e 'B' e armazena em 'PROD'
    PROD = A * B;
    //escreve na tela o produto de 'A' e 'B' 
    printf("PROD = %i\n", PROD);
    return 0;
}