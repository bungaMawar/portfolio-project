# Generated by Django 2.0.2 on 2019-07-11 03:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0002_auto_20190711_0259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='imagefun',
            new_name='image',
        ),
    ]
