#include <stdio.h>
#include <stdlib.h>
#include <math.h>

typedef struct{
    int x;
    int y;
}coordenadas;

int main(){
    float distancia = 0;
    int numeroComputadores, i, j;
    coordenadas coord[2000];
    scanf("%i", &numeroComputadores);
    for(i = 0; i < numeroComputadores; i++){
        scanf("%i %i", &coord[i].x, &coord[i].y);
    }
    for(j = 0; j < numeroComputadores; j++){
        if(j = numeroComputadores - 1){
            distancia += sqrt(
                ((coord[j].x - coord[j].x) * (coord[0].x - coord[j].x))
                + 
                ((coord[j].y - coord[j].y)*(coord[0].y - coord[j].y))
            );
            break;
        }         
        printf("%i\n", j);
        distancia += sqrt(
            ((coord[j+1].x - coord[j].x) * (coord[j+1].x - coord[j].x))
            + 
            ((coord[j+1].y - coord[j].y)*(coord[j+1].y - coord[j].y))
            );
           
        printf("%.2f\n", distancia);
    }
    printf("tera que comprar uma fita de tamanho %.2f\n", distancia);
    return 0;
}