---
title: ksnctf Q.15 Jewel
date: "2020-09-11"
draft: false
category: "CTF"
tags:
    - "ksnctf"
cover: "../media/2020-09-11--ksnctf-q15-jewel.png"
---

apk(android アプリ)の問題。

とりあえず、ctf で apk を扱うときどういうツールを使うのか調べて、それらを使って色々調べてみることに。

最終的に使ったツールたち

-   apktool: apk を unzip するツール。AndroidManifest とか見れる
-   jadx: jar をデコンパイルするツール
-   dex2jar dex を jar に変換するツール

すると簡単に java ソースコードがでてきた。
何やらデバイス ID を SHA256 でほにゃほにゃしているっぽい。

```java
public class JewelActivity extends Activity {
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        setContentView(2130903040);
        String deviceId = ((TelephonyManager) getSystemService("phone")).getDeviceId();
        try {
            MessageDigest instance = MessageDigest.getInstance("SHA-256");
            instance.update(deviceId.getBytes("ASCII"));
            String bigInteger = new BigInteger(instance.digest()).toString(16);
            if (!deviceId.substring(0, 8).equals("99999991")) {
                new AlertDialog.Builder(this).setMessage("Your device is not supported").setCancelable(false).setPositiveButton("OK", new b(this)).show();
            } else if (!bigInteger.equals("356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5")) {
                new AlertDialog.Builder(this).setMessage("You are not a valid user").setCancelable(false).setPositiveButton("OK", new a(this)).show();
            } else {
                InputStream openRawResource = getResources().openRawResource(2130968576);
                byte[] bArr = new byte[openRawResource.available()];
                openRawResource.read(bArr);
                SecretKeySpec secretKeySpec = new SecretKeySpec(("!" + deviceId).getBytes("ASCII"), "AES");
                IvParameterSpec ivParameterSpec = new IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
                Cipher instance2 = Cipher.getInstance("AES/CBC/PKCS5Padding");
                instance2.init(2, secretKeySpec, ivParameterSpec);
                byte[] doFinal = instance2.doFinal(bArr);
                ImageView imageView = new ImageView(this);
                imageView.setImageBitmap(BitmapFactory.decodeByteArray(doFinal, 0, doFinal.length));
                setContentView(imageView);
            }
        } catch (Exception e) {
            Toast.makeText(this, e.toString(), 1).show();
        }
    }
}
```

何やらデバイス ID の比較により、行われているっぽい。

特定のデバイス ID でしか表示されない画像があるっぽい。

しかも画像はその場で生成してる。

デバイス ID の比較は、デバイス ID を SHA256 を通して行っているため直接デバイス ID を特定することはできない。

ただ、

`if (!deviceId.substring(0, 8).equals("99999991"))`

これをみると、デバイス ID の最初の数字が 99999991 にいなっているとわかる。

デバイス ID は 15 桁の数字なので、頑張って特定する。

```python
import hashlib

imei = ""
for i in range(999999910000000, 999999999999999):
    imei = str(i)
    print(imei)
    m= hashlib.sha256()
    m.update(imei.encode())

    if m.hexdigest() == "356280a58d3c437a45268a0b226d8cccad7b5dd28f5d1b37abf1873cc426a8a5":
        print(imei)
        break
```

ちょっと時間かかる。

## ソースコードメモ

`getResources().openRawResource(2130968576)`

これは、リソース ID「2130968576」を取得する関数。
このリソース ID は public.xml で定義されている。（今回は jewel_c.png)

ざっくり関数を調べると、暗号化に関わるものが多い。

上の関数で取得した画像に暗号化を施すと、ちゃんとした画像として見れるっぽい。

というわけで、java でソースコードをそのまま流用して画像の表示を試みる。

```java
class Main {
    public static void main(String[] args) {

        String deviceId = "999999913371337";
        try {
            MessageDigest instance = MessageDigest.getInstance("SHA-256");
            instance.update(deviceId.getBytes("ASCII"));
            String bigInteger = new BigInteger(instance.digest()).toString(16);
            File file = new File("...\jewel_c.png");
            InputStream openRawResource = new FileInputStream(file);
            byte[] bArr = new byte[openRawResource.available()];
            openRawResource.read(bArr);
            SecretKeySpec secretKeySpec = new SecretKeySpec(("!" + deviceId).getBytes("ASCII"), "AES");
            IvParameterSpec ivParameterSpec = new IvParameterSpec("kLwC29iMc4nRMuE5".getBytes());
            Cipher instance2 = Cipher.getInstance("AES/CBC/PKCS5Padding");
            instance2.init(2, secretKeySpec, ivParameterSpec);
            byte[] doFinal = instance2.doFinal(bArr);
            FileOutputStream  outfile = new FileOutputStream("...\\out.png");
            outfile.write(doFinal);
            outfile.close();
        } catch (Exception e) {
        }
    }
}
```

こうして画像を保存すると、しっかりと表示可能な png ファイルができた。

どうやら png 画像にはコメントを埋め込むことができて、そこに flag が書いてあるらしい。

どうにか tEXt チャンクを覗けないか試したものの、最終的には string コマンドを使って、解決した。

## 感想

android 問は少ないらしい。
