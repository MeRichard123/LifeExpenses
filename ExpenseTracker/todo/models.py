from django.db import models
from django.contrib.auth.models import User

# Create your models here.


PRIORITY = (
    ('0', '!'),
    ('1', '!!'),
    ('2', '!!!'),
)

STATUS = (
    ('0', 'In progress'),
    ('1', 'Completed'),
)


class Todo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    task = models.CharField(max_length=60, null=True,
                            verbose_name="your task", )
    priority = models.CharField(max_length=3, choices=PRIORITY, default=0, null=True,
                                help_text="Set priority of this task",
                                verbose_name="priority")
    description = models.CharField(max_length=100, null=True,
                                   verbose_name="enter description")
    status = models.CharField(max_length=15, choices=STATUS, default=0, null=True,
                              help_text="Set status of this task",
                              verbose_name="status")
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return str(self.task)
