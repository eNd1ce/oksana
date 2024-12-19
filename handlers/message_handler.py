# handlers/message_handler.py
from telethon import events
from iioksana.utils.preprocessing import preprocess_message
from iioksana.filters.content_filter import is_appropriate

def register_message_handlers(client, chatbot, sentiment_analyzer, language_detector, translator, memory, command_handler):
    @client.on(events.NewMessage)
    async def handle_message(event):
        # Проверка активности модуля
        if not command_handler.module_active:
            return

        user_id = event.sender_id
        user_input = event.raw_text

        # Предобработка сообщения
        processed_input = preprocess_message(user_input)

        # Определение языка сообщения
        language = language_detector.detect_language(processed_input)

        # Перевод на русский язык, если необходимо
        if language != 'ru':
            processed_input = translator.translate_to_ru(processed_input, src_lang=language)

        # Анализ настроения
        sentiment = sentiment_analyzer.analyze_sentiment(processed_input)

        # Генерация ответа через GPT-4
        response = await chatbot.generate_response(user_id, processed_input, sentiment)

        # Перевод ответа на язык пользователя, если необходимо
        if language != 'ru':
            response = translator.translate(response, dest_lang=language)

        await event.reply(response)
