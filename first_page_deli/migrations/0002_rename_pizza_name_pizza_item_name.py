# Generated by Django 4.2.15 on 2024-10-15 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('first_page_deli', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pizza',
            old_name='pizza_name',
            new_name='item_name',
        ),
    ]
