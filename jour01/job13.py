length = int(input('Entrez le nombre entier'))
counter = 0

with open("./files/data.txt", 'r') as content:
    while True:        
        line = content.readline()
        arr = line.split()
        if not line:
            break
        for word in arr:
            if len(word) == length:
                counter += 1
        
    print(counter)    
    