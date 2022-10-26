

#import du module re python 

import re



#method pour ouvrir & lire un fichier 

fichier = open("/home/meyze/Bureau/python/domains.xml", "r")

contenu = fichier.read()
#print(contenu)


x = re.findall('[a-zA-Z]{1,}\.[a-z]{1,6}', contenu)
print(x)
#print(x)
#print(fichier.read())



#nb de nomdedomaine
#------------------------------------------------------------

fichier = open("/home/meyze/Bureau/python/domains.xml", "r")
contenu = fichier.read()
print(contenu.count('name="domain"'))
fichier.close()






