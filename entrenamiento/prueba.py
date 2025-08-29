import random

vector = []

for i in range(0,1001):
    numero = random.randint(0,1001)
    vector.append(numero)


n = len(vector)

for i in range(n-1):
    for j in range(i+1,n):
        if vector[i] > vector[j]:
           vector[i], vector[j] = vector[j],vector[i] 


print(vector)