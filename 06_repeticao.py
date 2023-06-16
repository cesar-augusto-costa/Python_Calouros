qtd_num_pares = 0
for x in range(5):
    num = int(input(f'Informe o {x+1}º número inteiro: '))
    if num % 2 == 0:
        qtd_num_pares += 1
print('A Quantidade de números pares foi {}'.format(qtd_num_pares))
