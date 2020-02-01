"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

# Class to represent extended euklidian algorithm result
class GCD_Result:
    def __init__(self, gcd, u, v):
        self.gcd = gcd
        # u and v are the linear combination coefficients
        self.u = u
        self.v = v
    def __str__(self):
        return str(self.gcd) + " = " + str(self.u) + " * a + " + str(self.v) + " * b"

def gcd(a, b):
    while True:
        if b == 0:
            return a
        a = a % b
        if a == 0:
            return b
        b = b % a

"""
def extended_gcd(a, b):
    if a == 0:
        return GCD_Result(b, 0, 1)

    result = extended_gcd(b % a, a)

    u = result.u
    result.u = result.v - (b // a) * result.u
    result.v = u

    return result
"""

def extended_gcd(a, b):
    if a == 0:
        return GCD_Result(b, 0, 1)

    unPrev = 1
    vnPrev = 0
    unCur = 0
    vnCur = 1

    while b != 0:
        bn = a // b
        newB = a % b
        a = b
        b = newB

        # Update coefficients
        unNew = unPrev - bn * unCur
        vnNew = vnPrev - bn * vnCur

        # Shift coefficients
        unPrev = unCur
        vnPrev = vnCur
        unCur = unNew
        vnCur = vnNew

    return GCD_Result(a, unPrev, vnPrev)