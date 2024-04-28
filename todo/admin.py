from django.contrib import admin
from .models import TodoItem

class TodoItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'created_at')
    list_filter = ('completed', 'created_at')
    search_fields = ('title',)
    date_hierarchy = 'created_at'
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'completed')
        }),
        ('Advanced Options', {
            'classes': ('collapse',),
            'fields': ('created_at',)
        }),
    )
    readonly_fields = ('created_at',)

admin.site.register(TodoItem, TodoItemAdmin)