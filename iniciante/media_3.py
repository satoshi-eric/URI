def get_grades():
    grades = map(float, input().split())
    return grades

def get_mean(*grades: list):
    n1 = grades[0] * 2
    n2 = grades[1] * 3
    n3 = grades[2] * 4
    n4 = grades[3] * 1
    mean = (n1 + n2 + n3 + n4) / 10
    return mean

def print_result(mean: float):
    print(f'Media: {mean:.1f}')
    if mean >= 7:
        print('Aluno aprovado.')
    elif mean >= 5:
        print('Aluno em exame.')
        exame = float(input())
        print(f'Nota do exame: {exame:.1f}')
        media_final = (mean + exame) / 2
        if media_final >= 5:
            print('Aluno aprovado.')
        else:
            print('Aluno reprovado.')
        print(f'Media final: {media_final:.1f}')
    else:
        print('Aluno reprovado.')
        

def main():
    n1, n2, n3, n4 = get_grades()
    mean = get_mean(n1, n2, n3, n4)
    print_result(mean)

if __name__ == '__main__':
    main()