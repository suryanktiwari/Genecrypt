import operator

def makeCipher(text, key):
    # pre processing - padding
    print("Text Length =", len(text))
    pad_length = len(key) - int(len(text)%len(key))
    pad = ""
    for i in range(pad_length):
        pad+="Y"
    text+=pad
    # print("Pad Length =", pad_length)
    # print("Padded Text =", text)

    # converting to columnar transposition cipher
    pT = []
    for i in range(int(len(text) / len(key))):
        temp = []
        for j in range(len(key)):
            temp.append(text[i * len(key) + j])
            # print(temp[j], end="")
        pT.append(temp)
        # print()

    alpha_key = list(key)
    columns = []
    for i in range(len(key)):
        this_col = ""
        for j in range(len(pT)):
            this_col += pT[j][i]
        columns.append((alpha_key[i], this_col))

    cipher = ""
    columns.sort(key=operator.itemgetter(0))
    for col in columns:
        cipher += col[1]

    return (columns, cipher)



pt_file = "plainText.txt"
plainText = open(pt_file).read()
print(plainText)

key = "ZEBRAS"
print(key)

key_file = "key.txt"
cur_key = open(key_file, "w")
cur_key.write(key)

res = ""
cip = ""
temp = ""
count = 0
for i in plainText:
    i = i.upper()
    if i == ']':
        res += "]\n"
        count += 1
        columns, cipher = makeCipher(temp, key)
        cip += "["+cipher+"]\n"
        temp = ""
    elif i=="[":
        res+='['
    elif i != ' ' and i != '\n' and i != '.' and i!= "," and i!=";" and i!="?" and i!="[":
        res += i
        temp += i
res_file = "result.txt"
result = open(res_file, "w")
result.write(res)
print(res)

print("Samples = ", count)
cipher_file = "cipher.txt"
cipher_f = open(cipher_file, "w")
cipher_f.write(cip)
