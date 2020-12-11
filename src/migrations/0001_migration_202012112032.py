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
    expiration_at = DateTimeField(default=datetime.datetime.now)
    class Meta:
        table_name = "certificate"


