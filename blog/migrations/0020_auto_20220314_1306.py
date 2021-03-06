# Generated by Django 3.2.6 on 2022-03-14 04:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_auto_20220313_1553'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, unique=True, verbose_name='カテゴリーのタイトル')),
                ('detail', models.CharField(max_length=1000, verbose_name='カテゴリーについて')),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 3, 14, 13, 6, 50, 538942), verbose_name='公開日'),
        ),
    ]
