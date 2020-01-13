#include "stdio.h"

int main(){
    //variaveis SOMA , A e B
    int SOMA, A, B;
    //entrada para 'A'
    scanf("%i", &A);
    //entrada para 'B'
    scanf("%i", &B);
    //soma 'A' e 'B' e armazena em SOMA
    SOMA = A + B;
    //escreve na tela o valor de SOMA
    printf("SOMA = %i\n", SOMA);
    return 0;
}