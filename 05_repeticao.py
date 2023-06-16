qtd_notas = int(input('Quantidades de Notas? '))
soma_notas = 0
for x in range(qtd_notas):
    nota = float(input('{}ª Nota: '.format(x+1)))
    soma_notas += nota
media = soma_notas / qtd_notas
print('A média é {:.2f}'.format(media))
