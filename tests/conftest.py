import pytest
import yaml
from pathlib import Path
from unittest.mock import AsyncMock

@pytest.fixture
def test_config():
    return {
        "provider": "openai",
        "openai": {
            "api_key": "test-key",
            "api_base": "https://api.openai.com/v1",
            "model": "gpt-3.5-turbo"
        },
        "ollama": {
            "api_base": "http://localhost:11434",
            "model": "llama2"
        }
    }

@pytest.fixture
def mock_response():
    def _create_response(content):
        return type('Response', (), {
            'content': [
                type('Content', (), {'text': content})
            ]
        })
    return _create_response

@pytest.fixture
def mock_client():
    client = AsyncMock()
    client.messages.create.return_value = type('Response', (), {
        'content': [
            type('Content', (), {'text': "test reply"})
        ]
    })
    return client 