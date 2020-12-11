from services.CertificateService import CertificateService
from peewee import DataError
import datetime

CertificateService = CertificateService()


def create_handler(update, context):
    if len(context.args) != 3:
        message = "Invalid data"
    else:
        title = context.args[0]
        recipient = context.args[1]

        if len(title) < 256 and len(recipient) < 256:

            days_to_expire = None
            if context.args[2].isdigit():
                days_to_expire = int(context.args[2])

            certificate = CertificateService.create_certificate(title=title,
                                                                recipient_name=recipient,
                                                                days_to_expire=days_to_expire)
            message = f"Certificate created: \n{repr(certificate)}"

        else:
            message = "Data too long"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
