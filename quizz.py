import random as r
import os
import sys

pays =[]
capitales =[]


NoQ = int(input("Donnez le nombre de questions souhaités : "));
while NoQ < 1 or NoQ > 100 :
    NoQ = int(input("Donnez le nombre de questions souhaités : "));

ToQ = int(input("Donnez le type des questions (Capitales = 1) (Pays = 2) : "));
while ToQ not in (1,2) :
    ToQ = int(input("Donnez le type des questions (Capitales = 1) / (Pays = 2) : "));

with open(file="capitales.csv", mode="r", encoding="utf-8") as file :
    for line in file :
        cap = line.split(",")[-1]
        capitales.append(cap.replace("\n",""))

        pay = line.split("(l")[0]
        pays.append(pay.replace(" ",""))

#  print(pays)
# print(pays.index('Tunisie '))
already= [];
score = 0;
if ToQ == 1 :
    for i in range(NoQ) :
        indice =r.randint(0,len(pays))
        while indice in already :
            indice = r.randint(0,len(pays))
        print("\nQuelle est la capitale du",pays[indice])
        rep = str(input("réponse : "));
        if rep == capitales[indice] :
            print("--bonne réponse");
            score += 1 ;
        else :
            print("--mauvaise réponse, la bonne réponse est : ",capitales[indice]);
        already.append(indice)

elif ToQ == 2 :
    for i in range(NoQ) :
        indice =r.randint(0,len(capitales))
        while indice in already :
            indice = r.randint(0,len(capitales))
        print("\nQuel est le pays du",capitales[indice])
        rep = str(input("réponse : "));
        if rep == pays[indice] :
            print("--bonne réponse");
            score += 1 ;
        else :
            print("--mauvaise réponse, la bonne réponse est : ",pays[indice]);
        already.append(indice)


print()
print()

print ("Score final : ",score, " / ",NoQ);
print ("Pourcentage : ",(score/NoQ)*100,"%")


