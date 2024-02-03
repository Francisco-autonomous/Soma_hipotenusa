def é_hipotenusa(n):
    i = 1
    j = 1
    s = 0
    while i < n:
        while s != n ** 2 and s < n ** 2:
            s = i ** 2 + j ** 2
            j += 1
        if s == n ** 2:
            return True
            
        i += 1
        j = 1
        s = 0
    return False

def soma_hipotenusas(k):
    h = 0
    n = 1
    while n <= k:
        if é_hipotenusa(n) == True:
            h = h + n
        n += 1
            
    return h

k = int(input())
soma_hipotenusas(k)