# Link for problem: https://www.beecrowd.com.br/judge/pt/problems/view/1018

def print_cedules(notes: list, coins: list, notes_values: list, coins_values: list) -> None:
    """Prints the cedules and coins."""
    text = ''
    text += 'NOTAS:\n'
    for note, note_value in zip(notes, notes_values):
        text += f'{note} nota(s) de R$ {note_value:.2f}\n'
    text += 'MOEDAS:\n'
    for coin, coin_value in zip(coins, coins_values):
        text += f'{coin} moeda(s) de R$ {coin_value:.2f}\n'
        
    print(text, end='')

def calculate_change(amount: int, notes_values: list, coins_values: list) -> list:
    """Calculates the cedules and coins with a given amount."""
    notes = []
    coins = []
    
    for note_value in notes_values:
        exchange = amount / note_value
        amount = round(amount % note_value, 2)
        notes.append(int(exchange))

    for coin_value in coins_values:
        exchange = amount / coin_value
        amount = round(amount % coin_value, 2)
        coins.append(int(exchange))

    return notes, coins

def main():
    try:
        value = float(input())
        notes_values = [100, 50, 20, 10, 5, 2]
        coins_values = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
        notes, coins = calculate_change(value, notes_values, coins_values)
        print_cedules(notes, coins, notes_values, coins_values)
    except ValueError:
        print('ValueError: Please, enter a valid number.')

if __name__ == "__main__":
    main()