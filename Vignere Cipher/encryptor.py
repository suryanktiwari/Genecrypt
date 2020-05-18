import operator
import random

pt_file = "plainText.txt"
plainText = open(pt_file).read()
# print(plainText)


def generate_vignere_key(text_len, start_key):
    key_length = len(start_key)
    key = start_key
    if len(start_key) != text_len:
        remaining_chars = text_len - len(start_key)
        for i in range(remaining_chars):
            key_index = i % key_length
            key += start_key[key_index]
        return key
    else:
        return key


key = ['A'] * 9
# print(key)
str_key = ""
for i in range(len(key)):
    key[i] = chr(i + 65)
random.shuffle(key)
str_key = str_key.join(key)

"""
        forming the start key 
"""

key_file = "key.txt"
cur_key = open(key_file, "w")
cur_key.write(str_key)

"""
    handling special characters
"""

res = ""
count = 0
count_chars = 0
for i in plainText:
    i = i.upper()
    if i == ']':
        res += "]\n"
        count += 1
    elif i != ' ' and i != '\n' and i != '.' and i != "," and i != ";" and i != "?":
        res += i
        count_chars += 1
res_file = "result.txt"
result = open(res_file, "w")
result.write(res)
print(res)

"""
    generating key of same length as plain text 
"""

vignere_key = generate_vignere_key(count_chars, str_key)

print("The key is :" + vignere_key)
res = ""
i_res = ""
key_index = 0
for i in plainText:
    temp = ""
    i = i.upper()
    if i == '[':
        i_res = ""
    elif i.isalpha():
        temp = (ord(i) + ord(vignere_key[key_index])) % 26
        temp += ord('A')
        temp = chr(temp)
        key_index += 1
    elif i == ']':
        res += "[" + i_res + "]\n"
    elif i != ' ' and i != '\n' and i != '.' and i != "," and i != ";" and i != "?":
        temp = i
    i_res += temp

print(res)
print("Samples = ", count)
cipher_file = "cipher.txt"
cipher = open(cipher_file, "w")
cipher.write(res)