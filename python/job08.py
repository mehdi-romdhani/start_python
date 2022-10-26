#declarations variables

larg = int(input("valeur larg : "))
haut = int(input("valeur haut : "))

tiret = "-"
es =" "


#multipl
larg_tiret = larg*tiret
haut_pipe = es*larg

i=0



while i <= haut:
    
    print("|"+larg_tiret+"|")
    i +=1
    for i in haut_pipe:

      print("|"+haut_pipe+"|")
    
    print("|"+larg_tiret+"|")

    break


       
    
    
    
    
   




