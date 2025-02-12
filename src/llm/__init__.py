from typing import Dict
from .base import BaseLLM
from .openai_llm import OpenAILLM
from .ollama_llm import OllamaLLM

class LLMFactory:
    @staticmethod
    def create(provider: str, config: Dict) -> BaseLLM:
        if provider == "openai":
            return OpenAILLM(config['openai'])
        elif provider == "ollama":
            return OllamaLLM(config['ollama'])
        else:
            raise ValueError(f"不支持的提供商: {provider}")
