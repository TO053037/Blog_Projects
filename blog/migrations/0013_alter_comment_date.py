# Generated by Django 3.2.6 on 2022-03-12 04:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0012_auto_20220312_1309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 12, 13, 45, 45, 27857), verbose_name='公開日'),
        ),
    ]