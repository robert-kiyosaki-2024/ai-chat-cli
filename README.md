# 多模型 LLM 聊天工具

这是一个支持多种大语言模型(LLM) API 的命令行聊天工具。目前支持 OpenAI 和 Ollama 等多个 LLM 提供商，可以通过配置文件灵活切换不同的 LLM 服务。

## 功能特点

- 支持多种 LLM 提供商
  - OpenAI (GPT-3.5, GPT-4 等)
  - Ollama (本地部署的开源模型)
  - 可扩展支持其他提供商
- 通过 YAML 配置文件灵活切换 LLM 提供商
- 异步 API 调用，提供更好的性能
- 支持对话历史记录
- 简单直观的命令行界面

## 项目结构
```
.\
 ├── README.md
 ├── requirements.txt
 ├── config/
 │ └── config.yaml # LLM 配置文件
 └── src/
 ├── init.py
 ├── llm/ # LLM 相关实现
 │ ├── init.py # LLM 工厂类
 │ ├── base.py # 基础 LLM 接口
 │ ├── openai_llm.py # OpenAI 实现
 │ └── ollama_llm.py # Ollama 实现
 ├── config.py # 配置加载
 └── cli.py # 命令行界面
```
## 启动虚拟环境

```bash
python -m venv venv
``` 
Windows：
```bash
venv\Scripts\activate
```
Linux：
```bash
source venv/bin/activate
```

## 安装依赖

```bash
pip install -r requirements.txt
```

## 配置文件

在 `config/config.yaml` 文件中配置 LLM 提供商信息:

```yaml
llm:
  provider: openai # 提供商名称
  api_key: your_openai_api_key # OpenAI API 密钥
  model: gpt-4o-mini # 模型名称
```

## 使用方法

```bash
python -m src.cli
```

## 运行测试

1. 安装测试依赖：
```bash
# 安装项目和测试依赖
pip install -e ".[test]"
```

2. 运行所有测试：
```bash
pytest tests/ -v --asyncio-mode=auto
```

3. 运行特定测试文件：
```bash
# 运行 CLI 测试
pytest tests/test_cli.py -v --asyncio-mode=auto

# 运行 LLM 相关测试
pytest tests/test_llm/ -v --asyncio-mode=auto
```

4. 查看测试覆盖率：
```bash
pytest tests/ --cov=src --cov-report=term-missing -v --asyncio-mode=auto
```

### 测试结构

```
tests/
├── conftest.py           # 测试配置和共享 fixture
├── test_config.py        # 配置加载测试
├── test_cli.py          # CLI 界面测试
└── test_llm/            # LLM 相关测试
    ├── test_base.py     # 基础 LLM 类测试
    ├── test_factory.py  # LLM 工厂测试
    ├── test_openai_llm.py
    ├── test_ollama_llm.py
    └── test_claude_llm.py
```

### 主要测试内容

- 基础功能测试
  - LLM 基类功能
  - 配置加载
  - 工厂类创建实例

- API 适配器测试
  - OpenAI API 集成
  - Ollama API 集成

- CLI 界面测试
  - 用户输入处理
  - 命令执行
  - 错误处理

- 异常处理测试
  - API 错误
  - 超时处理
  - 重试机制


```bash
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin git@github.com:robert-kiyosaki-2024/ai-chat-cli.git
git push -u origin main
```