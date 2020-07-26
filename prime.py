"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

def isPrime(n):
    if n <= 1:
        return 0
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    
    return True
  
def nextPrime(n):
    if n <= 1:
        return 2

    if n % 2 == 0:
        n = n + 1
        if isPrime(n):
            return n
  
    while True:
        n += 2
        if isPrime(n):
            return n

def find_factor(n):
    p = 2

    while n % p != 0:
        p = nextPrime(p)

    return p