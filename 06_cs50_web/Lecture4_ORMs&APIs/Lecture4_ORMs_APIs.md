# CS50 Lecture4- ORMs,APIs


```python
class Flight:
    def __init__(self, origin, destination, duration)
    self.origin = origin
    self.destination = destination
    self.duration = duration
```
Q&A
---

Q: what is self ? do we have to use it?
A: self就是可以使我們可以更新特定對象的來源，並

---

Q: 一定要使用self這個詞嗎?
A: 可以改為其他詞來表示相同功能，但大部分還是照慣例使用slef一詞

---

Q:  一定要創立__init__嗎?
A: 可以，可以改為pass，產生一個空的類別，但若要創立一個物件去控制不同方法，就要創立一個類別

---
```python
if __name__ == "__main__":
    main()
```
Q: if __name == "__main__"?
A: Python由上而下的執行code，所以我們所有相關的code都包含在def main()中。除非我去call main function，不然此function是不會運作的，因此if __name__ = "__main__"表示: 「如果我運行這個特定文件，我們就做以下的事情: main() 也就是調用main()函式」

---

Q: 若拿掉if，直接調用main()呢，會運行嗎?
A: 可以運行，但通常不這樣做的原因，是如果我們想要import此文件(classes1.py)到其他文件中，如果我導入classes1.py，將會從上而下的讀取code，並擊中這個main()函數，但如果不想在每次導入此classes1.py文件時，這個特定的對象一直產生，就要使用if，可以表示:「只有我運行此文件才需要跑main()，而不是導入其他文件時，就跑main()」

ORMs
===
Object-Relational Mapping: 允許我們使用Python類別和方法和SQL Database互動。




