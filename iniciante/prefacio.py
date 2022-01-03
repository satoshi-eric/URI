def divisao_euclidiana(num1: int, num2: int):
    if (num1 < 0 and num2 > 0):
        q = -(abs(num1) // num2 + 1)
        r = num1 - num2 * q
        return q, r
    elif (num1 > 0 and num2 < 0):
        return -(num1 // abs(num2)), num1 % abs(num2)
    elif num1 > 0 and num2 > 0:
        return num1 // num2, num1 % num2
    elif num1 < 0 and num2 < 0:
        return abs(num1 // abs(num2)), num1 % abs(num2)
    elif num1 == 0:
        return 0, 0

def main():
    num1, num2 = map(int, input().split())
    divisao, resto = divisao_euclidiana(num1, num2)
    print(f"{divisao} {resto}")

if __name__ == "__main__":
    main()