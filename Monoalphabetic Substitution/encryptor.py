import random

pt_file = "plainText.txt"
plainText = open(pt_file).read()
print(plainText)

key = ['A'] * 26
str_key = ""
for i in range(len(key)):
    key[i] = chr(i+65)
random.shuffle(key)
str_key = str_key.join(key)
print(key)

key_file = "key.txt"
cur_key = open(key_file, "w")
cur_key.write(str_key)

res = ""
count = 0
for i in plainText:
    i = i.upper()
    if i == ']':
        res += "]\n"
        count += 1
    elif i != ' ' and i != '\n' and i != '.' and i!= "," and i!=";" and i!="?":
        res += i
res_file = "result.txt"
result = open(res_file, "w")
result.write(res)


res = ""
i_res = ""
for i in plainText:
    temp = ""
    i = i.lower()
    if i == '[':
        i_res = ""
    elif 96 < ord(i) < 123:
        temp = key[ord(i) - 97]
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
