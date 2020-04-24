import uuid

from django.db import models


class Account(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        OTHER = 'O'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20)
    nickname = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=20)
    gender = models.CharField(max_length=1, choices=Gender.choices)
