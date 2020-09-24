---
title: ksnctf Q.11
date: "2020-09-04"
draft: false
category: "CTF"
tags:
    - "ksnctf"
cover: "../media/"
---

# ksnctf Q.11 Riddle

難しかった。

IDA の使い方を覚えるのに時間がかかった。

FLAG の文字数まではわかったものの、その後進展できず。

write up からヒントをもらい、解き終えた。

重要だったのは、

入力を xor する処理

と

入力文字と FLAG を比較する処理

ctf みたいな、文字列を直接表示できないプログラムではよく使われる処理らしい。

## 感想

それにしても、pwn はやっぱり面白い。

そして、やっぱりめっちゃ難しい。

アセンブリから処理をイメージすることが難しい。

もうちょっと特訓を積みたい！