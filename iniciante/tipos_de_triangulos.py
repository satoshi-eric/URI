A = float(input())
B = float(input())
C = float(input())

nums = [A, B, C]
nums.sort(reverse=True)

A = nums[0]
B = nums[1]
C = nums[2]

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

index_classificacoes = []
for i in range(len(condicoes)):
    if condicoes[i] == True:
        index_classificacoes.append(i)

if 0 in index_classificacoes:
    print(tipos_triangulos[0])
else:
    for index in index_classificacoes:
        print(tipos_triangulos[index])