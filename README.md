# PollardRsaCracker
This is my implementation of RSA cracking algorithm based on Pollard factorization. It will work if the prime number `n` as part of the public key has not a very big maximum prime factor. Of course, all modern RSA implementations don't have this security hole so this is more of an educational project that doesn't have much real-world applications.

# Usage
In order to start the script, simply run `python pollard.py`

You will need 4 inputs:
1. `b` - the maximum prime factor of `n`.
2. `n` - prime number in the public key so that `m = c ^ d mod n` where `m` is the message, `c` is the encrypted message, `d` is the private key.
3. `c` - the encrypted message.
4. `e` - the second public key component (so that `gcd(e, phi(n)) = 1`).

# Demo
```
Enter b (the maximum prime number factor): 200000
Enter n (as part of the public key): 186444745729857899758373984272541398503249351266417000699738642133172271283265124803102459
Enter c (the encrypted message to decrypt): 159178142916077677757648147687519523540045276157456113470673097514775229976995968698190914
Enter e (as part of the public key): 65537
Factorizing n to find ist prime divisors...
(a ^ k mod n) - 1 = 95072790833932492612013226959843266212858324985456485206430737027466196168851937286400160
p = 2962244945158622279601750283735698362054297
q = 62940354083336669282335053470277744418281466547
Factorizing complete.
phi(n) = 186444745729857899758373984272541398503249288323100672417910737518517050721785008159581616
Solving e * d = 1 mod phi(n) with the euklidian algorithm...
a = -41924961744066952541910026492278294547238731739590378098215520069737488388039514552813743
b = 14737
d (private key) = 144519783985790947216463957780263103956010556583510294319695217448779562333745493606767873
m (decrypted message) = 2020
```

# Credits
* Mirko Hoehn for helping me with the mathematics behind RSA.

# License
Copyright (c) 2020 Alexander Mayorov.

This project is licenced under the MIT Licence.

Please leave a copyright notice if you use/modify this software or parts of it.

For more information see the LICENCE file.
