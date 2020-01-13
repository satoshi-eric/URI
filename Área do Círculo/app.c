    //biblioteca padrão de entradas e saídas
    #include <stdio.h>
    //definindo pi como 3.14159
    #define pi 3.14159

    //função main
    int main(){
        //decalaração das variáveis area e raio
        double area , raio;
        //entrada para valor do raio
        scanf("%lf", &raio);
        //conta da area
        //multiplica raio por ele mesmo, multiplica pelo pi e armazena p resultado em area
        area = pi * (raio * raio);
        //imprime na tela o resultado da área
        printf("A=%.4lf\n", area);
        return 0;
    }