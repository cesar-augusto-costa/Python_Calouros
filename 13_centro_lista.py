N = int(input("Digite um número ímpar maior do que 1: "))
if (N % 2 == 0):
    print("{} é par. Programa será encerrado.".format(N))
elif N < 0:
    print('Número menor do que 1. Programa será encerrado.')
else:
    valores = []
    num_validos = 0
    while num_validos < N:
        num = int(input(f"Digite o {num_validos+1}º número inteiro positivo: "))
        if num > 0:
            valores.append(num)
            num_validos += 1
        
    indice_centro = int(N/2)              # Desconsidera a parte decimal da divisão
    numero_centro = valores[indice_centro]      # Acessa o elemento do centro da lista
    fat = 1                               # 1 é o valor que não altera o produto
    for x in range(1, numero_centro + 1):
        fat = fat * x
    print("Numero do centro da lista é {}.\nPortanto {}! = {}.".format(numero_centro, numero_centro, fat))