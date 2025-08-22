from utils.config_loader import ConfigLoader

keymap = ConfigLoader("config/keymap.json")

def note2key(note: int) -> str | None:
    return keymap.get(str(note), None)

def reload_keymap() -> None:
    keymap.reload()