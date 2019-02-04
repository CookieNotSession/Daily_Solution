# Python Crawler BeautifulSoup Basic Tutorial

This is a simple tutorial about how to use the BeautifulSoup basic skill to get the movie title in PTT MOIVE.

- Reference : [Python 網路爬蟲 Web Crawler 基本篇 By 彭彭](https://www.youtube.com/watch?v=9Z9xKWfNo7k)

# The crawler

抓取資料
---

#### 抓取資料有個難題:
- 問題: 大部分網站不希望是利用「程式碼」來獲取資料，只希望造訪網頁的是真正的「使用者(人類)」，因此若直接利用python urllib套件的urlopen方法串接url，可能會得到404 Forbidden等錯誤訊息，被拒絕存取。

- Solution: 為了模仿普通的使用者，就要在我們的Request中設定Header，其中最重要的元素就是User-Agent，此元素可以提供網頁知道，我們用的是哪種瀏覽器、哪個作業系統，這樣PTT伺服器才會認為我們是一個正常的使用者。

- 注意: 我們在urlopen此方法是，open的內容是 "request(帶有url+Header)"的物件

解析資料
---
- 解析資料的格式是HTML，因此我們去pip install BeautifulSoup，利用此套件工具，快速地為HTML格式做解析

- 即可對標籤(tag)做篩選，找到我們真正想要的部分


```python
root = bs4.BeautifulSoup(data, "html.parser")
# data為openurl獲取到的PTT電影版網頁原始碼，並丟給BeautifulSoup解析
```

```python
root.title
# 即可抓到網頁網頁的title標籤
root.title.string
# 即可抓到網頁網頁的title標籤中的「文字」
```

- 工具 find : 會在網頁找出「其中一個」符合條件的tag

```python
root.find("div", class_="title")
# 用一個find，表示你要找的標籤名稱(這裏樣找的是"div")，篩選條件是class="title"的標籤
```

- 如果要抓到所有符合條件的tag，使用find_all

```python
root.find_all("div", class_="title")
# 抓到所有符合條件的tag
```
