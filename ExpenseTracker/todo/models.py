from django.db import models

# Create your models here.


PRIORITY = (
    ('0', ''),
    ('1', '!'),
    ('2', '!!'),
    ('3', '!!!'),
)


class Category(models.Model):
    name = models.CharField(max_length=70, null=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Todo(models.Model):
    task = models.CharField(max_length=60, null=True,
                            verbose_name="your task",
                            help_text="name of your task"
                            )
    priority = models.CharField(max_length=3, choices=PRIORITY, default=0, null=True,
                                help_text="Set priority of this task",
                                verbose_name="priority")
    description = models.CharField(max_length=150, null=True,
                                   verbose_name="enter description of this task")
    category = models.ManyToManyField(Category,
                                      verbose_name="what category?")
    date_added = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ['-date_added']
        verbose_name = "Todo"
        verbose_name_plural = "Todos"

    def __str__(self):
        return self.task
