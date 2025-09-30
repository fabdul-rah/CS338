# Feraidon AbdulRahimzai
## CS338 - BEING EVE
### September 29, 2025


_______
Alice and Bob
______

Alice and Bob agree on

g = 5
p = 103

Alice sent Bob the number 10 : A
Bob sent Alice the number 71 : B

In order to get 10 for Alice, she used something like so; 

A = g^a (mod p)

We need to set up this equation in a way to get the (a).

10 = 5^a (mod 103)

How do we find the value of (a) here? Well, by brute forcing through it. Plug in numbers for a until we get the 10. So, (5 ** 45) % 103 gives as 10. Meaning that a is 45. 

Now to get the secret key:

S = B^a (mod 103)
S = 71^45 (mod 103)
S = 31

Answer to Question:

- It is computationally impossible to find the private key a if the p is very large. Because we are brute forcing, we are not at the computational level to get the answer for a if the p value is very large.



____
RSA
____

Bob's Public key 

e = 17, n = 266473

Now we need to factor n to get two prime numbers. Here, I used a python script to get the factors.

```bash
def find_factors(number):
    for i in range(1, number + 1):
        if number % i == 0:
            print(i)

num = 266473
find_factors(num)
```

```bash 
1
439
607
266473
```

Now that we have the factors, we use the Euler's totient function from wikipedia, "https://en.wikipedia.org/wiki/RSA_cryptosystem".

```bash 
phi(n) = (p-1)(q-1)
```

Such that n = p * q (p and q are the prime numbers we got from factoring the n; 266473)

```bash 
phi(n) = (438)(606)
phi(n) = 265428

```

Now we need to find d * e equivalent to 1 (mod 265428)

To find d I used the pow() function in python as so: 

```bash 
e = 17
phi_n = 265428
d = pow(e, -1, phi_n)
print(d)

187361
```
So d = 187361

Now, our message M is = C^d (mod n)

Meaning, M = (42750 ** 187361) % 266473
         M = 18533

Now that we have the message, I couldn't figure out the Ascii so after doing some google searching, I figured that sometimes 2 ascii characters are pack together to decrypt messages into 16-bits. 

After finding out how to unpack it as so, 

```bash   
character1 = m // 256   
character2 = m % 256

character1 = 18533 // 256 = 72 => "H"
and 
character2 = 18533 % 256 = 101 => "e"

```

Now that I had the intuition and necessary information, I wrote another python script to decrypt the message for me. 

```bash 
# Bob's public key
e = 17
n = 266473

# Encrypted data sent from Alice to Bob
ciphertext = [42750, 225049, 67011, 9062, 263924, 83744, 10951, 156009,
174373, 125655, 207173, 200947, 227576, 183598, 148747, 211083,
225049, 218587, 191754, 164498, 225049, 171200, 193625, 99766,
94020, 223044, 38895, 74666, 48846, 219950, 139957, 77545,
171672, 165278, 150326, 262673, 164498, 142355, 77545, 171672,
255299, 5768, 264753, 75667, 261607, 31371, 164498, 140654,
244325, 140696, 40948, 179472, 168428, 34824, 32543, 30633,
104926, 190298, 148747, 132510, 42607, 232272, 42721, 188452,
239228, 50536, 216512, 139240, 78779, 166647, 100152, 261607,
121165]

# Step 1: Factor n = 439 * 607 (266473)
p, q = 439, 607
phi = (p - 1) * (q - 1)

# Step 2: Compute private key d
d = pow(e, -1, phi)

# Step 3: Decrypt each ciphertext block
plaintext_numbers = [pow(c, d, n) for c in ciphertext]

# Step 4: Unpack each number into two ASCII characters
message = ""
for m in plaintext_numbers:
    c1 = m // 256   # high byte
    c2 = m % 256    # low byte
    message += chr(c1) + chr(c2)

# Step 5: Print the decoded message
print(message)

```

```bash 
feraidon@abdulf cs338 % python3 rsa_decrypter.py

Hey Bob, here's some cryptography history for you (https://en.wikipedia.org/wiki/The_Magic_Words_are_Squeamish_Ossifrage). Happy factoring, Alice.

```

The message is now decrypted and I guess I have to go read the wikipedia article.

_______
Answers to Questions: 
_______

**Why this breaks for large integers?**  

I solved this by brute force (finding exponents \(a\) and \(b\)). That’s the *discrete logarithm problem*. With small \(p\) it’s easy, but with cryptographically large primes, discrete logs are computationally infeasible.


**Where this would fail with big integers?**

I obtained d because I could factor n. In a real RSA modulus, factoring the n is not computationally feasible, and that is the step that would fail.

**Why the encoding is insecure (even if n were large)?**

I think the encoding is insecure because there isn't any randomness in the RSA, so, if the same words or characters appear more than once, it will produce the same encrypted number every time. 







