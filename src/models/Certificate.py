import datetime

from models.Base import BaseModel
from peewee import DateTimeField, CharField
import datetime


class Certificate(BaseModel):
    title = CharField(max_length=255, verbose_name='title')
    recipient = CharField(max_length=255, index=True, verbose_name='recipient_user')
    expiration_at = DateTimeField(default=None, null=True, verbose_name='expiration_date')

    def __str__(self):
        return f'<Certificate title={self.title}>'

    def __repr__(self):
        return f"Number: {self.id}, \n" \
               f"Title: {self.title}, \n" \
               f"Recipient name: {self.recipient}, \n" \
               f"Expiration date: {self.expiration_at.ctime() if isinstance(self.expiration_at, datetime.date) else None}"
