# Generated by Django 2.2.5 on 2019-11-04 07:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo_first_app', '0005_auto_20191103_1643'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['due_date']},
        ),
        migrations.RemoveField(
            model_name='task',
            name='created',
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateField(default='2019-11-04'),
        ),
    ]
