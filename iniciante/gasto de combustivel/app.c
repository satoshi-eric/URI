#include <stdio.h>

int main(){
    FILE *input, *output, *arq;
    arq = fopen("in.txt", "w");
    input = fopen("in.txt", "r");
    output = fopen("out.txt", "w");

    const float eficiencia = 12;
    float tempo, velocidade_Media, gasto;

    printf("Digite o tempo de viagem:\n");
    scanf("%f", &tempo);
    printf("Digite o velocidade media durante a viagem:\n");
    scanf("%f", &velocidade_Media);    

    fprintf(arq, "%f %f", tempo, velocidade_Media);

    fscanf(input, "%f %f", &tempo, &velocidade_Media);
    gasto = (velocidade_Media*tempo)/eficiencia;
    fprintf(output, "%.3f\n", gasto);
    //printf("%.3f\n", gasto);
    return 0;
}