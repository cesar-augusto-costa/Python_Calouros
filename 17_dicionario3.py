from operator import itemgetter

contatos = {
    '@camilaqueiroz': 1.77,
    '@paollaoliveira': 1.70,
    '@sherronmenezzes': 1.67,
    '@bruna_ionica': 1.70
}

for insta, alt in sorted(contatos.items(),key=itemgetter(1)):
    print('{} tem {:.2f}m'.format(insta, alt))

print()

for insta, alt in sorted(contatos.items(),key=itemgetter(1), reverse=True):
    print('{} tem {:.2f}m'.format(insta, alt))