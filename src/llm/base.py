from abc import ABC, abstractmethod
from typing import List, Dict

class BaseLLM(ABC):
    def __init__(self, config: dict):
        self.config = config
        self.history: List[Dict] = []
    
    @abstractmethod
    async def chat(self, message: str) -> str:
        """发送消息到 LLM 并获取响应"""
        pass
    
    def add_to_history(self, role: str, content: str):
        """添加消息到历史记录"""
        self.history.append({"role": role, "content": content}) 