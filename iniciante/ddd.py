ddds = [61, 71, 11, 21, 32, 19, 27, 31]
destinos = [
    'Brasilia', 
    'Salvador', 
    'Sao Paulo', 
    'Rio de Janeiro', 
    'Juiz de Fora', 
    'Campinas', 
    'Vitoria', 
    'Belo Horizonte'
]

ddd = int(input())
ddd_incorreto_msg = "DDD nao cadastrado"

if ddd not in ddds:
    print(ddd_incorreto_msg)
else:
    destino_pos = ddds.index(ddd)
    destino = destinos[destino_pos]
    print(destino)