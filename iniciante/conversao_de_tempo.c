//converte a entrada (segundos) em formato de horário (horas:minutos:segundos) 
#include <stdio.h>

int main(){
    int segundos_input, segundos, minutos, horas, resto_segundos, resto_minutos, resto_horas;
    scanf("%i", &segundos_input);
    
    horas = segundos_input/3600;
    resto_horas = segundos_input%3600;
    
    
    minutos = resto_horas/60;
    resto_minutos = resto_horas%60;

    segundos = resto_minutos;

    printf("%i:%i:%i\n", horas, minutos, segundos);
    return 0;
}