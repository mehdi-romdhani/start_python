
txt = str(input('saisir votre texte : '))
fichier = open("/home/meyze/Bureau/python/output.txt", "a")
fichier.write(txt)
fichier.close

fichier1 = open("/home/meyze/Bureau/python/output.txt", "r")
print(fichier1.read())






