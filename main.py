# -*- coding: utf-8 -*-
from src.midi_listener import listen_midi,choose_midi_device
from src.mapper import note2key
from src.key_emulator import keyDown,keyUp
from utils.logger import get_logger, shutdown_logger

logger = get_logger()

def main():
    device = None
    logger.info("Starting MIDI to keyboard")
    while device == None:
        device = choose_midi_device()
    logger.info("Listening for MIDI input")
    try:
        with listen_midi(device) as midi_input:
            for message in midi_input:
                if message.type == 'note_on':
                    note = message.note
                    logger.info(f"MIDI note on: {note}")
                    key_press = note2key(note)
                    if key_press:
                        keyDown(key_press)
                
                if message.type == 'note_off':
                    note = message.note
                    logger.info(f"MIDI note off: {note}")
                    key_release = note2key(note)
                    if key_release:
                        keyUp(key_release)
    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        logger.info("Exiting MIDI to keyboard")
        shutdown_logger()

if __name__ == "__main__":
    main()