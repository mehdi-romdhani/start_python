hauteur = int(input("Entrez une hauteur : "))

cote_droite = "/"
cote_gauche = "\ "
base = "_"
espace =" "
tiret = "-"

i=1

while i <= hauteur:
    if i == 1:
        print(espace*(hauteur-i)+cote_droite+espace*((i-1)*2)+cote_gauche)
        i +=1

    elif i == hauteur :
        print(espace*(hauteur-i)+cote_droite+base*((i-1)*2)+cote_gauche) 
        i +=1
    else:
        print(espace*(hauteur-i)+cote_droite+espace*((i-1)*2)+cote_gauche) 
        i +=1
   

        
