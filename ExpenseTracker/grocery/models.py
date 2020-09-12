from django.db import models
from django.contrib.auth.models import User

# Create your models here.


PROGRESS = (
    ('In progress', 'In progress'),
    ('Completed', 'Completed')
)


class List(models.Model):
    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             null=True,
                             related_name='list')
    name = models.CharField(max_length=70,
                            null=True)
    status = models.CharField(choices=PROGRESS,
                              null=True,
                              max_length=12,
                              default="In progress")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Shopping List'
        verbose_name_plural = 'Shopping Lists'


class Item(models.Model):
    name = models.CharField(max_length=70,
                            null=True)
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                default=0.00,
                                null=True)
    quantity = models.IntegerField(default=1,
                                   null=True)
    list = models.ForeignKey(List,
                             on_delete=models.CASCADE,
                             null=True,
                             related_name='item')
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}"

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Shopping Item'
        verbose_name_plural = 'Shopping Items'

    @property
    def total_item(self):
        return self.price * self.quantity
