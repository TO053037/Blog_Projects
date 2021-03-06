# Generated by Django 3.2.6 on 2022-03-14 04:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20220314_1309'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='is_public',
            field=models.BooleanField(choices=[(False, '非公開'), (True, '公開中')], default=False, verbose_name='公開設定'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 14, 13, 31, 47, 311012), verbose_name='公開日'),
        ),
    ]
