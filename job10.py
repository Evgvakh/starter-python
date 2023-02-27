content = input('Entrez le text')

with open("./files/output.txt", "w") as w:
    w.write(content)

with open("./files/output.txt", "r") as r:
    contenu = r.read()
    print(contenu)
