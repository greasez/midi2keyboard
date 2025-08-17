# midi to keyboard

MIDI 輸入訊號轉鍵盤訊號輸出，目的是在遊戲裡面使用自己的MIDI設備玩音樂！
永劫無間的蓬萊島提供樂器供玩家彈奏，彈奏方式是使用鍵盤按下對應的按鍵就會發出對應的音調出來。
但是鍵盤真的不好按，因此誕生出這個小工具，讓會彈琴的人不用重新熟悉鍵盤鍵位。
![圖片](images/screenshot.png)

## 如何安裝

本專案使用python，因此需自行到python官網下載python，版本選擇3.10.6，下載並安裝。
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

## 如何使用

移動到專案資料夾

```powershell
cd C:\midi2keyboard
```

執行前，**檢查是否接上MIDI設備，如果沒有找到MIDI設備，會執行失敗**。

```powershell
python main.py
```

執行後，選擇你的MIDI設備(輸入後方數字)，就可以在遊戲裡面彈奏樂器~

```plaintext
PS C:\midi2keyboard> python .\main.py
[2025-08-17 23:20:45,775] : Starting MIDI to keyboard
MIDI devices:
 - CASIO USB-MIDI 0
選擇設備 ( 輸入數字 ): 0
[2025-08-17 23:21:25,348] : midi Device: CASIO USB-MIDI 0
[2025-08-17 23:21:25,348] : Listening for MIDI input
['CASIO USB-MIDI 0']
[2025-08-17 23:22:24,597] : MIDI note on: 60
[2025-08-17 23:22:24,669] : keyDown: ,
[2025-08-17 23:22:24,762] : MIDI note off: 60
[2025-08-17 23:22:24,762] : keyUp: ,
[2025-08-17 23:22:24,909] : MIDI note on: 62
[2025-08-17 23:22:24,910] : keyDown: .
[2025-08-17 23:22:25,022] : MIDI note off: 62
[2025-08-17 23:22:25,023] : keyUp: .
[2025-08-17 23:22:25,110] : MIDI note on: 64
[2025-08-17 23:22:25,111] : keyDown: /
[2025-08-17 23:22:25,267] : MIDI note off: 64
[2025-08-17 23:22:25,269] : keyUp: /
```



## 鍵位設定

**注意，如果有重新設定鍵位的話，需要將程式關掉，並重新執行設定才會生效**
鍵位映射的設定檔在**config資料夾**裡面的`keymap.json`
e.g. 以C3、C4為例，我要把電子琴的`C3`設為鍵盤上的`z`、`C4`設為`k`：
參照下方音符對照的數字，**C3為48**

```json
{
    "48": "z",
    "60": "k"
}
```

各音符對應的數字如下：

```plaintext
C3 = 48
C#3 = 49
D3 = 50
D#3 = 51
...
C4 = 60
C#4 = 61
...
以此類推

```

## 其他設定

**注意，如果有更改設定設定檔的話，需要將程式關掉，並重新執行設定才會生效**
其他設定的設定檔在**config資料夾**裡面的`settings.json`，一般來說不需要動到這個。
共有三項設定，如下所示

```json
{
    "enableLog": true, // 是否啟用logger，如果不啟用的話，就不會生成和顯示log紀錄(預設為啟用)
    "showLog": true, // 是否顯示log(預設為顯示)
    "saveLog": true // 是否將log存成檔案(預設為儲存)
}
```

## 常見問題

為甚麼按了鍵盤沒有反應，但是終端機或Powershell有正常輸出
> 可以嘗試使用管理員模式啟動程式。
