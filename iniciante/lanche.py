# Link for the problem: https://www.beecrowd.com.br/judge/pt/problems/view/1038

"""
Código  |  Expecificação  |  Preço
1       | Cachorro-quente | R$ 4,00
2       | X-Salada        | R$ 4,50
3       | X-Bacon         | R$ 5,00
4       | Torrada simples | R$ 2,00
5       | Refrigerante    | R$ 1,50
"""

def main():
    items = {
        1: {'name': 'Cachorro-quente', 'price': 4.00},
        2: {'name': 'X-Salada', 'price': 4.50},
        3: {'name': 'X-Bacon', 'price': 5.00},
        4: {'name': 'Torrada simples', 'price': 2.00},
        5: {'name': 'Refrigerante', 'price': 1.50}
    }
    item, qtd = map(int, input().split())
    total = items[item]['price'] * qtd
    print(f'Total: R$ {total:.2f}')

if __name__ == "__main__":
    main()