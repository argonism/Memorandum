import re

text = ""
with open("program.cpp", "r") as file:
    text = file.read()

text = re.sub(r'[^ \t\n]', '', text)
print(text)
with open("out.txt", "w+") as file:
    file.write(text)