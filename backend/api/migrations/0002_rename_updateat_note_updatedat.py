# Generated by Django 3.2.5 on 2021-07-18 15:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='note',
            old_name='updateAt',
            new_name='updatedAt',
        ),
    ]