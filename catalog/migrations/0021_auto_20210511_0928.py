# Generated by Django 3.1.7 on 2021-05-11 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0020_auto_20210505_1142'),
    ]

    operations = [
        migrations.AddField(
            model_name='venueinstance',
            name='time_end',
            field=models.TimeField(blank=True, null=True, verbose_name='結束'),
        ),
        migrations.AddField(
            model_name='venueinstance',
            name='time_start',
            field=models.TimeField(blank=True, null=True, verbose_name='開始'),
        ),
    ]
