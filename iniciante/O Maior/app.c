#include <stdio.h>

/*
int main(){
    int valores[3], aux;
    //entrada para 3 valores
    for(int i = 0; i<3; i++){
        scanf("%i", &valores[i]);    
    }
    //ordenação do vetor
    for(int j = 0; j<2; j++){
        if(valores[j]>valores[j+1]){
            aux = valores[j];
            valores[j] = valores[j+1];
            valores[j+1] = aux;
        }
    }
    printf("%i eh o maior\n", valores[2]);
    return 0;
}
 */

int main(){
    int valor[3], i, j, aux = 0;
    //entrada para os valores
    for(i = 0; i<3; i++){
        scanf("%i", &valor[i]);
    }
    //busca o maior valor
    for(j=0; j<3; j++){
        if(valor[j]>aux){
            aux = valor[j];
        }
    }
    printf("%i eh o maior\n", aux);
    return 0;
}