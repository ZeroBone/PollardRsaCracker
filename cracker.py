"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

from prime import find_factor
from powmod import aPowbModn
from euklidian import inverse_modulo
from pollard import pollard

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

    p = None

    if b >= n or b < 1:
        print("Factorizing n with the BRUTEFORCE algorithm...")
        p = find_factor(n)
    else:
        print("Factorizing n with the Pollard algorithm...")
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