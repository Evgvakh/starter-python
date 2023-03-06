def func(*args):
    myList = []

    for x in args:
        myList.append(x)

    for i in range(len(myList)):
        for k in range(len(myList)):
            if myList[i] < myList[k]:
                temp = myList[i]
                myList[i] = myList[k]
                myList[k] = temp
                
    print(myList)

func(2, 32, 3, 34, 65, 15, 78, 52, 50, 52)