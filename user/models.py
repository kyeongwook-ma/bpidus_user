import uuid

from django.db import models


class User(models.Model):
    class Gender(models.TextChoices):
        MALE = 'M'
        FEMALE = 'F'
        OTHER = 'O'

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=20, blank=False, default=None)
    nickname = models.CharField(max_length=30, blank=False, default=None)
    email = models.CharField(max_length=100, blank=False, default=None)
    phone_number = models.CharField(max_length=20, blank=False, default=None)
    gender = models.CharField(max_length=1, default=Gender.OTHER, blank=True, choices=Gender.choices)