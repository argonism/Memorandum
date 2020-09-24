import hashlib
import crypt

def hex_to_string(hex):
    hex_s = str(hex)
    out = ""
    for i in range(int(len(hex_s) / 2)):
        char = chr(int(hex_s[i*2] + hex_s[i*2+1], 16))
        out += char
    return out

passhash = []
with open('pass.txt', 'r') as file:
    text = file.readlines()
    for line in text:
        splited = line.rstrip().split('$')
        passhash.append({
            'salt' : splited[0],
            'hash' : splited[1]
        })

source = []
with open('dictionary.txt', 'r') as file:
    source.append(file.readlines())

for passwd in source:
    for dict_ in passhash:
        # seed = dict_['salt'] + dict_['hash']
        hash_ = crypt.crypt(seed, '$6${0}$'.format(dict_['salt']))
        print(hash_)


