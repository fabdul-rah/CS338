# Feraidon AbdulRahimzai
# CS338 - BEING EVE
# September 29, 2025


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
