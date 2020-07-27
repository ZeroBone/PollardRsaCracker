"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from prime import nextPrime
from powmod import aPowbModn
from euklidian import gcd, next_divisor_of

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
        
        # print("Found factor in k: "+str(currentPrime)+" ^ "+str(currentExponent)+" = "+str(maximalePrimFaktor))
        
        k *= maximalePrimFaktor

        currentPrime = nextPrime(currentPrime)

    return k

def pollard(b, n):

    k = calculateK(b)

    # print("k = " + str(k))
    print("k has " + str(len(str(k))) + " digits")

    p = 1
    # a is an arbitraty element in the multiplicative group of divisors of 1 modulo n
    a = next_divisor_of(1, n)

    while p == 1 or p >= n:
        print("Trying to solve with a = " + str(a))

        aPowKModNminus1 = aPowbModn(a, k, n) - 1

        print("(a ^ k mod n) - 1 = " + str(aPowKModNminus1))

        p = gcd(aPowKModNminus1, n)

        a = next_divisor_of(a, n)

    return p