---
title: ksnctf Q.3
date: "2020-08-26"
draft: false
category: "CTF"
tags:
    - "ksnctf"
cover: "../media/"
---

# ksnctf Q.3

色々調べてみると、にゃるこさんのコードが js としてちゃんと機能していることが分かった。

最初は１からコードを見やすい形に直して理解しようとしたが、めんどくさくなり別のやり方を模索。
そうしているうちに、かんまで一行区切りだということに気付いたため、コードをカンマ区切りで改行し、
各行を実行して様子を調べることにした。(chrome のディベロッパーツールを使用)
そうすると、ひときわ長い行があり、それを実行すると utf-8 の文字列であることが分かった。
\u0030 みたいなやつ。これを変換機にかけると見やすい js が出現。
これを読みといていく。
全体のコードはこうだ。

```
$(function () {
  $("form").submit(function () {
var t = \$('input[type="text"]').val();
var p = Array(70, 152, 195, 284, 475, 612, 791, 896, 810, 850, 737, 1332, 1469, 1120, 1470, 832, 1785, 2196, 1520, 1480, 1449);
var f = false;
if (p.length == t.length) {
f = true;
for (var i = 0; i < p.length; i++)
if (t.charCodeAt(i) \* (i + 1) != p[i]) f = false;
if (f) alert("(」・ω・)」うー!(/・ω・)/にゃー!");
}
if (!f) alert("No");
return false;
});
});
```

これがもう答えであることはすぐに分かった。
p が答えの文字コードたちで、これを(i + 1)で割った文字コードに対応する文字が答えとなる。
ただ、chrome では正しく jquery を読み込めていないため、
