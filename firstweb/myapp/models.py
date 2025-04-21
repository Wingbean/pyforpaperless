from django.db import models

class Job(models.Model):
    fullname = models.CharField(max_length=255)
    tel = models.CharField(max_length=255)
    position = models.CharField(max_length=255)