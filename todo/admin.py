from django.contrib import admin
from .models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    fields = ('title', 'memo', 'date_completed', 'important', 'user', 'created')
    readonly_fields = ('created', )
