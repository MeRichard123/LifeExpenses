# Generated by Django 3.1.1 on 2020-09-11 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery', '0006_auto_20200911_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='list',
            name='status',
            field=models.CharField(choices=[('In progress', 'In progress'), ('Completed', 'Completed')], default='In progress', max_length=12, null=True),
        ),
    ]
