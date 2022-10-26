#import module regex 

import re 

#declarations var 
nb = int(input("rentrer un nombre entier : "))

    
fichier = open("/home/meyze/Bureau/python/data.txt","r")
x = fichier.read()


y = re.findall(r"[a-zA-Z]{1,}", x)

word = 0 
w = 0


while w < len(y):

    if nb == len(y[w]):
        word += 1

    w += 1
   
print(word)


