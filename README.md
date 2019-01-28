# SSL_Apply
SSL for Free Apply and using on Windows IIS with OpenSSL Tutorial

Https Apply Tutorial
===

- Author: 周秉楠

- 參考文件: https://ephrain.net/wordpress-%E4%BD%BF%E7%94%A8-dns-%E6%89%8B%E5%8B%95%E9%A9%97%E8%AD%89%E7%9A%84%E6%96%B9%E5%BC%8F%EF%BC%8C%E5%8F%96%E5%BE%97-ssl-for-free-%E7%9A%84-https-%E6%86%91%E8%AD%89/  https://dotblogs.com.tw/supershowwei/2016/05/29/232917

前言:
---
此篇主要紀錄如何於NCTU ME上申請一個新網域並為此網域於Windows IIS 加上SSL憑證。

步驟
---
### 1. 申請網域(Domain) : NCTU Domain
- 利用nctu.me申請一個新網域
<img src="https://i.imgur.com/ZGXaDoX.png" height="200" />

### 2. 至SSL for Free網站，選擇 Manual Verification (DNS):
<img src="https://i.imgur.com/H1rlBk5.png" height="200" />
- 按下驗證按鈕
<img src="https://i.imgur.com/5AyyJnB.png" height="200" />

### 3. 於NCTU ME的網域DNS上，加上指定的 TXT 記錄：
<img src="https://i.imgur.com/NcBGD0h.png" height="200" />
點選NCTU ME網站您申請的網域後面的DNS管理，並於TXT加入上面提到的value
<img src="https://i.imgur.com/witvVGV.png" height="200" />
<img src="https://i.imgur.com/tSlQT3W.png" height="200" />

**注意: 名稱填寫好 _acme-challenge 即可，後面的網域名稱已經幫你添加好了!**
<img src="(https://i.imgur.com/WkI6XUL.png" height="200" />

### 4. 輸入好之後，可以回到 SSL for Free 網頁，點下 Verify _acme_challenge.<網域名稱> 的連結。如果 SSL for Free 可以成功取得 DNS 的 TXT 記錄的話，可以看到像下面的結果：
<img src="(https://i.imgur.com/JeVVgoC.png" height="200" />

### 5. 驗證成功後，即可下載ssl憑證
<img src="(https://i.imgur.com/dB2nwB3.png" height="200" />
### 6. Local端下載好的ssl憑證包:
<img src="(https://i.imgur.com/lkTAWZz.png" height="200" />

### 7. SSL for Free產生的憑證是 *.crt 而不是 *.pfx，然而 IIS 只能使用 *.pfx 憑證檔，所以這時候就需要透過OpenSSL軟體做轉換。
<img src="(https://i.imgur.com/cvZhCen.png" height="200" />

### 8. 完成OpenSSL安裝後，即可在cmd中輸入以下步驟:

``` shell
cd C:\OpenSSL-Win32\bin
```

``` shell
openssl pkcs12 -export -out  C:\sslforfree\certificate.pfx -inkey  C:\sslforfree\private.key -in  C:\sslforfree\certificate.crt -certfile  C:\sslforfree\ca_bundle.crt

```
其中會要您輸入密碼，此密碼將是在IIS匯入*.pfx憑證的密碼，因此要記住!

