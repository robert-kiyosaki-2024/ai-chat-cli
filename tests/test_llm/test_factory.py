import pytest
from unittest.mock import patch
from src.llm import LLMFactory
from src.llm.base import BaseLLM
from src.llm.openai_llm import OpenAILLM
from src.llm.ollama_llm import OllamaLLM

class TestLLMFactory:
    def test_create_openai(self, test_config):
        llm = LLMFactory.create("openai", test_config)
        assert isinstance(llm, OpenAILLM)
    
    def test_create_ollama(self, test_config):
        llm = LLMFactory.create("ollama", test_config)
        assert isinstance(llm, OllamaLLM)
    
    def test_create_invalid(self, test_config):
        with pytest.raises(ValueError) as exc_info:
            LLMFactory.create("invalid", test_config)
        assert "不支持的提供商" in str(exc_info.value) 