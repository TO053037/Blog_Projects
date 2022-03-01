# Generated by Django 3.2.6 on 2022-02-28 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='記事のタイトル')),
                ('content', models.CharField(max_length=3000, verbose_name='記事内容')),
                ('public_settings', models.BooleanField(choices=[(False, '非公開'), (True, '公開中')], default=False, verbose_name='公開設定')),
                ('public_date', models.DateField(verbose_name='公開日')),
            ],
            options={
                'verbose_name_plural': '記事',
            },
        ),
    ]