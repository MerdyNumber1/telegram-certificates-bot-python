# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Certificate(peewee.Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    title = CharField(max_length=255, unique=True)
    recipient = CharField(index=True, max_length=255, unique=True)
    expiration_at = DateTimeField(default=datetime.datetime.now, null=True)
    class Meta:
        table_name = "certificate"


def backward(old_orm, new_orm):
    certificate = new_orm['certificate']
    return [
        # Apply default value datetime.datetime(2020, 12, 11, 21, 42, 6, 502098) to the field certificate.expiration_at
        certificate.update({certificate.expiration_at: datetime.datetime(2020, 12, 11, 21, 42, 6, 502098)}).where(certificate.expiration_at.is_null(True)),
    ]
