def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def isPrime(n):
    fc = 0
    for i in range(1,n+1):
        if n%i == 0:
            fc = fc + 1
    if fc == 2:
        return True
    else:
        return False