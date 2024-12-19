from .message_handler import register_message_handlers
from .reactions import ReactionHandler

def register_handlers(client, chatbot, sentiment_analyzer, language_detector, translator, memory, command_handler):
    register_message_handlers(client, chatbot, sentiment_analyzer, language_detector, translator, memory, command_handler)
    ReactionHandler(client, chatbot)
