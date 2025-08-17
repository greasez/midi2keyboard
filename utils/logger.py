import os
import logging
from datetime import datetime
from utils.config_loader import ConfigLoader

config = ConfigLoader("config/settings.json")
log_dir = "log"
    
def get_logger(name: str = "midi2keyboard"):
    # log資料夾如果不存在則建立
    os.makedirs(log_dir, exist_ok=True)
    
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    if not config.get("enableLog", True):
        logger.handlers.clear()
        logger.disabled = True
        return logger
    
    if not logger.handlers:
        log_date = datetime.now().strftime("%Y-%m-%d") # 設定log檔名稱        
        log_path = f"{log_dir}/midi2keyboard_{log_date}.log" # 設定log檔路徑        
        formatter = logging.Formatter('[%(asctime)s] : %(message)s') # 設定log格式
        
        # 設定log是否輸出到檔案
        if config.get("saveLog", False):                        
            file_handler = logging.FileHandler(log_path, encoding="utf-8")
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        # 設定log是否輸出到控制台
        if config.get("showLog", True):
            stream_handler = logging.StreamHandler()
            stream_handler.setFormatter(formatter)
            logger.addHandler(stream_handler)
    return logger

def shutdown_logger():
    for handler in logging.getLogger().handlers:
        handler.close()
        logging.getLogger().removeHandler(handler)
    logging.shutdown()