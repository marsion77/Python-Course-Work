def reverse_string(n):
    return  n[::-1]



def vovel(a):
    count = 0
    myvovel = "aeiouAEIOU"

    for i in a:
        for ch in myvovel:
            if i == ch:
                count = count + 1
    return count
        

def palindrom(b):
    b = b.lower()
    if b == b[::-1]:
        return "The String is a Palindrom"
    else:
        return "The String is not a Palindrom"
