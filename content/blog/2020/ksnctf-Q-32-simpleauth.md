---
title: ksnctf Q.32 simple auth
date: "2020-09-11"
draft: false
category: "CTF"
tags:
    - "ksnctf"
cover: "../media/"
---

php のソースコードが見られる。

```php
<!DOCTYPE html>
<html>
  <head>
    <title>Simple Auth</title>
  </head>
  <body>
    <div>
<?php
$password = 'FLAG_????????????????';
if (isset($_POST['password']))
    if (strcasecmp($_POST['password'], $password) == 0)
        echo "Congratulations! The flag is $password";
    else
        echo "incorrect...";
?>
    </div>
    <form method="POST">
      <input type="password" name="password">
      <input type="submit">
    </form>
  </body>
</html>
```

単純なログイン機構だが、脆弱性があるらしい。

30 分くらい試行錯誤してみたり、色々考えてみたが、全然わからん。

というわけで、かなり怪しい strcasecmp を調べる。

しばらく調べていると、このログイン機構、重要なのは`==` ここらしい。

つまり、厳密でない比較。

## 要点

｀ \$\_POST['password'] `

これは、配列が入る可能性がある。

ここに配列を入れると、`strcasecmp($_POST['password'], $password)` これが null になるらしい。

そうなると、`null == 0` の比較となるわけだが、これがなんと true となる。

`==` は、オペランドを相互型変換して、比較をする。

`===` は、型変換なしで比較する、ということらしい。

というわけで、\$password の中身が表示される。

# 感想

こういうのくらい自分で発見したい気持ちありますねぇ
