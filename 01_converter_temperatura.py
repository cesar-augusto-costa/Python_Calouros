'''
Construa um programa que leia uma temperatura em Fahrenheit
e converta-a para Celsius.
Sabe-se que: ºC = (ºF - 32) / 1.8
'''

fahrenheit = float(input('Digite a temperatura em Fahrenheit: '))
celsius = (fahrenheit - 32) / 1.8
print('A temperatura é {:.2f} ºC'.format(celsius))
