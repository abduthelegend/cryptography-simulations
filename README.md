# cryptography-simulations
# Cryptography & Cryptanalysis Simulations 🔐

A collection of Python implementations and mathematical simulations exploring the foundations of modern cryptography, information security, and computational complexity. Inspired by **Stanford University's Cryptography I** (Dr. Dan Boneh).

---

## 📂 Implemented Simulations

### 1. Many-Time Pad (Two-Time Pad) XOR Attack (`many_time_pad_attack.py`)
* **Concept:** Stream Ciphers & Perfect Secrecy (Shannon's Theorem).
* **The Math:** A One-Time Pad (OTP) achieves perfect secrecy only when a truly random key $K$ is used **once**. If the same key $K$ encrypts two plaintexts $M_1$ and $M_2$:
  $$C_1 = M_1 \oplus K \quad \text{and} \quad C_2 = M_2 \oplus K$$
  An attacker who intercepts both ciphertexts can compute their XOR to completely eliminate the secret key:
  $$C_1 \oplus C_2 = (M_1 \oplus K) \oplus (M_2 \oplus K) = M_1 \oplus M_2$$
* **Implementation:** Demonstrates key elimination and **crib-dragging**—guessing a probable word in $M_1$ and XORing it against $C_1 \oplus C_2$ to recover the corresponding plaintext in $M_2$.

---

## 🗺️ Planned Simulations (In Progress)
* **Birthday Paradox & Hash Collisions:** Monte Carlo simulation modeling collision probabilities in $n$-bit hash functions ($O(2^{n/2})$ complexity).
* **Block Cipher Modes (CBC & CTR):** Demonstrating Initialization Vector (IV) predictability and bit-flipping attacks.
* **Public-Key Foundations:** Modular exponentiation, Diffie-Hellman key exchange, and small-scale RSA implementations.

---

## 🚀 How to Run Locally

1. Clone the repository:
   ```bash
   git clone https://github.com
   cd cryptography-simulations
   ```
2. Run any simulation using Python 3:
   ```bash
   python many_time_pad_attack.py
   ```
