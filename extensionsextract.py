import re


test = ["fichier.txt","fichier2.txt", "fichier3.sh", "fichier4", "fichier5.java", "fichier6.txt", "fichier7.java"];
res =[];
for files in test :
    ans = re.findall("\.([^.]+)", files);
    res.append(ans);
    print("l'extension : ",ans," se repète : ", res.count(ans), "fois");
