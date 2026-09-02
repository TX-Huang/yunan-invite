# 侯畇安 週歲派對 電子邀請卡

線上網址：<https://tx-huang.github.io/yunan-invite/>

打開網址，把朋友的名字一行一個貼進去，按「產生連結」，每個人會拿到一條專屬連結。
朋友點開只會看到寫著他名字的那張卡。

連結格式：

```
https://tx-huang.github.io/yunan-invite/?to=林小美
```

## 派對資訊

| 項目 | 內容 |
| --- | --- |
| 時間 | 2026/9/28（一）14:00 |
| 地點 | 樹瓅咖啡 st. tree cafe |
| 地址 | 新竹縣竹北市隘口三街22號 |

## 要改東西的時候

檔案分兩層。**不要直接改 `index.html`**，它是產生出來的。

| 檔案 | 是什麼 |
| --- | --- |
| `src/invite-picker.html` | 原始檔，文字、樣式、動畫都改這裡 |
| `src/cutout.webp` | 去背好的照片，換照片就換這個檔 |
| `src/build.py` | 把照片嵌進去，產生 `index.html` |
| `index.html` | 產生出來的成品，GitHub Pages 讀這個 |
| `src/makecompare.py` | 產生 A/B 版面比較頁（照片位置在上或在中） |

改完跑一次：

```bash
python src/build.py
```

然後推上去，網站一兩分鐘後自動更新：

```bash
git add -A && git commit -m "改了什麼" && git push
```

## 換一台電腦繼續編輯

```bash
git clone https://github.com/TX-Huang/yunan-invite.git
cd yunan-invite
python src/build.py
```

第一次要先登入 GitHub 才能 push：

```bash
gh auth login
```

## 已經定案的設計決定

- 風格是「樹咖啡」，森林＋秋天，米色底配綠色。
- 照片直接用預先去背好的整張圖，**不要再自己裁切或補畫**，會切到手掌。
- 邀請對象姓名：中文用圓體 `Zen Maru Gothic`，英文用 `Dancing Script`。
  程式會自動判斷是中文還是英文再換字型。
- 秋天小圖案（橡實、蘑菇、南瓜、漿果）要散在整張卡、大小角度都不一樣，
  不要左右對稱排在最上面。
- 地址不顯示郵遞區號，但「查看地圖」的連結有帶，這樣 Google 地圖找得準。
- 頁面有 `noindex`，Google 搜尋不會找到這張邀請卡。
