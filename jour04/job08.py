n = int(input('Selectionnez le largeur du champ(nombre des cases)'))
# testarr = [['x' for i in range (n)] for j in range(n)] 
# for item in testarr:
#     print(' '.join(item))
cells = n

def game(num):    
    arr = [['x' for i in range(n)] for j in range(n)]       
    row = 0
    isFirst = True    
    while row < n:        
        if 'D' not in arr[row]:
            if 'x' in arr[row]:                              
                if isFirst:
                    damei = num - 1
                    isFirst = False
                else:
                    damei = arr[row].index('x')                           
                for i in range(n):
                    arr[row][i] = 'o'
                arr[row][damei] = 'D'    

                newRow = row + 1                
                offset = 1
                
                for i in range(newRow, n):                
                    arr[i][damei] = 'o'
                    if damei+offset in range(len(arr[i])):
                        arr[i][damei+offset] = 'o'                    
                    if damei-offset in range(len(arr[i])):
                        arr[i][damei-offset] = 'o'
                    offset += 1                
                row += 1                
            else:
                row += 1
        else:
            row += 1  
            
    dameCount = 0 
            
    for i in arr:
        if 'D' in i:
            dameCount += 1
    if dameCount < n:
        game(num - 1)
    else:
        for item in arr:
            print(' '.join(item)) 
    
        
game(cells - 1)

        



