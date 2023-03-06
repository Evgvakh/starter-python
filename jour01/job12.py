import re
n = 0
counter = 0
with open("./files/data.txt", 'r') as file:
# with open("./files/11.txt", 'r') as file:     
    while True:
        line = file.readline()
        if not line:
            break
        arr = line.split(" ")
        counter += len(arr)        
    print(counter)    

    