//calcula a media das notas 'A' , 'B' e 'C'
#include <stdio.h>

int main(){
    //declaração de variáveis
    double A, B, C, media;
    //entrada das variáveis para as notas
    scanf("%lf", &A);
    scanf("%lf", &B);
    scanf("%lf", &C);
    //calcula a média das notas de pesos 2, 3 e 5
    media = ((2*A) + (3*B) + (5*C))/10;
    //imprime na tela a media com formtação de 1 digito depois da vírgula
    printf("MEDIA = %.1lf\n", media);
    return 0;
}