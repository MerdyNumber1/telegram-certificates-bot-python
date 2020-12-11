# auto-generated snapshot
from peewee import *
import datetime
import peewee


snapshot = Snapshot()


@snapshot.append
class Certificate(peewee.Model):
    created_at = DateTimeField(default=datetime.datetime.now)
    title = CharField(max_length=255)
    recipient = CharField(index=True, max_length=255)
    expiration_at = DateTimeField(default=datetime.datetime.now, null=True)
    class Meta:
        table_name = "certificate"


