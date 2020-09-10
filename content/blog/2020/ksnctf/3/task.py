text = ""
with open("3", "r", encoding="utf_8") as file:
    text = file.read()

print(text)
text = text.replace(",", ",\n")
print(text)
with open("3", "w", encoding="utf_8") as file:
    file.write(text)