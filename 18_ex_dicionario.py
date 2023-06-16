produtos = {}
while True:
    cod = int(input('Cod: '))
    nome = input('Nome: ')
    preco = float(input('Preço: R$ '))
    qtd = int(input('Quantidade: '))
    
    valores = []
    valores.append(nome)
    valores.append(preco)
    valores.append(qtd)

    produtos.update({cod:valores})

    resp = input('Deseja continuar? [S|N]: ')
    if resp.upper() == 'N':
        break

total = 0
for valor in sorted(produtos.values()):
    subtotal = valor[1] * valor[2]
    print(f'Produto: {valor[0]} R$ {valor[1]:.2f}, Qtd:, {valor[2]}, Subtotal:, {subtotal:.2f}')
    total += subtotal

print(10*'-*-')
print('Total: R$ {:.2f}'.format(total))
