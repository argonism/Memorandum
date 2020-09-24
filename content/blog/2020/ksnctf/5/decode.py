import base64

input_text = ""
with open('text', 'r') as file:
    input_text = file.read()

print(input_text)

while input() == "n":
    print("")
    input_text = base64.b64decode(input_text).decode()
    print(input_text)