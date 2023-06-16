t1 = int(input("Digite o 1º termo da PA: "))
qt = int(input("Digite a qtde de termos da PA: "))
r  = int(input("Digite a razão da PA: "))

# Inclusão do primeiro termo na lista PA
PA = [t1] 

# Como o primeiro termo já foi incluído, então o número de termos a serem gerados é a quantidade informada menos 1
for x in range(qt - 1):
    # Sabe-se que a(n) = a(n-1) + r

    # Pega o índice do último elemento da PA 
    ultimo_indice = len(PA) - 1
    
    # a(n) = a(n-1) + r
    prox = PA[ultimo_indice] + r

    # Inclui o novo termo na PA
    PA.append(prox)
    
print(PA)