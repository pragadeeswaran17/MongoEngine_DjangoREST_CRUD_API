from django.db import models
from mongoengine import Document, fields
# Create your models here.

class Poll(Document):
    poll_name = fields.StringField(required=True)
    poll_voutes = fields.IntField(required=True)
    
    

