from django.contrib import admin
from todolist_app import models
# Register your models here.

class TodolistView(admin.ModelAdmin):
    list_display = ['id','task','done', 'owner']


admin.site.register(models.TodoList,TodolistView)