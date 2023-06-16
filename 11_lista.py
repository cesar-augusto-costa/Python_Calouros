num_nadadores = 7
ATLETA = []
TEMPO  = []
for x in range(num_nadadores):
    nome = input("Digite o nome de um nadador: ")
    t    = float(input("Digite o seu tempo: "))
    ATLETA.append(nome)
    TEMPO.append(t)

print("")
for x in range(num_nadadores):
   print("{} nadou 25m em {} seg.".format(ATLETA[x], TEMPO[x]))

pior_tempo          = max(TEMPO)                  # Pior tempo é o MAIOR de todos
indice_pior_tempo   = TEMPO.index(pior_tempo)     # Índice em que está o pior tempo
pior_nadador        = ATLETA[indice_pior_tempo]   # Acessa o nadador cujo índice corresponde ao maior tempo

melhor_tempo        = min(TEMPO)                  # Melhor tempo é o MENOR de todos
indice_melhor_tempo = TEMPO.index(melhor_tempo)   # Índice em que está o menor tempo
melhor_nadador      = ATLETA[indice_melhor_tempo] # Acessa o nadador cujo índice corresponde ao menor tempo

media_tempo = sum(TEMPO) / len(TEMPO)             # Soma os tempos e divide pela quantidade

print("")
print("{} é o melhor nadador com {} seg.".format(melhor_nadador, melhor_tempo))
print("{} é o pior nadador com {} seg.".format(pior_nadador, pior_tempo))
print("A média dos tempos é {} seg.".format(media_tempo))