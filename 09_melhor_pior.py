lista_nadadores = ['Ana', 'Bruna', 'Carol']
tempo = [15, 8, 10]
indice_pior_tempo = tempo.index(max(tempo))
indice_melhor_tempo = tempo.index(min(tempo))
print('A melhor nadadora é {}'.format(lista_nadadores[indice_melhor_tempo]))
print('A pior nadadora é {}'.format(lista_nadadores[indice_pior_tempo]))
