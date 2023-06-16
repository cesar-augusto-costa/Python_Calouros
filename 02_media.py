'''
Escreva um programa que leia 3 números inteiros,
calcule e escreva a média aritmética entre eles.
'''

nota1 = float(input('Digite a 1ª nota: '))
nota2 = float(input('Digite a 2ª nota: '))
nota3 = float(input('Digite a 3ª nota: '))

media = (nota1 + nota2 + nota3) / 3
print('A média é {:.2f}'.format(media))
