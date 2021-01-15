def power_modulo(a: int, b: int, n: int) -> int:
    """ Computes a ^ b mod n """
    result = 1
    
    # Loop through all the binary digits of the numbers
    while b != 0:

        if b % 2 == 1:
            # b odd
            result = (result * a) % n
            # result = (result * (a % n)) % n

        a = (a * a) % n
        # a = ((a % n) * (a % n)) % n

        b //= 2

    return result
