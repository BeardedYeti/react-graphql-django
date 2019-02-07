# File: ./backend/todo/admin.py
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from .models import Todo, Message

# Register your models here.
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed')

class MessageAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'creation_date')

admin.site.register(Todo, TodoAdmin)
admin.site.register(Message, MessageAdmin)