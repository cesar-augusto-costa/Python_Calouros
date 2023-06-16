A = [[1, 2, 3],
     [4, 5, 6],
     [0, 0, 0]]

for i in range(2):     # percorre a 1a e a 2a linhas da matriz
    for j in range(3): # percorre todas as linhas da matriz
        A[2][j] = A[2][j] + A[i][j]
#a terceira linha da matriz corresponde à soma das outras duas.        
print(A)