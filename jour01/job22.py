def myUpper(st):
    return st.upper()

def myLower(st):
    return st.lower()

def myTitle(st):
    first = st[0].upper()
    rest = st[1:]
    return first + rest

def myClean(st):
    arr = st.split()
    return ' '.join(arr)  
    

def makeAction():
    string = input('Entrez une phrase')
    func = input('Choisissez entre: \'upper\', \'lower\', \'title\' ou \'clean\'')
    if func == 'upper':
        print(myUpper(string))
    elif func == 'lower':
        print(myLower(string))
    elif func == 'title':
        print(myTitle(string))
    elif func == 'clean':
        print(myClean(string))

makeAction()



