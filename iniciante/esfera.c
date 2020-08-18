#include  <stdio.h>

int main(){
    //constante pi
    const double pi = 3.14159; 
    double volume, raio;
    scanf("%lf", &raio);
    //cálculo do volume da esfera
    volume =  (4.0/3.0) * pi * raio * raio * raio;
    printf("VOLUME = %.3lf\n", volume);
    return 0;
}