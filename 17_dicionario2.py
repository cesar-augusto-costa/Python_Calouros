contatos = {
    '@camilaqueiroz': 'Camila Queiroz',
    '@paollaoliveira': 'Paolla Oliveira',
    '@sherronmenezzes': 'Sherron Menezes',
    '@bruna_ionica': 'Bruna Marquesine'
}

for insta in contatos.keys():
    print(insta)

for atriz in contatos.values():
    print(atriz)

for insta, atriz in sorted(contatos.items()):
    print('O instagran de {} é {}'.format(atriz, insta))