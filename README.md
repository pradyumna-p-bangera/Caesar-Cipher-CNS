
# Caesar Cipher Implementation - CNS Assignment

This project contains the implementation, web-based demonstration, and security analysis of the **Caesar Cipher**, developed as part of the Cryptography and Network Security (CNS) coursework[cite: 1, 2, 3].

---

## 📋 Table of Contents
1. [Algorithm Understanding & Explanation](#1-algorithm-understanding--explanation)
2. [Files Included](#2-files-included)
3. [Python Implementation](#3-python-implementation)
4. [Security Analysis, Efficiency & Limitations](#4-security-analysis-efficiency--limitations)
5. [How to Run](#5-how-to-run)

---

## 1. Algorithm Understanding & Explanation

### **Introduction**
The **Caesar Cipher** is one of the simplest, earliest, and most widely known substitution ciphers[cite: 3]. It is a type of replacement cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. For example, with a shift of $3$, 'A' becomes 'D', 'B' becomes 'E', and so on.

### **Mathematical Formulation**
Let $P$ be the plaintext letter, $C$ be the ciphertext letter, and $k$ be the secret shift key ($0 \le k \le 25$).

* **Encryption Formula:** 
  $$C = (P + k) \bmod 26$$
* **Decryption Formula:** 
  $$P = (C - k) \bmod 26$$

---

## 2. Files Included
* `caesar.py`: Python script containing the encryption, decryption, and test cases.
* `index.html`: Interactive web page to demonstrate the Caesar cipher live in any browser.

---

## 3. Python Implementation
You can run the script using Python:
```bash
python caesar.py
