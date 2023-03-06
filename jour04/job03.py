
str1 = str(bin(55))
str2 = str(bin(33))
print(str1, str2)
print(str1[-4], str2[-4])

def compare(i):    
    res = ''  
    if str1[i] == 'b' or str2[i] == 'b':        
        return res
    else:
        res += str(int(not str1[i] == str2[i]))
        return res + str(int(compare(str1[i - 1] == str2[i - 1])))

print(compare(-1))


