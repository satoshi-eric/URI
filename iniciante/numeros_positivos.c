#include <stdio.h>
#include <stdlib.h>


int main(int *argc, char **argv)
{
    int numbers_length = 6;
    float *numbers = malloc(numbers_length*sizeof(float));
    int positive_numbers = 0;
    for (int i = 0; i < numbers_length; i++) 
    {
        scanf("%f", &numbers[i]);
    }
    for (int i = 0; i < numbers_length; i++)
        if (numbers[i] > 0) positive_numbers++;
    
    printf("%i valores positivos\n", positive_numbers);

}
