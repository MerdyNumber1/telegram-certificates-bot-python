def help_handler(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id,
                             text="/create [title] [recipient name] [days to expire] - to create a certificate\n"
                                  "/delete [number] - to delete a certificate\n"
                                  "/get [number] - to get a certificate")
