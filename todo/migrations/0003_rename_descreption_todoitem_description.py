# Generated by Django 5.0.2 on 2024-04-28 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_todoitem_descreption'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitem',
            old_name='descreption',
            new_name='description',
        ),
    ]
