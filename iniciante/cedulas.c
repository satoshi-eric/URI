#include <stdio.h>
#include <stdlib.h>

/*
 Leia um valor de ponto flutuante com duas casas decimais. Este valor representa um valor monetário. A seguir, calcule o menor número de notas e moedas possíveis no qual o valor pode ser decomposto. As notas consideradas são de 100, 50, 20, 10, 5, 2. As moedas possíveis são de 1, 0.50, 0.25, 0.10, 0.05 e 0.01. A seguir mostre a relação de notas necessárias.\    
*/

// Entrada
/*
O arquivo de entrada contém um valor de ponto flutuante N (0 ≤ N ≤ 1000000.00).
*/

// Saída
/*
Imprima a quantidade mínima de notas e moedas necessárias para trocar o valor inicial, conforme exemplo fornecido.
*/

int *get_banknotes_amount(float money)
{
    static int banknotes_amount[6] = {0, 0, 0, 0, 0, 0};
    double banknotes_values[6] = {100, 50, 20, 10, 5, 2};
    for(int i = 0; i < 6; i++)
    {   
        printf("%f\n", money);
        if((money - banknotes_values[i]) >= 0)
        {
            money -= banknotes_values[i];
            banknotes_amount[i]++;
            printf("%f", money);
        }
    }
    return banknotes_amount;
}

int main()
{
    float value;
    scanf("%f", &value);

    int *banknotes_amount = get_banknotes_amount(value);
    printf("%i", banknotes_amount[0]);
}