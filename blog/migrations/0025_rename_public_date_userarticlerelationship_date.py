# Generated by Django 3.2.6 on 2022-04-03 02:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20220403_1057'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userarticlerelationship',
            old_name='public_date',
            new_name='date',
        ),
    ]