# PollardRsaCracker
This is my implementation of RSA cracking algorithm based on Pollard factorization. It will work if the numbers `p - 1` and `q - 1` that form `n = p * q` (as a part of the public key, `p` and `q` are prime), have no large maximum prime power factors. Of course, all modern RSA implementations don't have this security issue so this is more of an educational project.

# Usage
In order to start the script, simply run `python cracker.py`

You will need 4 inputs:
1. `n` - prime number in the public key so that `m = c ^ d mod n` where `m` is the message, `c` is the encrypted message, `d` is the private key.
2. `e` - the second public key component (so that `gcd(e, phi(n)) = 1`).
3. `c` - the encrypted message.
4. `b` - the maximum prime factor of `n`. This field is optional. However, if you leave it blank, the brute-force algorithm will be used for factorizing `n`.

# Demo
```
Enter n (as part of the public key): 186444745729857899758373984272541398503249351266417000699738642133172271283265124803102459
Enter e (as part of the public key): 65537
Enter c (the encrypted message to decrypt): 159178142916077677757648147687519523540045276157456113470673097514775229976995968698190914
Enter b (the maximum prime factor in n, optional): 200000
Factorizing n with the Pollard algorithm...
k has 86871 digits
Trying to solve with a = 2
(a ^ k mod n) - 1 = 95072790833932492612013226959843266212858324985456485206430737027466196168851937286400160
p = 2962244945158622279601750283735698362054297
q = 62940354083336669282335053470277744418281466547
Factorizing complete.
phi(n) = 186444745729857899758373984272541398503249288323100672417910737518517050721785008159581616
Solving e * d = 1 mod phi(n) with the euklidian algorithm...
d (private key) = 144519783985790947216463957780263103956010556583510294319695217448779562333745493606767873
m (decrypted message) = 2020
```

# Demo with small numbers
## Brute-force
```
Enter n (as part of the public key): 493
Enter e (as part of the public key): 45
Enter c (the encrypted message to decrypt): 56
Enter b (the maximum prime factor in n, optional):
Factorizing n with the Bruteforce algorithm...
p = 17
q = 29
Factorizing complete.
phi(n) = 448
Solving e * d = 1 mod phi(n) with the euklidian algorithm...
d (private key) = 229
m (decrypted message) = 490
```
## Pollard
```
Enter n (as part of the public key): 493
Enter e (as part of the public key): 45
Enter c (the encrypted message to decrypt): 56
Enter b (the maximum prime factor in n, optional): 493
Factorizing n with the Pollard algorithm...
k has 216 digits
Trying to solve with a = 2
(a ^ k mod n) - 1 = 0
Trying to solve with a = 3
(a ^ k mod n) - 1 = 0
Trying to solve with a = 4
(a ^ k mod n) - 1 = 0

...

Trying to solve with a = 509
(a ^ k mod n) - 1 = 0
Trying to solve with a = 510
(a ^ k mod n) - 1 = 203
p = 29
q = 17
Factorizing complete.
phi(n) = 448
Solving e * d = 1 mod phi(n) with the euklidian algorithm...
d (private key) = 229
m (decrypted message) = 490
```

# Credits
* [This awesome lecture where I learnt about RSA](https://www.mathematik.uni-kl.de/~boehm/lehre/1920_MfI/)
* Mirko Höhn for helping me understand the mathematics behind RSA.

# License
Copyright (c) 2020 Alexander Mayorov.

This project is licenced under the MIT Licence.

Please leave a copyright notice if you use/modify this software or parts of it.

For more information see the LICENCE file.
