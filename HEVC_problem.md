GoPro HEVC Problem
===
此篇主要紀錄1/30早上解決Gopro7錄製之影片開頭為'GX'檔案，於Win8各player播放「只有聲音，卻無畫面」之問題。

Introduction
---
1/30早上老爸找我解決Gopro7錄製之影片開頭為'GX'檔案，於Win8各player播放「只有聲音，卻無畫面」之問題，去武陵農場後，就發現GoPro7錄製的影片，只有Time Lapse的
影片開頭是'GH'，且可以在Win8上正常播放，其他一般模式的錄影檔案開頭都是'GX'，且無論是在Media Player、Movie Maker(老爸主要想用來剪片，但匯入後卻只有聲音)或是QuickTime，
皆無法看到影片的畫面(Audio Only)。

Solution
---
- 首先檢查了Win8各Player是否能運行，發現幾乎不行，更在QuickTime Player上運行時，發生了2041 error，此時還是懷疑只是Player不合適之問題。
- 尋找GoPro官方論壇的詳解，開始了解可能是影片的decoding問題，也在留言中看到了有人利用'codec software'解決了類似問題，但始終還是不太了解。
- 後來遠端登入至實驗室電腦，想查看若是用實驗室的Win10來看，會不會有相同問題
- 因此先將老爸Win8電腦中的Gopro GX開頭影片樣本上傳至Google Drive
- 此時，發現了Google Drive上傳後的GX影片卻能夠在雲端平台上順利運行
- 理解了是作業系統相容性的問題
- 並試圖在Win10的player上運行，發現Win10有提供錯誤警示(這點做的的確比Win8好，更來的詳細，比較知道如何debug)，錯誤訊息內容是「請加裝HEVC延伸編碼器」
- 理解了是Win8系統上缺乏了HEVC decode的裝置，近年來因為影像壓縮的流行，HEVC、HEIF等格式開始普及在各個攝影裝置
- 包含記得有次iphone7更新後，變成HEIF格式(也是類似HEVC的一種圖像壓縮格式)，導致我上傳Google時，無法預覽圖片
- 因此到網路上尋找'HEVC decode free'的解碼器
- 順利於Win8系統上運行



