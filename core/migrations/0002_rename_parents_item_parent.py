# Generated by Django 3.2 on 2022-10-26 09:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='parents',
            new_name='parent',
        ),
    ]
