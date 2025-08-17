# -*- coding: utf-8 -*-
import json
import os
from typing import Any, Dict

class ConfigLoader:
    """載入並管理 JSON 設定檔"""
    def __init__(self, config_path: str = "config/settings.json") -> None:
        self.config_path = config_path
        self.config: Dict[str, Any] = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """從 JSON 檔案載入設定"""
        if not os.path.exists(self.config_path):
            raise FileNotFoundError(f"找不到設定檔：{self.config_path}")
        with open(self.config_path, "r", encoding="utf-8") as f:
            return json.load(f)

    def get(self, key: str, default: Any = None) -> Any:
        """取得指定設定值"""
        return self.config.get(key, default)

    def reload(self) -> None:
        """重新載入設定檔"""
        self.config = self._load_config()
