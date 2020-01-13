#include <stdio.h>

//calcula fatorial do numero num
unsigned long long int fatorial(int num){
    long int fat = 1;
    if(num == 0){
        return 1;
    }
    while(num>0){
        fat *= num;
        num--;
    }
    return fat;
}

int main(){
    unsigned long long int M, N, soma;
    while(scanf("%lld %lld", &M, &N) != -1){
        //soma os fatoriais dos numeros e armazena em 'soma'
        soma = fatorial(M) + fatorial(N);
        printf("%lld\n", soma);   
    }
    return 0;
}