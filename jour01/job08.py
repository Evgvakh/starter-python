largeur = int(input('Entrez la largeur'))
hauteur = int(input('Entrez la hauteur'))

for x in range(hauteur):
    line = ""
    for y in range(largeur):
        if y == 0 or y == largeur - 1:
            line += "|"      
        else:
            if x == 0 or x == hauteur - 1:
                line += "-"
            else:
                line += " "
    print(line)