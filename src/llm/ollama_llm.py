import json
import aiohttp
from typing import Dict, List
from .base import BaseLLM

class OllamaLLM(BaseLLM):
    def __init__(self, config: Dict):
        super().__init__(config)
        self.api_base = config.get('api_base', 'http://localhost:11434')
        self.model = config.get('model', 'llama2')
        self.history: List[Dict] = []

    async def chat(self, message: str) -> str:
        try:
            # 构建请求数据
            data = {
                "model": self.model,
                "messages": [
                    {"role": "user", "content": message}
                ],
                "stream": False  # 关闭流式响应
            }

            # 添加历史消息
            if self.history:
                data["messages"] = self.history + data["messages"]

            async with aiohttp.ClientSession() as session:
                async with session.post(
                    f"{self.api_base}/api/chat",
                    json=data,
                    headers={"Content-Type": "application/json"}
                ) as response:
                    if response.status != 200:
                        return f"Ollama API 错误: {response.status}, {await response.text()}"
                    
                    # 解析响应
                    result = await response.json()
                    reply = result.get("message", {}).get("content", "")
                    
                    # 更新历史记录
                    self.add_to_history("user", message)
                    self.add_to_history("assistant", reply)
                    
                    return reply

        except Exception as e:
            return f"Ollama API 错误: {str(e)}" 