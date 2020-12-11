from models.Certificate import Certificate
from exceptions import CertificateNotFound
import peewee
import datetime


class CertificateService:
    def create_certificate(self, title, recipient_name, days_to_expire=None):
        expiration_at = None
        if days_to_expire:
            expiration_at = datetime.datetime.now() + datetime.timedelta(days=days_to_expire)

        certificate = Certificate.create(title=title, recipient=recipient_name, expiration_at=expiration_at)
        certificate.save()
        return certificate

    def get_certificate_by_id(self, id):
        try:
            return Certificate.get(id=id)
        except peewee.DoesNotExist:
            raise CertificateNotFound('Certificate not found')

    def delete_certificate_by_id(self, id):
        try:
            return self.get_certificate_by_id(id).delete_instance()
        except peewee.DoesNotExist:
            raise CertificateNotFound('Certificate not found')
