rapazes_maiores = 0
qtd_mocas = 0
somatoria_idades_mocas = 0
media_idade_mocas = 0
while True:
    sexo = input('sexo [M|F]: ')
    idade = int(input('idade: '))
    if(sexo.upper() == 'M'):
        if idade > 18:
            rapazes_maiores += 1
    elif(sexo.upper() == 'F'):
        qtd_mocas += 1
        somatoria_idades_mocas += idade
    else:
        print('sexo inválido.')
    condicao = input('Tem mais pessoas [S|N]: ')
    if condicao.upper() == 'N':
        break
if qtd_mocas > 0:
    media_idade_mocas = somatoria_idades_mocas / qtd_mocas

print('A quantidade de rapazes maiores de idade é {}'.format(rapazes_maiores))
print('A média de idades das moças é {:.0f}'.format(media_idade_mocas))
