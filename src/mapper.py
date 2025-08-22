from utils.config_loader import ConfigLoader

keymap = ConfigLoader("config/keymap.json")

def note2key(note: int) -> str | None:
    """將midi音符轉換為鍵盤按鍵"""
    return keymap.get(str(note), None)

def reload_keymap() -> None:
    """重新載入鍵位對應表"""
    keymap.reload()