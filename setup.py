from setuptools import setup, find_packages

setup(
    name="llm-chat-tool",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "openai>=1.0.0",
        "aiohttp>=3.8.0",
        "pyyaml>=6.0.0",
        "click>=8.0.0",
        "anthropic>=0.8.0",
    ],
    extras_require={
        "test": [
            "pytest>=7.0.0",
            "pytest-asyncio>=0.23.0",
            "pytest-mock>=3.10.0",
            "pytest-cov>=4.1.0",
        ],
    },
) 