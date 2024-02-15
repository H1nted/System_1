import os
import sys


extensions = {}
def parcours (rep) :
    print(rep);
    maListe = os.listdir(rep) ;
    print(maListe, "\n") ;
    for fichier in maListe :
        if os.path.isdir(rep + "/"+fichier):
            parcours(rep + "/"+fichier);
        else :
            ext = fichier.split(".");
            if len(ext) > 1 :
                ext = fichier.split(".")[-1];
                if ext not in extensions :              
                    extensions[ext] = 1 ;
                else :
                    extensions[ext] += 1 ;
            else : 
                ext = "pas d'extension";
                if ext not in extensions :
                    extensions[ext] = 1 ;
                else :
                    extensions[ext] += 1 ;

parcours(sys.argv[1]);
for (clef, valeur) in extensions.items():
    print(clef, ":", valeur);
    
print("Total : ",sum(extensions.values()))