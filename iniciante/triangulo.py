def verifica_triangulo(lado1, lado2, lado3):
    return not (lado1 + lado2 == lado3 or lado1 + lado3 == lado2 or lado2 + lado3 == lado1)
        
def calcular_perimetro_triangulo(lado1, lado2, lado3):
    return lado1 + lado2 + lado3

def calcular_trapezio(base1, base2, altura):
    return ((base1 + base2) / 2) * altura

def calcular(lado1, lado2, lado3):
    if verifica_triangulo(lado1, lado2, lado3):
        return "Perimetro", calcular_perimetro_triangulo(lado1, lado2, lado3)
    else:
        return "Area", calcular_trapezio(lado1, lado2, lado3)

def main():
    lados = list(map(float, input().split()))
    texto, valor = calcular(*lados)
    print(f"{texto} = {valor:.1f}")

if __name__ == "__main__":
    main()