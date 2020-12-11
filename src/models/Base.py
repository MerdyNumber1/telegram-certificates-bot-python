import datetime

from database import db
from peewee import DateTimeField, Model


class BaseModel(Model):
    created_at = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db
