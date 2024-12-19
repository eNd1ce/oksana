import os
from dotenv import load_dotenv

load_dotenv()

# Настройки API Telegram
# Если переменная окружения 'API_ID' не найдена, будет использован ID '21523301' по умолчанию.
API_ID = int(os.getenv('API_ID', '24090820'))

# Если переменная окружения 'API_HASH' не найдена, используется значение по умолчанию.
API_HASH = os.getenv('API_HASH', 'd2821114d8d592a1e2b7accc69db6eee')

# Ключ OpenAI API. Если не указан в окружении, используется данный ключ по умолчанию.
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY', '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')

# Настройки подключения к Redis
# Если 'REDIS_URL' не указана, используется redis://localhost:6379.
REDIS_URL = os.getenv('REDIS_URL', 'redis://localhost:6379')

# Настройки модели
MAX_HISTORY_LENGTH = 5  # Максимальная длина истории диалога
