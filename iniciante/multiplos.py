def sao_multiplos(num1, num2):
    return num1 % num2 == 0 or num2 % num1 == 0

def main():
    nums = list(map(int, input().split()))
    print("Sao Multiplos") if sao_multiplos(*nums) else print("Nao sao Multiplos")

if __name__ == "__main__":
    main()