import keyboard
from utils.logger import get_logger

logger = get_logger()

def keyDown(key: str):
    try:
        keyboard.press(key)
        logger.info(f"keyDown: {key}")
    except Exception as e:
        logger.error(f"Error key {key}: {e}")
def keyUp(key: str):
    try:
        keyboard.release(key)
        logger.info(f"keyUp: {key}")
    except Exception as e:
        logger.error(f"Error key {key}: {e}")