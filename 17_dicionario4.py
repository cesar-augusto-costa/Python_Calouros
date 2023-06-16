contatos = {
    '@camilaqueiroz': 'Camila Queiroz',
    '@paollaoliveira': 'Paolla Oliveira',
    '@sherronmenezzes': 'Sherron Menezes',
    '@bruna_ionica': 'Bruna Marquesine'
}

backup_contatos = contatos.copy()
print(backup_contatos)

contatos.pop('@paollaoliveira')
print(contatos)

contatos.popitem()
print(contatos)

contatos.clear()
print(contatos)


