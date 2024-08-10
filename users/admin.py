from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from users.models import Subject, User, Career

# Register your models here.
admin.site.register(Subject)
admin.site.register(User)
admin.site.register(Career)
