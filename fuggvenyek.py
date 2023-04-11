def area(): #1. feladat, teglalap terulete
    a = int(input('a:'))
    b = int(input('b:'))
    T = a*b
    return T
print(f'T:{area()}')

def lnko(): #2. feladat
    c = int(input('c:'))
    d = int(input('d:'))
    while d:
        c,d = d,c%d
    return c
print(f'Lnko: {lnko()}')

def div(): #3. feladat
    counter = 0
    f = int(input('f:'))
    for i in range(1,f+1):
        if f % i == 0:
            counter += 1
    return counter
print(f'The number has {div()} divisors')

def prime(): #4. feladat
    n = int(input('n:'))
    if n % n == 1 and n % 1 == n:
        return 'Prime number'
    else:
        return 'Not prime number'
print(f'{prime()}')

#amit nem fejeztem be az lecke a szunetre!!!!

def valueCounter(): #5. feladat
    t = [1, 2, 3, 2, 4, 2, 5, 6, 7, 6]
    val = int(input('g:'))
    _counter = 0
    for item in t:
        if item == val:
            _counter += 1
    return _counter
print(f'Is in the list {valueCounter()} times') 

def valueSet(): # 6. feladat
    q = [1, 2, 3, 2, 4, 2, 5, 6, 7, 6]
    p = [3, 2, 3, 2, 4, 2, 5, 1, 7, 1]
    _set = int(input('h:'))
    _counter_ = 0
    for _item in q and p:
        if _item == _set:
            _counter_ += 1
    return _counter_
print(f'The number is in {valueSet()} times')

# ennyi ment :)