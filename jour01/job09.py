hauteur = int(input('Entrez la hauteur'))
largeur = hauteur * 2
left = hauteur
right = hauteur + 1


for x in range(1, hauteur + 1):
    line = ""    
    for y in range(1, largeur + 1):
        if y == left:
            line += "/"
        elif y == right:
            line += "\\"
        else:
            if x == hauteur:
                line += "_"
            else:
                line += " "
    print(line)
    right += 1
    left -= 1

