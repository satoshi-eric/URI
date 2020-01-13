#include <stdio.h>

int main(){
    int id, horas_trabalhadas;
    float salario_hora, salario;
    scanf("%i", &id);
    scanf("%i", &horas_trabalhadas);
    scanf("%f", &salario_hora);
    salario = salario_hora * horas_trabalhadas;
    printf("NUMBER = %i\n", id);
    printf("SALARY = U$ %.2f\n", salario);
    return 0;
}