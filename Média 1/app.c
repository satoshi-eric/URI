#include <stdio.h>

//função main
int main(){
    //declaração de variáveis 
    double MEDIA, A, B;
    //entrada para 'A'
    scanf("%lf", &A);
    //entrada para 'B'
    scanf("%lf", &B);
    //calcula média de 'A' com peso 3,5 e 'B' com peso 7,5 e armazena em MEDIA
    MEDIA = (3.5 * A + 7.5 * B)/11;
    //imprime na tela o valor da media
    printf("MEDIA = %.5lf\n", MEDIA);
    return 0;
}