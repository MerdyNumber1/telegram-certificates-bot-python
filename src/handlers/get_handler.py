from services.CertificateService import CertificateService
from helpers import get_id_from_context
from exceptions import InvalidIdFromContextException, CertificateNotFound

CertificateService = CertificateService()


def get_handler(update, context):
    try:
        id = get_id_from_context(context)
        certificate = CertificateService.get_certificate_by_id(id)
        message = f"Certificate found: \n{repr(certificate)}"
    except (InvalidIdFromContextException, CertificateNotFound) as e:
        message = str(e)

    context.bot.send_message(chat_id=update.effective_chat.id, text=message)
