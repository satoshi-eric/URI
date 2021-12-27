# Link for the problem: https://www.beecrowd.com.br/judge/pt/problems/view/1037

def calculate_interval(value: float, interval: list) -> int:
    """Calculates the interval."""
    interval_str = ""
    if value < interval[0] or value > interval[-1]:
        interval_str = "Fora de intervalo"
    if interval[0] <= value <= interval[1]:
         interval_str = f"Intervalo [{interval[0]},{interval[1]}]"
    for i in range(1, len(interval) - 1):
        if interval[i] < value <= interval[i+1]:
            interval_str = f"Intervalo ({interval[i]},{interval[i+1]}]"

    return interval_str

def main():
    try:
        value = float(input())
        intervals = [0, 25, 50, 75, 100]
        print(calculate_interval(value, intervals))
    except ValueError:
        print('ValueError: Please, enter a valid number.')

if __name__ == "__main__":
    main()