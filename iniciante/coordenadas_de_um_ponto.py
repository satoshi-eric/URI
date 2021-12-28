def get_coords():
    x, y = map(float, input().split())
    return x, y

def get_quadrant(x, y):
    if x == y == 0:
        return 'Origem'
    elif x == 0:
        return 'Eixo Y'
    elif y == 0:
        return 'Eixo X'
    elif x > 0 and y > 0:
        return 'Q1'
    elif x < 0 and y > 0:
        return 'Q2'
    elif x < 0 and y < 0:
        return 'Q3'
    elif x > 0 and y < 0:
        return 'Q4'

def main():
    x, y = get_coords()
    quadrant = get_quadrant(x, y)
    print(quadrant)

if __name__ == '__main__':
    main()