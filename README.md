Directory containing files must have plaintext.txt. This file contains the text that will be ciphered and then deciphered. More text is better. 

english_quadgrams.txt is a file consisting of popular quadgramss and their score from [Practical Cryptography](http://practicalcryptography.com/cryptanalysis/text-characterisation/quadgrams/). Do check them out. The n_gram_score file is refered from there as well. n_gram_score takes a bigram, trigram or quadgram file with scores as input and returns a score for a piece of text. Score is directly proportional to the number of high ranking ngrams seen in the provided text.

1. Run encryptor.py. This creates three text files.
..*key.txt: This file contains a random key that is used to cipher the plaintext
..*cipher.txt: This file contains the data from plaintext.txt after being put through a Mono substitution cipher.
..*results.txt: This is just plaintext.txt but without spaces so the results obtained after Genetic Learning can be compared.

2. Run driver.py - The resultant text will emerge slowly over the course of generations. At the end, all the results will be scored on similarity measures.