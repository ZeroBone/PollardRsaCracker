from prime import find_factor
from powmod import power_modulo
from euklidian import inverse_modulo
from pollard import pollard


def main():
    
    n = int(input("Enter n (as part of the public key): "))
    e = int(input("Enter e (as part of the public key): "))
    c = int(input("Enter c (the encrypted message to decrypt): "))
    b = int(input("Enter b (the maximum prime factor in n, optional): ") or 1)

    # Demo:
    # n = 186444745729857899758373984272541398503249351266417000699738642133172271283265124803102459
    # e = 65537
    # c = 159178142916077677757648147687519523540045276157456113470673097514775229976995968698190914
    # b = 200000

    if n < 2 or e < 2 or c < 0 or b > n or b <= 0:
        print("Invalid input")
        return
        
    p = None

    if b == 1:
        print("Factorizing n with the Bruteforce algorithm...")
        p = find_factor(n)
    else:
        print("Factorizing n with the Pollard algorithm...")
        if b > n - 1:
            b = n - 1
        p = pollard(b, n)

    print("p = %d" % p)

    q = n // p

    print("q = %d" % q)
    print("Factorizing complete.")

    phi = (p - 1) * (q - 1)

    print("phi(n) = %d" % phi)

    print("Solving e * d = 1 mod phi(n) with the euklidian algorithm...")

    d = inverse_modulo(e, phi)

    print("d (private key) = %d" % d)

    m = power_modulo(c, d, n)

    print("m (decrypted message) = %d" % m)


if __name__ == "__main__":
    main()
