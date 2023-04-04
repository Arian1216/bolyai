import math
e = [name for name in dir(math)]
print('\t'.join(e))

def ter(): #1. feladat, teglalap terulete
    a = int(input('a:'))
    b = int(input('b:'))
    T = a*b
    return T
print(f'T:{ter()}')

def prim(): #4. feladat
    n = int(input('n:'))
    if n % n == 1 and n % 1 == n:
        return 'Prime number'
    else:
        return 'Not prime number'
print(f'{prim()}')

#amit nem fejeztem be az lecke a szunetre!!!!

def lnko(): #2. feladat
    c = int(input('c:'))
    d = int(input('d:'))
    while d:
        c,d = d,c%d
    return c
print(f'Lnko: {lnko()}')

def oszto():
    counter = 0
    f = int(input('f:'))
    for i in range(1,f+1):
        if f % i == 1:
            counter += 1
    return counter
print(f'The number has {oszto()} divisors')