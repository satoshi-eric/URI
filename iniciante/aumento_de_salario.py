def aumento_salario(salario: float):
    reajuste = zip(
        [[0, 400], [400.01, 800], [800.01, 1200], [1200.01, 2000], [2000.01, float('inf')]],
        [15/100, 12/100, 10/100, 7/100, 4/100]
    )

    for intervalo, aumento in reajuste:
        if intervalo[0] <= salario <= intervalo[1]:
            ganho = salario * aumento
            novo_salario = salario + ganho
            percentual = aumento
            return novo_salario, ganho, percentual

def main():
    salario = float(input())
    novo_salario, ganho, percentual = aumento_salario(salario)
    print(f"Novo salario: {novo_salario:.2f}")
    print(f"Reajuste ganho: {ganho:.2f}")
    print(f"Em percentual: {percentual*100:.0f} %")

if __name__ == "__main__":
    main()