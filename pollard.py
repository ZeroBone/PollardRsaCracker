from prime import next_prime
from powmod import power_modulo
from euklidian import gcd, next_coprime


def compute_k(b: int) -> int:

    k = 1

    cur_prime = 2

    while cur_prime <= b:

        cur_expo = 1

        while cur_prime ** cur_expo <= b:
            k *= cur_prime
            cur_expo += 1

        cur_prime = next_prime(cur_prime)

    return k


def pollard(b: int, n: int) -> int:

    k = compute_k(b)

    print("k has %d digits" % len(str(k)))

    p = 1
    # a is an arbitraty element in the multiplicative group of divisors of 1 modulo n
    a = next_coprime(1, n)

    while p == 1 or p >= n:

        print("Trying to solve with a = %d" % a)

        a_pow_k_mod_n_minus1 = power_modulo(a, k, n) - 1

        print("(a ^ k mod n) - 1 = %d" % a_pow_k_mod_n_minus1)

        p = gcd(a_pow_k_mod_n_minus1, n)

        a = next_coprime(a, n)

    return p
