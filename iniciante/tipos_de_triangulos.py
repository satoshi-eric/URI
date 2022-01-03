def main():
    lados = list(map(float, input().split()))
    lados.sort(reverse=True)
    A, B, C = lados

    condicoes = [
        A >= B + C,
        A**2 == B**2 + C**2,
        A**2 > B**2 + C**2,
        A**2 < B**2 + C**2,
        A == B == C,
        A == B != C or A != B == C or A == C != B
    ]

    tipos_triangulos = [
        'NAO FORMA TRIANGULO',
        'TRIANGULO RETANGULO',
        'TRIANGULO OBTUSANGULO',
        'TRIANGULO ACUTANGULO',
        'TRIANGULO EQUILATERO',
        'TRIANGULO ISOSCELES'
    ]

    if condicoes[0]:
        print(tipos_triangulos[0])
    else:
        for i, condicao in enumerate(condicoes):
            if condicao:
                print(tipos_triangulos[i])
        

if __name__ == "__main__":
    main()