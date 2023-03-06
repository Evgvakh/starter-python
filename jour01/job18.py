def func(*args):
    myList = []
    for x in args:
        myList.append(x)
    myList.sort()
    print(myList)

func(2, 32, 3, 34, 65, 15, 78, 52, 50, 52)