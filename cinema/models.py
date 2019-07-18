from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


class Place(models.Model):
    name = models.CharField(max_length=50)
    hall = models.CharField(max_length=50)
    row = models.CharField(max_length=50)
    seat = models.CharField(max_length=50)
    armrests = models.CharField(max_length=50, choices=(('1', 'Да'), ('2', 'Нет')), default='2')
    comment = models.CharField(max_length=500)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

