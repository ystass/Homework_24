from django.contrib import admin

from materials.models import Course, Lesson


@admin.register(Course)
class UserPayments(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'owner')


@admin.register(Lesson)
class UserPayments(admin.ModelAdmin):
    list_display = ('id', 'title', 'description', 'course', 'owner')
