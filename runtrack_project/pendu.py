import random

def game():
    arr = []
    charsNumber = int(input('Precisez le nombre des lettres'))
    count = 0

    with open("./files/dico_france.txt", 'r', encoding='iso-8859-1') as file:
        while True:
            line = file.readline()
            if not line:
                break
            if len(line) == charsNumber + 1:
                arr.append(line)
    file.close()

    word = arr[randomIndex(0, len(arr) - 1)].lower()    
    hiddenWord = word

    for i in range(len(hiddenWord) - 1):
        hiddenWord = hiddenWord.replace(word[i], '_')
    
    print(hiddenWord)
    wordArr = list(word)
    wordArr.remove('\n')
    hiddenWordArr = list(hiddenWord)
    hiddenWordArr.remove('\n')

    charsArr = []
    while True:
        if isEndVerify(hiddenWordArr):
            break

        char = input('Entrez une lettre')
        
        isUsed = False
        while isUsed != True:
            if charsArr.count(char) > 0:
                char = input('Vous avez deja utilisé cette lettre. Veuillez essayer une autre')
            else:
                charsArr.append(char)  
                isUsed = True
            
        for i in range(len(wordArr)):
            if wordArr[i] == char:                
                hiddenWordArr[i] = char

        count += 1                    
        print(hiddenWordArr)        

    print('Le mot cherché est: ' + "".join(hiddenWordArr))    
    print('Vous avez utilisé ' + str(count) + ' essais')    
            
def isEndVerify(array):
    isEnd = False
    for i in array:
        if i == '_':
            isEnd = False
            return isEnd
        else:
            isEnd = True
    return isEnd      

def randomIndex(start, stop):
    return random.randint(start, stop)





game()
    
