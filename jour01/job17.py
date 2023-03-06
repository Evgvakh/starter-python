def func(*args):
    myList = []
    for x in args:
        myList.append(x)
    for num in myList:
        if num % 2 == 0:
            print(num)

func(1, 3, 5, 7, 8, 9, 12, 18, 21, 24, 31, 34)