#include <stdio.h>
#include <math.h>

int main(){
    struct ponto{
        double x;
        double y;
    }p1, p2;
    double distancia;
    scanf("%lf %lf", &p1.x, &p1.y);
    scanf("%lf %lf", &p2.x, &p2.y);
    //distancia entre 2 pontos
    distancia = sqrt(pow((p1.x - p2.x),2) + pow((p1.y - p2.y), 2));
    printf("%.4lf\n", distancia);
    return 0;
}