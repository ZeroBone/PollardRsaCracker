def gcd(a: int, b: int) -> int:
    while True:
        if b == 0:
            return a
        a = a % b
        if a == 0:
            return b
        b = b % a


def extended_gcd(a: int, b: int) -> (int, int, int):
    if a == 0: # Optional check
        return b, 0, 1

    if b == 0: # Without this check the first iteration will divide by zero
        return a, 1, 0

    un_prev = 1
    vn_prev = 0
    un_cur = 0
    vn_cur = 1

    while True:
        qn = a // b
        new_r = a % b
        a = b
        b = new_r

        if b == 0:
            return a, un_cur, vn_cur

        # Update coefficients
        un_new = un_prev - qn * un_cur
        vn_new = vn_prev - qn * vn_cur

        # Shift coefficients
        un_prev = un_cur
        vn_prev = vn_cur
        un_cur = un_new
        vn_cur = vn_new


def inverse_modulo(a: int, n: int) -> int:

    _, b, _ = extended_gcd(a, n)

    return b % n


def next_coprime(d: int, n: int) -> int:

    d = d + 1

    while d < n and gcd(d, n) != 1:
        d = d + 1

    return d
