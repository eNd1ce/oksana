# handlers/command_handler.py
from telethon import events

class CommandHandler:
    def __init__(self, client):
        self.client = client
        self.module_active = True
        self.register_handlers()

    def register_handlers(self):
        @self.client.on(events.NewMessage(pattern=r'\.ii\s+(on|off)'))
        async def handle_ii_command(event):
            command = event.pattern_match.group(1)
            if command == 'on':
                self.module_active = True
                await event.respond("Модуль активирован и работает.")
            elif command == 'off':
                self.module_active = False
                await event.respond("Модуль деактивирован.")
            await event.delete()
