def prepare_n_gram(file_name, val):
    global  n
    n = val
    ngram = {}
    raw_ngram = []
    my_file = open(file_name)
    raw_ngram = my_file.read().split()
    word = []
    for i in range(0, len(raw_ngram) - 1, 2):
        ngram[raw_ngram[i]] = raw_ngram[i + 1]
        word.append(raw_ngram[i])
    raw_ngram = word
    for x in raw_ngram:
        print(x)
    for x in ngram:
        print(x, ngram[x])
    return ngram, raw_ngram


def init():
    global setup, cipher, quadgrams, raw_quadgrams, bigrams, raw_bigrams
    cipher_file = "cipher.txt"
    my_cipher_file = open(cipher_file)
    # raw_bigram = my_cipher_file.read()
    cipher = my_cipher_file.read()
    # bigrams, raw_bigrams = prepare_n_gram("english_bigrams.txt", 2)
    bigrams, raw_bigrams = prepare_n_gram("english_quadgrams.txt", 4)
    print(cipher)
    setup = True


def convert(key):
    # res = []
    str = ""
    for w in cipher:
        for i in range(0, len(w)):
            for j in range(0, len(key)):
                if w[i] == key[j]:
                    w = w[:i] + chr(j + 65) + w[i + 1:]
                    break
        # res.append(w)
        str += w
    return str


def fit_bi_check(key):
    if not setup:
        init()
    plain_text = convert(key)
    score = 0
    for i in range(0, len(cipher)):
        temp = plain_text[i:i + n]
        if temp in raw_bigrams:
            score += int(bigrams[temp])
    return score, plain_text

'''
def fit_quad_check(key):
    if not setup:
        init()
    plain_text = convert(key)
    score = 0;
    for i in range(0, len(cipher)):
        temp = plain_text[i:i+2]
        if temp in raw_quadgrams:
'''

setup = False
cipher = ""
n = 0
bigrams = {}
raw_bigrams = []
quadgrams = []
raw_quadgrams = []
'''

init()

xyz = ('X', 'Y', 'Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q',
       'R', 'S', 'T', 'U', 'V', 'W')
a, b = fit_bi_check(xyz)
print(a, b)

# xyz = ('H', 'B', 'W', 'Y', 'F', 'G', 'Q', 'Z', 'K', 'R', 'P', 'J', 'L', 'X', 'O', 'N', 'S', 'V', 'A', 'E', 'C', 'T', 'U'
#        , 'I', 'D', 'M')
a, b = fit_bi_check(xyz)
print(a)
print(b)
'''