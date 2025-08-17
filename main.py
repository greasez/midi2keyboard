# -*- coding: utf-8 -*-
from src.midi_listener import listen_midi,choose_midi_device
from src.mapper import note2key
from src.key_emulator import press_key
from utils.logger import get_logger, shutdown_logger

logger = get_logger()

def main():
    key = None
    logger.info("Starting MIDI to keyboard")
    while key == None:
        key = choose_midi_device()
    logger.info("Listening for MIDI input")
    try:
        with listen_midi(key) as midi_input:
            for message in midi_input:
                if message.type == 'note_on':
                    note = message.note
                    logger.info(f"MIDI note: {note}")
                    key_to_press = note2key(note)
                    if key_to_press:
                        press_key(key_to_press)
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        logger.info("Exiting MIDI to keyboard")
        shutdown_logger()

if __name__ == "__main__":
    main()