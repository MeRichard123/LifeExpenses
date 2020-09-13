from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class ExpenseProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name="profile")
    monthlyBudget = models.DecimalField(
        max_digits=50, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user}'s profile"


class ExpenseItem(models.Model):
    userProfile = models.ForeignKey(
        ExpenseProfile, null=True, on_delete=models.SET_NULL, related_name="item")
    name = models.CharField(max_length=100, null=True)
    price = models.DecimalField(max_digits=50, decimal_places=2, null=True)
    date_purchased = models.DateField(auto_now=False)

    class Meta:
        ordering = ['date_purchased']
        verbose_name_plural = "ExpenseItems"

    def __str__(self):
        return self.name
