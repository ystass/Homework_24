from django.contrib import admin

from users.models import User, Payments


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone', 'city')
    list_filter = ('email', 'city')


@admin.register(Payments)
class UserPayments(admin.ModelAdmin):
    list_display = ('id', 'user', 'date', 'course', 'lesson', 'payment_amount', 'payment_method')

