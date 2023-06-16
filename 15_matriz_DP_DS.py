from random import randint

while True:
    try:
        ordem = int(input('Informe a ordem da matriz: '))
    except:
        print('Digite um número inteiro: ')
        continue
    if ordem < 2:
        print(' - Digite um número maior que 1.')
    else:
        break
    
matriz = []
for i in range(ordem):
    linha = []
    for j in range(ordem):
        num = randint(1, 10)
        linha.append(num)
    matriz.append(linha)

DP = []
DS = []
for i in range(ordem):
    for j in range(ordem):
        print(matriz[i][j], end=' ')
        if i == j:
            DP.append(matriz[i][j])
        if i + j == ordem -1:
            DS.append(matriz[i][j])
    print()

maior_DP = max(DP)
menor_DS = min(DS)
media = (maior_DP + menor_DS)/2

print('A média entre DP+ com DS- é', media)


