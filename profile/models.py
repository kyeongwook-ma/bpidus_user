import uuid

from django.db import models

from user.models import User


class UserProfile(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    name = models.CharField(max_length=50, unique=False)
    nickname = models.CharField(max_length=50, unique=False)
    email = models.EmailField(
        verbose_name='email address',
        max_length=100,
        unique=True
    )
    phone_number = models.CharField(max_length=10, unique=True, null=False, blank=False)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)

    class Meta:
        '''
        to set table name in database
        '''
        db_table = "profile"
