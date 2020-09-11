from django.db.models.signals import post_save
from django.contrib.auth.models import User

from .models import ExpenseProfile


def expense_profile(sender, instance, created, **kwargs):
    if created:
        ExpenseProfile.objects.create(user=instance)


post_save.connect(expense_profile, sender=User)
