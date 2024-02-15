
import math as m
import numpy as np


import time
start_time = time.time()



n = int(input('Donnez les n premiers nombres n : '))

listePrem=[]

def estpremier (n) :
    for i in range (2,round(m.sqrt(n)+1)) :
        if n % i == 0 :
            return False
    return True


for i in range(2,n+1) :
    if estpremier(i) == True :
        listePrem.append(i)

# listePrem=[2]

# for candidat in range(2,n+1) :
#     primalite = True
#     for i in listePrem :
#         if candidat % i  == 0 :
#             primalite = False
#     if primalite == True :
#         listePrem.append(candidat)


print("Process finished --- %s seconds ---" % (time.time() - start_time))

print("Nombre des nombres premiers : ", len(listePrem))
# print('La liste des 100 premiers nombres premiers est : ',listePrem)

