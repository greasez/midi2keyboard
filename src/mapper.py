import json

with open('config/keymap.json', 'r') as file:
    keymap = json.load(file)

def note2key(note: int) -> str | None:
    return keymap.get(str(note), None)