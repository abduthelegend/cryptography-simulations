"""
Many-Time Pad (Two-Time Pad) XOR Cryptanalysis Simulation
Demonstrates why reusing a stream cipher key destroys perfect secrecy:
C1 ^ C2 = (M1 ^ K) ^ (M2 ^ K) = M1 ^ M2
"""

import os

def xor_bytes(b1: bytes, b2: bytes) -> bytes:
    return bytes(a ^ b for a, b in zip(b1, b2))

# 1. Two secret messages of equal length
message_1 = b"ATTACK AT DAWN!!"
message_2 = b"RETREAT AT NOON!"

# 2. A single random key (MISTAKE: reused twice!)
key = os.urandom(len(message_1))

# 3. Encrypt both messages with the SAME key
cipher_1 = xor_bytes(message_1, key)
cipher_2 = xor_bytes(message_2, key)

# 4. Attacker intercepts cipher_1 and cipher_2 (without knowing the key)
# XORing them cancels out the key completely!
m1_xor_m2 = xor_bytes(cipher_1, cipher_2)

# 5. Crib-dragging: Attacker guesses a common word ("ATTACK ") in message_1
crib = b"ATTACK "
recovered_start_of_m2 = xor_bytes(m1_xor_m2[:len(crib)], crib)

print("Cipher 1 (hex):", cipher_1.hex())
print("Cipher 2 (hex):", cipher_2.hex())
print("Guessed M1 crib:", crib.decode())
print("Recovered start of M2:", recovered_start_of_m2.decode())
