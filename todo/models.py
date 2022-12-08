from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


class Todo(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()

    def __str__(self):
        return self.title


class AccountUser(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    createdAt = models.DateTimeField("作成日", default=timezone.now)
    birthDay = models.DateTimeField("誕生日")

    def __str__(self):
        return self.username


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='')
    uploaded_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.description
