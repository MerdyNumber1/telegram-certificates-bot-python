from models.Certificate import Certificate


class CertificateService:
    def create_certificate(self, title, recipient_name, expiration_at=None):
        certificate = Certificate.create(title=title, recipient=recipient_name, expiration_at=expiration_at)
        certificate.save()
        return certificate

    def get_certificate_by_id(self, id):
        return Certificate.get(id=id)

    def delete_certificate_by_id(self, id):
        return self.get_certificate_by_id(id).delete_instance()
