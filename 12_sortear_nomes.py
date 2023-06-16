import random

RIFA = []
while True:
    nome = input("Digite um nome: ")
    RIFA.append(nome)
    
    resp = input("Deseja continuar [S | N]?")
    if resp.upper() == "N":
        break
    
random.shuffle(RIFA) 
sorteado = random.choice(RIFA) 
print("O ganhador foi {}".format(sorteado))