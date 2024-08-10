from django.db import models
from django.contrib.auth.models import AbstractUser


class Career(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class User(AbstractUser):
    career = models.ForeignKey(
        Career,
        related_name="careers",
        on_delete=models.PROTECT,
        blank=True,
        null=True
    )
    control_number = models.CharField(max_length=9, blank=True, null=True)
    employee_card = models.CharField(max_length=4, blank=True, null=True)


class Subject(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=100, blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.name} - {self.description}"

