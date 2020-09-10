from passlib.hash import sha512_crypt

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
    source = [ line.rstrip() for line in file.readlines() ]

for passwd in source:
    for dict_ in passhash:
        # print(passwd, "$6$" + dict_['salt'])
        # hash_ = crypt.crypt(passwd, "$6$" + dict_['salt'])
        hash_ = sha512_crypt.encrypt("password", salt=)
        # passlib.hash.sha512_crypt()
        def migrate(self):
            proc = subprocess.run("docker-compose run api rake db:migrate:reset db:seed", shell=True, stdout=PIPE, stderr=PIPE, text=True)
            out = proc.stdout
            print(out)
        print(hash_)
        if hash_ == dict_['hash']:
            print("matched")

