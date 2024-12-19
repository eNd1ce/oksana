# models/chatbot_model.py
import openai
from iioksana.config import MAX_HISTORY_LENGTH, OPENAI_API_KEY
from iioksana.utils.memory import Memory

class ChatbotModel:
    def __init__(self):
        openai.api_key = OPENAI_API_KEY
        self.memory = Memory()

    async def generate_response(self, user_id, user_input, sentiment):
        chat_history = self.memory.get_chat_history(user_id)
        chat_history.append(user_input)
        chat_history = chat_history[-MAX_HISTORY_LENGTH:]
        context = ' '.join(chat_history)

        try:
            openai_response = openai.ChatCompletion.acreate(
                engine="gpt-4",
                input=[
                    {"role": "system", "content": "Ты помощник, который отвечает пользователям."},
                    {"role": "user", "content": context}
                ],
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.7,
            )
            final_response = openai_response["choices"][0]["message"].message['content'].strip()
        except Exception as e:
            print(f"Ошибка с API OpenAI: {e}")
            final_response = "Извините, произошла ошибка при генерации ответа."

        final_response = self.adapt_response_based_on_sentiment(final_response, sentiment)
        chat_history.append(final_response)
        self.memory.save_chat_history(user_id, chat_history)
        return final_response

    def adapt_response_based_on_sentiment(self, response, sentiment):
        if sentiment == 'negative':
            response = "Мне жаль это слышать. " + response
        elif sentiment == 'positive':
            response = "Рад, что у вас всё хорошо! " + response
        return response
