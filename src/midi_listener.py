# -*- coding: utf-8 -*-
import mido
from utils.logger import get_logger

logger = get_logger()

def get_midi_device() -> list:
    input_names = mido.get_input_names()
    if not input_names:
        logger.error("當前沒有可用的MIDI裝置")
        raise RuntimeError("當前沒有可用的MIDI裝置")
    return input_names

def listen_midi(number: int = 0):
    input_name = mido.get_input_names()[number] # 取得MIDI 輸入裝置
    print(mido.get_input_names())
    return mido.open_input(input_name)

def choose_midi_device() -> int:
    devices = get_midi_device()
    print("MIDI devices:")
    for device in devices:
        print(f" - {device}")

    key = input("選擇設備 ( 輸入數字 ): ")
    if key.isdigit():
        device_index = int(key)
        if 0 <= device_index < len(devices):
            selected_device = devices[device_index]
            logger.info(f"midi Device: {selected_device}")
            return device_index
        else:
            logger.error("unvalid device index")
    else:
        logger.error("Please input a valid number")
    return None