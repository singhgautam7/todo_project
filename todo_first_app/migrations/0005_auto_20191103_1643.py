# Generated by Django 2.2.5 on 2019-11-03 16:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_first_app', '0004_auto_20191103_1352'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='task',
            options={'ordering': ['-created']},
        ),
    ]
