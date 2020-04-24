import uuid

from django.core.validators import MinLengthValidator
from django.db import models


class Account(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    email = models.CharField(max_length=100)
    password = models.CharField(validators=[MinLengthValidator(10)], max_length=100)
