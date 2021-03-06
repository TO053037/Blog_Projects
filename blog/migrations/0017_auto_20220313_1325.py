# Generated by Django 3.2.6 on 2022-03-13 04:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0016_auto_20220313_1322'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='picture',
            field=models.ImageField(blank=True, default='default.JPG', null=True, upload_to='article_thumbnail', verbose_name='記事のサムネ'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 13, 13, 25, 29, 483635), verbose_name='公開日'),
        ),
    ]
