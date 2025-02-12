import asyncio
import click
from .config import load_config
from .llm import LLMFactory

@click.command()
def main():
    """多模型 AI 聊天工具"""
    # 加载配置
    config = load_config()
    
    # 创建 LLM 实例
    try:
        llm = LLMFactory.create(config['provider'], config)
    except ValueError as e:
        click.echo(f"错误: {e}")
        return
    
    click.echo(f"使用 {config['provider']} 作为 LLM 提供商")
    click.echo("输入 'quit' 或 'exit' 退出")
    
    async def chat_loop():
        while True:
            user_input = click.prompt("你", type=str)
            
            if user_input.lower() in ['quit', 'exit']:
                break
                
            response = await llm.chat(user_input)
            click.echo(f"AI: {response}")
    
    asyncio.run(chat_loop())
    click.echo("感谢使用！再见！")

if __name__ == '__main__':
    main() 