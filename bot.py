# bot.py
import asyncio
from telethon import TelegramClient
from iioksana.config import API_ID, API_HASH
from .handlers import register_handlers
from iioksana.models.chatbot_model import ChatbotModel
from iioksana.models.sentiment_analysis import SentimentAnalyzer
from iioksana.models.language_detection import LanguageDetector
from iioksana.models.translation import Translator
from iioksana.utils.memory import Memory
from .handlers.command_handler import CommandHandler

async def main():
    client = TelegramClient('iioksana', API_ID, API_HASH)
    await client.start()

    # Инициализация компонентов
    chatbot = ChatbotModel()  # GPT-4 only
    sentiment_analyzer = SentimentAnalyzer()
    language_detector = LanguageDetector()
    translator = Translator()
    memory = Memory()
    command_handler = CommandHandler(client)

    # Регистрация обработчиков
    register_handlers(
        client,
        chatbot,
        sentiment_analyzer,
        language_detector,
        translator,
        memory,
        command_handler
    )

    print("Бот запущен")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())

