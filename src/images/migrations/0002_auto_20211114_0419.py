# Generated by Django 2.2 on 2021-11-13 22:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='image',
            old_name='classfield',
            new_name='classified',
        ),
    ]
