#include <stdio.h>

int main(){
    int cedula, n100, n50, n20, n10, n5, n2, n1, resto100, resto50, resto20, resto10, resto5, resto2;
    scanf("%i", &cedula);

    //calculo da quantidade de cedulas para cada valor de cedula(100, 50, 20, 10, 5, 2, 1)
    n100 = cedula/100;
    resto100 = cedula%100;

    n50 = resto100/50;
    resto50 = resto100%50;

    n20 = resto50/20;
    resto20 = resto50%20;

    n10 = resto20/10;
    resto10 = resto20%10;

    n5 = resto10/5;
    resto5 = resto10%5;

    n2 = resto5/2;
    resto2 = resto5%2;

    n1 = resto2/1;

    printf("%i\n", cedula);
    printf("%i nota(s) de R$ 100,00\n", n100);
    printf("%i nota(s) de R$ 50,00\n", n50);
    printf("%i nota(s) de R$ 20,00\n", n20);
    printf("%i nota(s) de R$ 10,00\n", n10);
    printf("%i nota(s) de R$ 5,00\n", n5);
    printf("%i nota(s) de R$ 2,00\n", n2);
    printf("%i nota(s) de R$ 1,00\n", n1);
    return 0;
}