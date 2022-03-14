# Generated by Django 3.2.6 on 2022-03-12 03:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20220312_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, default='enemy2.png', null=True, upload_to='article_thumbnail'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 12, 12, 30, 31, 826384), verbose_name='公開日'),
        ),
    ]