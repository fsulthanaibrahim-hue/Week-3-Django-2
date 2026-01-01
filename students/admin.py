from django.contrib import admin
from .models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'course', 'email', 'phone', 'created_at')
    list_filter = ('course',)
    search_fields = ('name', 'course')
