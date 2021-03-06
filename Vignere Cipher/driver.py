import os
from vignere import *


def parse(st):
    parsed_list = []
    cur = ""
    for i in st:
        if i == '[':
            cur = ""
        elif i == ']':
            parsed_list.append(cur)
        else:
            cur += i
    return parsed_list

start_time = time.time()
path = "E:\IIITD\Semester 1\AI\Project\\vignere\\"
cipher_file = os.path.join(path, "cipher.txt")
cipher_file = open(cipher_file)
cipher = cipher_file.read()

res_file = os.path.join(path, "result.txt")
res_file = open(res_file)
results = res_file.read()

key_file = os.path.join(path, "key.txt")
key_file = open(key_file)
res_key = key_file.read()

print(cipher)
ciphers = parse(cipher)
results = parse(results)

plain_texts = []
for cur_cipher in ciphers:
    print ("Current Cipher = ", cur_cipher)
    vignere = Vignere([], cur_cipher)
    vignere.add_pop(vignere.initialize(pop_limit))
    vignere.print_pop()
    vignere.genetic()
    cur_best = vignere.get_last()
    plain_texts.append(cur_best[2])

acc = 0
for i in range(len(plain_texts)):
#     print("["+plain_texts[i]+"]")
#     print(results[i])
    if plain_texts[i] == results[i]:
        acc += 1
        print("MATCHED")


sim = 0
for i in range(len(plain_texts)):
    count = 0
    size = len(plain_texts[i])
    cur_key = ""
    cur_key = cur_key.join(plain_texts[i])
    for j in range(size):
        if plain_texts[i][j] != results[i][j]:
            count+=1
    sim += (size-count)/size

keysim = 0


print("accuracy = ", acc/len(results) * 100)
print("similarity = ", sim/len(results) * 100)
print("total time taken = ", time.time()-start_time)