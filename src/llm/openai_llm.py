from openai import AsyncOpenAI
from .base import BaseLLM

class OpenAILLM(BaseLLM):
    def __init__(self, config: dict):
        super().__init__(config)
        self.client = AsyncOpenAI(
            api_key=config['api_key'],
            base_url=config['api_base']
        )
        self.model = config['model']
    
    async def chat(self, message: str) -> str:
        self.add_to_history("user", message)
        
        try:
            response = await self.client.chat.completions.create(
                model=self.model,
                messages=self.history
            )
            reply = response.choices[0].message.content
            self.add_to_history("assistant", reply)
            return reply
            
        except Exception as e:
            return f"OpenAI API 错误: {str(e)}" 