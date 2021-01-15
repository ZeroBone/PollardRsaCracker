def is_prime(n: int) -> bool:
    if n <= 1:
        return 0
    if n <= 3:
        return True
    
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i = i + 6
    
    return True
  

def next_prime(n: int) -> int:
    if n <= 1:
        return 2

    if n % 2 == 0:
        n = n + 1
        if is_prime(n):
            return n
  
    while True:
        n += 2
        if is_prime(n):
            return n


def find_factor(n: int) -> int:
    p = 2

    while n % p != 0:
        p = next_prime(p)

    return p
