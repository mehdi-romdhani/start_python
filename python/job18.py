#déclaration d'une fonction en python 

def myList(*nb):
    
        list=[*nb]
        list.sort()
        print(list)



myList(7,5,98,12,1)


