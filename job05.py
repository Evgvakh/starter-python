valeur_1 = int(input("Entrez le nombre"))
valeur_2 = int(input("Entrez encore le nombre"))

if valeur_1 < valeur_2:
    for x in range(valeur_1 + 1, valeur_2):
        print(x)

elif valeur_1 > valeur_2:
    for x in range(valeur_1-1, valeur_2, -1):
        print(x)

else:
    print("Valeurs égales")