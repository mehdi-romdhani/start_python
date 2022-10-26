#import du module re 

import re 

#variables & methode pour ouvrir & lire le fichier.txt sur terminal

fichier = open("/home/meyze/Bureau/python/data.txt", "r")
contenu = fichier.read()
#print(contenu)

#regex 

x = len(re.findall(r"[a-zA-Z]{1,}", contenu))

print(x)









