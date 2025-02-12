import pytest
from unittest.mock import patch, AsyncMock
from click.testing import CliRunner
from src.cli import main

class TestCLI:
    @pytest.fixture
    def runner(self):
        return CliRunner()

    def test_cli_normal_exit(self, runner):
        result = runner.invoke(main, input="exit\n")
        assert result.exit_code == 0
        assert "感谢使用！再见！" in result.output

    async def test_cli_chat(self, runner):
        with patch('src.cli.LLMFactory.create') as mock_factory:
            # 设置模拟 LLM
            mock_llm = AsyncMock()
            mock_llm.chat.return_value = "test response"  # 直接设置返回值
            mock_factory.return_value = mock_llm
            
            # 简化异步运行的模拟
            def mock_run(coro):
                # 直接返回预设的响应，不创建新的事件循环
                return "test response"
            
            # 模拟对话
            with patch('src.cli.asyncio.run', side_effect=mock_run):
                result = runner.invoke(main, input="hello\nexit\n")
                
                # 验证调用
                assert mock_factory.called
                assert result.exit_code == 0
                # 检查完整的输出内容
                expected_outputs = [
                    "使用 ollama 作为 LLM 提供商",
                    "test response",
                    "感谢使用！再见！"
                ]
                for expected in expected_outputs:
                    assert expected in result.output