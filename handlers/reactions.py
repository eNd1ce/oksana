# handlers/reactions.py
from telethon import events
from iioksana.utils.media import process_image, process_audio

class ReactionHandler:
    def __init__(self, client, chatbot):
        self.client = client
        self.chatbot = chatbot
        self.register_handlers()

    def register_handlers(self):
        @self.client.on(events.NewMessage)
        async def handle_reaction(event):
            user_id = event.sender_id
            if event.message.media:
                file_path = await event.message.download_media()
                if event.photo:
                    # Обработка изображения
                    result = process_image(file_path)
                    await event.reply(result)
                elif event.document:
                    if event.file.mime_type.startswith('audio/'):
                        # Обработка аудио
                        result = process_audio(file_path)
                        await event.reply(result)
                    else:
                        await event.reply("Извините, я не могу обработать этот тип файла.")
                else:
                    await event.reply("Извините, я не могу обработать этот тип медиа.")
