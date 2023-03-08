
gameArr = ['-', '-', '-', '-', '-', '-', '-', '-', '-']
corr = {
    '1 1': 0,
    '1 2': 1,
    '1 3': 2,
    '2 1': 3,
    '2 2': 4,
    '2 3': 5,
    '3 1': 6,
    '3 2': 7,
    '3 3': 8,
}


def game():
    player1 = input('Saisir le nom du joueur 1: ')
    player1figure = 'Croix'
    player2 = input('Saisir le nom du joueur 2: ')
    player2figure = 'Ronds'

    print('Joueur 1: ' + player1figure + ': ' + player1  )
    print('Joueur 2: ' + player2 + '. ' + player2figure)  
        
    currentPlayer = ''
    
    for i in range(len(gameArr)):
        if i == 2 or i == 5:
            print(gameArr[i])
        else:
            print(gameArr[i], end=" ")

    while True:    
        isPlayer1 = currentPlayer == player2 or currentPlayer == ""
        currentPlayer = player1 if isPlayer1 else player2        
        
        turn = input(currentPlayer + ' joue: ')
        for key in corr:
            if turn not in corr:
                turn = input('Merci de saisir le nombre correct!')
            if key == turn:
                if gameArr[corr[key]] == 'X' or gameArr[corr[key]] == 'O':
                    turn = input('Cette case a déjà été utilisée!!!')
                else:
                    gameArr[corr[key]] = 'X' if currentPlayer == player1 else 'O'
        
        for i in range(len(gameArr)):
            if i == 2 or i == 5:
                print(gameArr[i])
            else:
                print(gameArr[i], end=" ")     

        if didSmbWin(gameArr):
            break   

    print(currentPlayer + ' wins!!!')
    writeInFile(currentPlayer)  
    
def didSmbWin(array):
    if (array[0] == array[1] == array[2] == 'X' or
        array[0] == array[1] == array[2]  == 'O'):
        return True
    elif (array[0] == array[3] == array[6] == 'X' or
        array[0] == array[3] == array[6]  == 'O'):
        return True
    elif (array[0] == array[4] == array[8] == 'X' or
        array[0] == array[4] == array[8]  == 'O'):
        return True
    elif (array[1] == array[4] == array[7] == 'X' or
        array[1] == array[4] == array[7]  == 'O'):
        return True
    elif (array[2] == array[5] == array[8] == 'X' or
        array[2] == array[5] == array[8]  == 'O'):
        return True
    elif (array[2] == array[4] == array[6] == 'X' or
        array[2] == array[4] == array[6]  == 'O'):
        return True
    elif (array[3] == array[4] == array[5] == 'X' or
        array[3] == array[4] == array[5]  == 'O'):
        return True
    elif (array[6] == array[7] == array[8] == 'X' or
        array[6] == array[7] == array[8]  == 'O'):
        return True

def writeFile(user):
    with open("./files/morpion.txt", 'r+') as file:
        lines = file.readlines()  

        def changeItem(item):
            dividedLine = item.split(" ")
            if dividedLine[0] == user:                
                victoriesNumber = int(dividedLine[1])                                
                victoriesNumber += 1                
                newline = dividedLine[0] + ' ' + str(victoriesNumber) + ' \n'
                return newline
            else:
                return item        
                               
        newLines = "".join(list(map(changeItem, lines))) 
        file.close()

    newFile = open("./files/morpion.txt", 'wt')
    newFile.write(newLines)
    newFile.close()

def writeInFile(user):
    with open("./files/morpion.txt", 'r+') as file:
        text = file.readlines()

        userExists = False
        for i in text:
            userName = i.split(" ")            
            if userName[0] == user:
                userExists = True
            
        if userExists:
            writeFile(user)
        else:
            file.write(user + ' 1 ' + '\n')


game()