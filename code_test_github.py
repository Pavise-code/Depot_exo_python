def narcissique(entrer):
    #entrer = input("entrer un nombre: ")
    value = str(entrer)
    somme = 0
    for i in value:
        valeur = int(i)
        carre = len(value)
        somme += valeur**carre
    print(somme)
    if somme == int(value):
        return True
    else:
        return False
booll = narcissique(153)
print(booll)