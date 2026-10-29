
# Caesar Cipher Implementation - CNS Assignment

This project contains the implementation, web-based demonstration, and security analysis of the **Caesar Cipher**, developed as part of the Cryptography and Network Security (CNS) coursework[cite: 1, 2, 3].

---

## 📋 Table of Contents
1. [Algorithm Understanding & Explanation](#1-algorithm-understanding--explanation)
2. [Security Analysis, Efficiency & Limitations](#4-security-analysis-efficiency--limitations)
3. [Files Included](#2-files-included)


---

## 1. Algorithm Understanding & Explanation

### **Introduction**
The **Caesar Cipher** is one of the simplest, earliest, and most widely known substitution ciphers[cite: 3]. It is a type of replacement cipher where each letter in the plaintext is shifted a fixed number of positions down the alphabet. For example, with a shift of $3$, 'A' becomes 'D', 'B' becomes 'E', and so on.

## 2. Security Analysis, Efficiency & Limitations

* **Key Space Limitations:** The Caesar cipher only has **25 possible keys**. This makes it completely insecure against modern cryptographic standards because an attacker can easily execute a brute-force attack by trying all 25 shift combinations in a fraction of a second.
* **Vulnerability to Frequency Analysis:** Natural languages (like English) have distinct letter frequencies (e.g., 'E' is the most common letter). The Caesar cipher preserves these relative frequencies, allowing cryptanalysts to break the cipher easily through letter distribution analysis.
* **Efficiency:** 
  * **Time Complexity:** $O(n)$, where $n$ is the length of the string, making it instantaneous.
  * **Space Complexity:** $O(n)$ to store the transformed string.
* **Conclusion:** While unsuitable for protecting sensitive real-world data, it serves as a foundational pedagogical tool to introduce basic concepts of Shannon’s principles of **confusion** and **substitution**.
## 3. Files Included
* `caesar.py`: Python script containing the encryption, decryption, and test cases.
* `index.html`: Interactive web page to demonstrate the Caesar cipher live in any browser.

---

