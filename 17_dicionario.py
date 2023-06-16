contatos = {
    '@camilaqueiroz': 'Camila Queiroz',
    '@paollaoliveira': 'Paola Oliveira',
    '@sherronmenezzes': 'Sherron Menezes'
}
print(contatos)
print(contatos['@camilaqueiroz'])
print(contatos.get('@paollaoliveira'))

contatos.update({'@paollaoliveira': 'Paolla Oliveira'})
contatos.update({'@bruna_ionica': 'Bruna Marquesine'})
print('Quantidade:',len(contatos))
print(contatos)


insta = input('Digite um insta: ')

if insta in contatos:
    print('Esse insta é de', contatos.get(insta))
else:
    print('Não tem cadastrado.')