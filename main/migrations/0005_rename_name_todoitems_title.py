# Generated by Django 4.2 on 2023-04-08 19:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_todoitems_createdat_todoitems_description_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todoitems',
            old_name='name',
            new_name='title',
        ),
    ]