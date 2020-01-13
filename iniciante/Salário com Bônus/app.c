#include <stdio.h>

int main(){
    char nome[200];
    double salario_fixo, salario_recebido, valor_total_das_vendas;
    fgets(nome, 200, stdin);
    scanf("%lf", &salario_fixo);
    scanf("%lf", &valor_total_das_vendas);
    salario_recebido = salario_fixo + (0.15 * valor_total_das_vendas);
    printf("TOTAL = R$ %.2lf\n", salario_recebido);
    return 0;
}