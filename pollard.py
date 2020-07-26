"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from prime import nextPrime
from powmod import aPowbModn
from euklidian import gcd

def calculateK(b):

    k = 1

    currentPrime = 2

    while currentPrime < b:

        currentExponent = 1

        maximalePrimFaktor = currentPrime

        while True:
            currentPrimFaktor = currentPrime ** (currentExponent + 1)
            if currentPrimFaktor > b:
                break
            maximalePrimFaktor = currentPrimFaktor
            currentExponent += 1
        
        print("Found factor in k: "+str(currentPrime)+" ^ "+str(currentExponent)+" = "+str(maximalePrimFaktor))
        
        k *= maximalePrimFaktor

        currentPrime = nextPrime(currentPrime)

    return k

def pollard(b, n):

    k = calculateK(b)

    factor = 1
    
    while n % 2 == 0:
        factor = factor * 2
        n = n // 2

    # a is an arbitraty element in the multiplicative group of divisors of 1 modulo n
    # as gcd(n-1, n) = 1 for all n, we can pick a = n - 1
    # or we can pick 2 if n is odd
    a = 2 # n - 1

    # print("k = " + str(k))
    print("k has " + str(len(str(k))) + " digits")
    print("a = " + str(a))

    aPowKModNminus1 = aPowbModn(a, k, n) - 1

    print("(a ^ k mod n) - 1 = " + str(aPowKModNminus1))

    p = gcd(aPowKModNminus1, n)

    return factor * p