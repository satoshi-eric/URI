valores = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.10, 0.5, 0.1]
notas = [0, 0, 0, 0, 0, 0]
moedas = [0, 0, 0, 0, 0, 0]

entrada = float(input(''))

while entrada >= 100:
    notas[0] += 1
    entrada -= 100

while entrada >= 50:
    notas[1] += 1
    entrada -= 50

while entrada >= 20:
    notas[2] += 1
    entrada -= 20

while entrada >= 10:
    notas[3] += 1
    entrada -= 10

while entrada >= 5:
    notas[4] += 1
    entrada -= 5

while entrada >= 2:
    notas[5] += 1
    entrada -= 2

while entrada >= 1:
    moedas[0] += 1
    entrada -= 1

while entrada >= 0.5:
    moedas[1] += 1;
    entrada -= 0.5

while entrada >= 0.25:
    moedas[2] += 1
    entrada -= 0.25

while entrada >= 0.10:
    moedas[3] += 1
    entrada -= 0.1

while entrada >= 0.05:
    moedas[4] += 1
    entrada -= 0.05

while entrada >= 0.01:
    moedas[5] += 1
    entrada -= 0.01

print('NOTAS:')
print('{} nota(s) de R$100.00' .format(notas[0]))
print('{} nota(s) de R$50.00' .format(notas[1]))
print('{} nota(s) de R$20.00' .format(notas[2]))
print('{} nota(s) de R$10.00' .format(notas[3]))
print('{} nota(s) de R$5.00' .format(notas[4]))
print('{} nota(s) de R$2.00' .format(notas[5]))
print('MOEDAS:')
print('{} moeda(s) de R$1.00' .format(moedas[0]))
print('{} moeda(s) de R$0.50' .format(moedas[1]))
print('{} moeda(s) de R$0.25' .format(moedas[2]))
print('{} moeda(s) de R$0.10' .format(moedas[3]))
print('{} moeda(s) de R$0.05' .format(moedas[4]))
print('{} moeda(s) de R$0.01' .format(moedas[5]))