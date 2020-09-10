# from factordb.factordb import FactorDB
import math

def split_n(text, n):
    return [ text[i:i+n] for i in range(int(len(text)-n+1)) ]

def is_prime(n):
# nが素数かどうか判定するプログラム
  for p in range(2, int(math.sqrt(n)) + 1):
    if n % p == 0:
      return False # 素数でないならFalseを返す
  return True # 素数ならTrueを返す

text = ""
with open("pi.txt", "r") as file:
  text = file.read()

digits = split_n(text, 10)

for digit in digits:
  if is_prime(int(digit)):
    print("flag found:", digit)
  print(digit)

# f = FactorDB(11)
# f.connect()
# print(len(f.get_factor_list()))


