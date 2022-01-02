def bubble_sort(vetor: list):
    vetor_ordenado = list(vetor)
    for i in range(len(vetor_ordenado)):
        for j in range(len(vetor_ordenado) - 1):
            if vetor_ordenado[j] > vetor_ordenado[j + 1]:
                vetor_ordenado[j], vetor_ordenado[j + 1] = vetor_ordenado[j + 1], vetor_ordenado[j]
    return vetor_ordenado

def main():
    vetor = list(map(int, input().split()))
    vetor_ordenado = bubble_sort(vetor)
    for item in vetor_ordenado:
        print(item)
    print()
    for item in vetor:
        print(item)

if __name__ == "__main__":
    main()