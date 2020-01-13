entrada = int(input(''))
dias = 0
meses = 0
anos = 0

while True:
    if entrada >= 365:
        anos += 1
        entrada -= 365
    else:
        break

while True:
    if entrada >= 30:
        meses += 1
        entrada -= 30
    else:
        break

while True:
    if entrada < 30 and entrada != 0:
        dias += 1
        entrada -= 1
    else:
        break

print('{} ano(s)\n{} mes(es)\n{} dia(s)' .format(anos, meses, dias))
