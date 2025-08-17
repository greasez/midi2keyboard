import keyboard
from utils.logger import get_logger

logger = get_logger()

def press_key(key: str):
    try:
        keyboard.press_and_release(key)
        logger.info(f"key: {key}")
    except Exception as e:
        logger.error(f"Error key {key}: {e}")