# Generated by Django 3.2.8 on 2021-11-24 09:32

import core.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='user',
            managers=[
                ('objects', core.models.UserManager()),
            ],
        ),
    ]
