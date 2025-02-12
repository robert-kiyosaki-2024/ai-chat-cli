import pytest
from pathlib import Path
from src.config import load_config

def test_load_config(tmp_path, monkeypatch):
    # 创建临时配置文件
    config_dir = tmp_path / "config"
    config_dir.mkdir()
    config_file = config_dir / "config.yaml"
    
    test_config = """
    llm:
        provider: openai
        api_key: test-key
        model: gpt-3.5-turbo
    """
    
    config_file.write_text(test_config)
    
    # 直接修改配置文件路径
    monkeypatch.setattr("src.config.CONFIG_PATH", config_file)
    
    config = load_config()
    
    assert config["llm"]["provider"] == "openai"
    assert config["llm"]["api_key"] == "test-key"
    assert config["llm"]["model"] == "gpt-3.5-turbo" 