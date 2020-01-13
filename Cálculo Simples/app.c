    #include <stdio.h>

    int main(){
        typedef struct{
            int codigo;
            int quantidade;
            float valor_unitario;
        }peca;

        float valor_total;

        peca p1;
        peca p2;
        scanf("%i %i %f", &p1.codigo, &p1.quantidade, &p1.valor_unitario);
        scanf("%i %i %f", &p2.codigo, &p2.quantidade, &p2.valor_unitario);
        valor_total = (p1.quantidade * p1.valor_unitario) + (p2.quantidade * p2.valor_unitario);
        printf("VALOR A PAGAR: R$ %.2f\n", valor_total);
        return 0;
    }