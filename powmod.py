"""
    Copyright (c) 2020 Alexander Mayorov
    This project is licenced under the MIT Licence.
    Please leave a copyright notice if you use/modify this software or parts of it.
    For more information see the LICENCE file.
"""

def aPowbModn(a, b, n):
    result = 1
    
    # Loop through all the binary digits of the numbers
    while b != 0:

        if b % 2 == 1:
            # b odd
            result = (result * a) % n

        a = (a * a) % n

        b //= 2

    return result