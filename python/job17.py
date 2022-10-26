#declaration d'une fonction

def nombre(*nb):
   for i in nb:

      if i %2 == 0: 
        print(i)

nombre(2,90,3,5)      
