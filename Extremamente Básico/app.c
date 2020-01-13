//biblioteca padrão de entradas e saídas
#include <stdio.h>

//função soma
//retorna um valor inteiro , a soma dos parâmetros recebidos pela função
int soma(int x, int y){
    return x + y;
}

//função main
int main(){
    //declaração de variáveis
    //primeiro valor da soma 'a'
    //segundo valor da soma 'b'
    //variável 's' para armazenar a soma dos números
    int a, b, s;
    //entrada para 'a'
    scanf("%i", &a);
    //entrada para 'b'
    scanf("%i", &b);
    //escreve na tela o valor da soma de 'a' e 'b'
    printf("X = %i\n", soma(a, b));
    return 0;
}