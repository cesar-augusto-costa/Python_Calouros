from random import randint

while True:
    li = int(input('Quantidade de linhas: '))
    col = int(input('Quantidade de colunas: '))
    if li <= 0 or col <= 0:
        print(' - Digite números maiores que 0.')
    else:
        break
matriz = []
for i in range(li):
    linha = []
    for j in range(col):
        num = randint(1, 10)
        linha.append(num)
    matriz.append(linha)

print(matriz, end='\n\n')

for i in range(li):
    for j in range(col):
        print(matriz[i][j], end=' ')
    print()