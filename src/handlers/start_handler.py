def start_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Hello! Type /help to get info about this bot!")
