from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core.models import *

class TaskFileInline(admin.TabularInline):
    model = TaskFile
    extra = 0

@admin.register(User)
class UserAdmin(UserAdmin):
    def get_urls(self):
        urls = super(UserAdmin, self).get_urls()
        custom_urls = [
          # path('^import/$', self.process_import, name='process_import'),
        ]
        return custom_urls + urls
    list_display_links = ['id', 'username', 'name']
    fieldsets = (
        ('Данные пользователя', {
            'fields': (
                'username', 'name',
            )
        }),
        ('Редактирование полномочий', {
            'fields': (
                'is_staff', 'is_superuser', 'is_active', 'groups', 'user_permissions', 'password'
            )
        })
    )
    list_display = (
        'id', 'username', 'name'
    )
    list_filter = (
        'is_staff', 'is_superuser', 'groups', 'date_joined'
    )
    search_fields = (
        'name', 'username'
    )
    filter_horizontal = ['groups', 'user_permissions']
    ordering = ['name']


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'id', 'title', 'deadline', 'executor'
    )
    list_filter = (
        'deadline', 'executor'
    )
    search_fields = (
        'executor', 'title', 'details'
    )
    inlines = [TaskFileInline]
