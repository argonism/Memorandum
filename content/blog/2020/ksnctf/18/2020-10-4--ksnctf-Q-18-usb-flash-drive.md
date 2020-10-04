---
title: ksnctf Q.18 usb flash drive
date: "2020-10-04"
draft: false
category: "CTF"
tags:
    - "ksnctf"
cover: "lltp.jpg"
---

# 問題概要

zip ファイルが配布されており、展開すると img ファイルが見つかる。

# 調査してみる

img ファイルをさらに展開してみると、3 つの画像ファイルと[SYSTEM]と書かれた隠しファイルが見つかった。

strings で FLAG 的な文字列を探したが画像ファイルに埋め込まれているわけではない。

file コマンドで img を調べてみると、

```
drive.img: DOS/MBR boot sector, code offset 0x52+2, OEM-ID "NTFS    ", sectors/cluster 8, Media descriptor 0xf8, sectors/track 63, heads 8, hidden sectors 1, dos < 4.0 BootSector (0x80), FAT (1Y bit by descriptor); NTFS, sectors/track 63, sectors 32767, $MFT start cluster 1365, $MFTMirror start cluster 2, bytes/RecordSegment 2^(-1*246), clusters/index block 1, serial number 0667e77597e77214b; contains bootstrap BOOTMGR
```

と出る。

`DOS/MBR boot sector`とか、`bootstrap BOOTMGR`とかあり、それぞれ調べてみると「ブートセクターの一種」とかなんかとか出てくる。

windows のブートセクターが usb にインストールされてる？?

ん？

よくわからん？

usb に img を入れて、usb から起動しようとしてみたり、virtualbox でなんやかんやしてみたり

ファイルシステムが win のものっぽいので windows でマウントしようとしてもうまくいかず、

linux でやろうとするも mount コマンドの使い方がよくないのかうまくいかず、何もわからない。

結構粘ったが発狂しそうだったので writeup をみることに

## 答え

あまり関係ないが、linux で mount すると中が見れる。

(mount コマンドの使い方が間違っていた) `# mount drive.img /hoge`

fls 　というコマンドがある。

これは、ディスクイメージのディレクトリやファイルの一覧が見れるコマンドだ。

こんな感じで使うと、こんな感じの結果が得られる

`fls drive.img`

```
...
r/r 35-128-1:   Carl Larsson Brita as Iduna.jpg
r/r 37-128-1:   Mona Lisa.jpg
d/d 184-144-2:  output
r/r 38-128-1:   The Great Wave off Kanagawa.jpg
-/r * 36-128-1: Liberty Leading the People.jpg
-/r * 36-128-4: Liberty Leading the People.jpg:00
-/r * 36-128-5: Liberty Leading the People.jpg:01
-/r * 36-128-6: Liberty Leading the People.jpg:02
-/r * 36-128-7: Liberty Leading the People.jpg:03
-/r * 36-128-8: Liberty Leading the People.jpg:04
-/r * 36-128-9: Liberty Leading the People.jpg:05
-/r * 36-128-10:        Liberty Leading the People.jpg:06
-/d * 64-144-2: output
-/d * 104-144-2:        output
-/d * 144-144-2:        output
V/V 256:        $OrphanFiles
```

-/r \* 36-128-1: Liberty Leading the People.jpg

これは削除されたファイルらしい。

復元するには、こんな感じで icat コマンドをいかのように使う。

icat -rs イメージファイル ノード番号 >　出力するファイル

`icat -rs drive.img 36-128-1 > Liberty_Leading_the_People.jpg`

FORENSICS でよく使うっぽい。

こうして出力した画像には
「The flag is in this file, but not in this image」

あとはどうようにして　他のファイルを調べれば完了だ。

## 感想

常設 ctf のようなすでに writeup が上がっているような ctf を勉強目的で解く場合、writeup をみるのにそこまで粘らなくてもいいのかなと思った。

もちろん自分の知っているあり得そうな手を試したり、調べたりすることは必要だが、一問に何時間も描けるようなことはしないほうが勉強になると思う。

というのは、ちょっと数学の勉強に似ているかなと思ったり（知らなきゃ解けない）
下のブログにもそう書いてあったので（）

> 基本的とりあえず過去問。30 分から 1 時間ほど調べて/考えてみてまったく進展がない/何をすればいいか分からないなら解説を見るべき。ただしその後手を動かすこと。

引用元: https://kimiyuki.net/blog/2016/12/02/getting-started-with-ctf/
