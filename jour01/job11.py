counter = 0
with open("./files/domains.xml", 'r') as file:    
    while True:
        line = file.readline()
        if not line:
            break
        if "name=\"domain\"" in line:
            counter += 1
    print(counter)    

    