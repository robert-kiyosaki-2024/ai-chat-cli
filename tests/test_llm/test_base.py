import pytest
from src.llm.base import BaseLLM

class TestLLMImpl(BaseLLM):  # 重命名类以避免与测试类冲突
    def __init__(self, config: dict):
        self.config = config
        self.history = []
    
    async def chat(self, message: str) -> str:
        return "test response"

class TestBaseLLM:
    @pytest.fixture
    def llm(self, test_config):
        return TestLLMImpl(test_config)
    
    def test_init(self, llm):
        assert llm.config is not None
        assert isinstance(llm.history, list)
    
    def test_add_to_history(self, llm):
        llm.add_to_history("user", "test message")
        assert len(llm.history) == 1
        assert llm.history[0]["role"] == "user"
        assert llm.history[0]["content"] == "test message" 