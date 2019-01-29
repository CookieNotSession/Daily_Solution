# SSL_Apply
SSL for Free Apply and using on Windows IIS with OpenSSL Tutorial

Https Apply Tutorial
===

- Author: 周秉楠

- 參考文件: [SSL for Free教學(申請步驟教學)](https://ephrain.net/wordpress-%E4%BD%BF%E7%94%A8-dns-%E6%89%8B%E5%8B%95%E9%A9%97%E8%AD%89%E7%9A%84%E6%96%B9%E5%BC%8F%EF%BC%8C%E5%8F%96%E5%BE%97-ssl-for-free-%E7%9A%84-https-%E6%86%91%E8%AD%89/) & [OpenSSL教學(cmd指令參考來源)](https://dotblogs.com.tw/supershowwei/2016/05/29/232917) & [IIS - 安裝 SSL 憑證 (著重於IIS繫結綁定網域設定)](https://blog.johnwu.cc/article/iis-install-ssl-certificate.html
)

Introduction
---
因碩士論文撰寫的系統需打開client端的webcam，因此有webcam access需求，需要用到https，因此決定寫一篇Readme.md來紀錄自己如何於nctu.me網域上申請一個新的網域並利用SSL for Free網站來免費獲取SSL憑證，再為此新網域於Windows IIS 加上SSL憑證，來為自己的網域提供一個為期3個月的免費SSL服務。

Steps
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

- 點選NCTU ME網站您申請的網域後面的DNS管理，並於TXT加入上面提到的value

<img src="https://i.imgur.com/witvVGV.png" height="100" />
<img src="https://i.imgur.com/tSlQT3W.png" height="200" />

**注意: 名稱填寫好 _acme-challenge 即可，後面的網域名稱已經幫你添加好了!**
<img src="https://i.imgur.com/WkI6XUL.png" height="100" />

### 4. 輸入好之後，可以回到 SSL for Free 網頁，點下 Verify _acme_challenge.<網域名稱> 的連結。

- 如果 SSL for Free 可以成功取得 DNS 的 TXT 記錄的話，可以看到像下面的結果：

<img src="https://i.imgur.com/JeVVgoC.png" height="100" />

### 5. 驗證成功後，即可下載ssl憑證
<img src="https://i.imgur.com/dB2nwB3.png" height="300" />

### 6. Local端下載好的ssl憑證包:
<img src="https://i.imgur.com/lkTAWZz.png" height="100" />

### 7. SSL for Free產生的憑證是 *.crt 而不是 *.pfx，然而 IIS 只能使用 *.pfx 憑證檔，所以這時候就需要透過OpenSSL軟體做轉換。
<img src="https://i.imgur.com/cvZhCen.png" height="200" />

### 8. 完成OpenSSL安裝後，即可在cmd中輸入以下步驟:

``` shell
cd C:\OpenSSL-Win32\bin
```

``` shell
openssl pkcs12 -export -out  C:\sslforfree\certificate.pfx -inkey  C:\sslforfree\private.key -in  C:\sslforfree\certificate.crt -certfile  C:\sslforfree\ca_bundle.crt

```
- 其中會要您輸入密碼，此密碼將是在IIS匯入*.pfx憑證的密碼，因此要記住!
### 9. 綁定Windows IIS網域

**注意:點選站台中旁邊的「繫結」後，進入介面後，點選畫面中藍色的主機名稱兩下，即可進入「編輯站台繫結」模式**

<img src="https://i.imgur.com/7iDIjrU.png" height="200" />

編輯模式中，**「SSL憑證」選項**若為「未選取」，請改為「cookiechou.nctu.me」(您的網域名稱)
<img src="https://i.imgur.com/jquLI2U.png" height="200" />
(圖片來源: https://blog.johnwu.cc/article/iis-install-ssl-certificate.html )

### 10. 成功設定https，即可使用webcam access等服務!

<img src="https://i.imgur.com/dL8MOB1.png" width="200" />


