"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from prime import nextPrime
from powmod import aPowbModn
from euklidian import gcd, inverse_modulo

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

    # a is an arbitraty element in the multiplicative group of divisors of 1 modulo n
    # as gcd(n-1, n) = 1 for all n, we can pick a = n - 1
    # or we can pick 2
    a = 2 # n - 1

    print("k has " + str(len(str(k))) + " digits")
    print("a = " + str(a))

    aPowKModNminus1 = aPowbModn(a, k, n) - 1

    print("(a ^ k mod n) - 1 = " + str(aPowKModNminus1))

    p = gcd(aPowKModNminus1, n)

    return p

if __name__ == "__main__":
    n = int(input("Enter n (as part of the public key): "))
    e = int(input("Enter e (as part of the public key): "))
    c = int(input("Enter c (the encrypted message to decrypt): "))
    b = int(input("Enter b (the maximum prime factor in n, optional): ") or n)

    # Demo:
    # n = 186444745729857899758373984272541398503249351266417000699738642133172271283265124803102459
    # e = 65537
    # c = 159178142916077677757648147687519523540045276157456113470673097514775229976995968698190914
    # b = 200000

    print("Factorizing n to find its prime divisors...")

    p = pollard(b, n)

    print("p = " + str(p))

    q = n // p

    print("q = " + str(q))
    print("Factorizing complete.")

    phi = (p - 1) * (q - 1)

    print("phi(n) = " + str(phi))

    print("Solving e * d = 1 mod phi(n) with the euklidian algorithm...")

    d = inverse_modulo(e, phi)

    print("d (private key) = " + str(d))

    m = aPowbModn(c, d, n)

    print("m (decrypted message) = " + str(m))