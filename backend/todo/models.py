# File: ./backend/todo/models.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class Message(models.Model):
    user = models.ForeignKey('auth.User', on_delete=models.PROTECT)
    message = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
