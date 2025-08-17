# midi to keyboard

MIDI 輸入訊號轉鍵盤訊號輸出，目的為在遊戲裡面使用自己的MIDI設備玩音樂！
以永劫無間為例，永劫無間在蓬萊島有樂器供玩家彈奏，彈奏方式是使用鍵盤按下對應的按鍵就會發出對應的音調出來。
但是鍵盤真的不好按，因此誕生出這個小工具。

## 如何使用

本專案使用python撰寫，因此需先到python官網下載python，版本選擇3.10.6，下載並安裝。
**安裝python時記得要勾選「Add Python to PATH」**

將專案下載下來後，解壓縮到任意位置(路徑盡量不要有中文)，並記住該資料夾的位置。

作業系統是win11的話，搜尋`終端機`，並打開。
win10的話，搜尋`powershell`，並打開。
執行下面指令，以解壓縮到C槽為例

移動到專案資料夾

```powershell
cd C:\midi2keyboard
```

更新pip版本

```powershell
python -m pip install --upgrade
```

安裝依賴套鍵

```powershell
pip install -r requirements.txt

```

執行程式，如果要再次執行的話，只需要執行這行。
如果關掉`終端機`或`powershell`，則需要先執行`cd C:\midi2keyboard`後，再執行`python main.py`

```python
python main.py
```

### 注意事項

如果遊戲是用管理員模式開啟的話，則必需使用管理員模式執行程式，否則權限會不夠。

## 鍵位設定

**注意，如果有重新設定鍵位的話，需要將程式關掉，並重新執行設定才會生效**
鍵位映射的設定檔在**config資料夾**裡面的`keymap.json`
以C3為例，我要把C3設為鍵盤上的"Z"：
> 參照下方音符對照的數字，**C3為48**
> "48" : "z",

```plaintext
各音符對應的數字，手邊沒有88鍵的電子琴，因此不清楚最低音支援到哪
C3 = 48
C#3 = 49
D3 = 50
D#3 = 51
...
C4 = 60
C#4 = 61
...以此類推

```

## 其他設定

**注意，如果有更改設定設定檔的話，需要將程式關掉，並重新執行設定才會生效**
其他設定的設定檔在**config資料夾**裡面的`settings.json`，一般來說不需要動到這個。
共有三項設定，如下所示

```json
{
    "enableLog": true, // 是否啟用logger，如果不啟用的話，就不會生成和顯示log紀錄(預設為啟用)
    "showLog": true, // 是否顯示log(預設為顯示)
    "saveLog": true // 是否將log存成檔案(預設為要儲存)
}
```

## 常見問題

為甚麼按了鍵盤沒有反應，但是終端機或Powershell有正常輸出
> 可以嘗試使用管理員模式啟動程式。
