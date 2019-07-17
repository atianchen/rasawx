from django.db import models


class Token(models.Model):
    token  = models.CharField(max_length=200)
    expireDate = models.DateTimeField()

