from services.CertificateService import CertificateService
from peewee import DoesNotExist
from helpers import get_id_from_context
from exceptions import InvalidIdFromContextException, CertificateNotFound

CertificateService = CertificateService()


def delete_handler(update, context):
    try:
        id = get_id_from_context(context)
    except InvalidIdFromContextException as e:
        message = e
    else:
        try:
            CertificateService.delete_certificate_by_id(id)
        except DoesNotExist:
            message = "Certificate not found"
        else:
            message = f"Certificate {id} deleted"

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
