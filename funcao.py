pi = 3.14

def saudar():
    print('Olá')

def saudar_aluno(nome):
    print('Olá,', nome)

def calcular_dobro(num):
    return 2 * num

def calcular_dobro_triplo(num):
    return 2 * num, 3 * num

def calcular_area_circulo():
    raio = 3
    return pi * pow(raio, 2)

def calcular_comprimento_circulo():
    raio = 2
    return 2 * pi * raio

def retornar_menor_maior_media(notas):
    menor = min(notas)
    maior = max(notas)
    media = sum(notas) / len(notas)
    return menor, maior, media

def calcular_dobroX_triploY(x, y):
    '''Calculo
    dobro
    triplo
    '''
    return 2 * x, 3 * y

def calcular_imc(peso, altura, nome = 'Cliente'):
    "Essa função calcula o IMC, dado o peso e a altura"
    imc = peso / pow(altura, 2)
    return '{}, seu IMC é {:.2f}'.format(nome, imc)