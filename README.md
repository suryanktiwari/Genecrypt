# Genecrypt: Cipher Breaking Using Genetic Algorithms

Genetic Algorithms are powerful tools that can search for optimal solutions in huge search spaces, making them adequate candidates for searching solutions even for NP hard problems We aim to use GAs to the field of cryptanalysis. 

Motivation is to apply GAs and hybridized GAs to attack cryptic symmetric ciphers as to retrieve original plaintext to analyse the degree of success over traditional brute force attacks. Hill Climbing is applied with Genetic Algorithms to perform memetic learning. All symmetric ciphers are cracked with very high similarities.

This repository was submitted as the course project for AI course at IIITD.

Ciphers Tackled:
1. Monoalphabetic Substitution:
2. Transposition Cipher
3. Vignere Cipher


## Instructions

Directory containing files must have plaintext.txt. This file contains the text that will be ciphered and then deciphered. A sample text with long length with lots of occurrences of every alphabet is better as more natural quadgrams will be generated. 

To add text in the plaintext.txt, add any text to be ciphered and then cracked by placing it within square brackers as **[your-sample1-here]** **[your-sample2-here]** ...

english_quadgrams.txt is a file consisting of popular quadgramss and their score from [Practical Cryptography](http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/). Do check them out. The n_gram_score file is refered from there as well. n_gram_score takes a bigram, trigram or quadgram file with scores as input and returns a score for a piece of text. Score is directly proportional to the number of high ranking ngrams seen in the provided text.

1. Run encryptor.py. This creates three text files.
..*key.txt: This file contains a random key that is used to cipher the plaintext
..*cipher.txt: This file contains the data from plaintext.txt after being put through a Mono substitution cipher.
..*results.txt: This is just plaintext.txt but without spaces so the results obtained after Genetic Learning can be compared.

2. Run driver.py - The resultant text will emerge slowly over the course of generations. At the end, all the results will be scored on similarity measures.
