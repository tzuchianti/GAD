# Generated by Django 3.1.7 on 2021-04-26 11:10

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0012_auto_20210422_1513'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activityuser',
            name='department',
            field=models.CharField(max_length=10, verbose_name='部門'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='e_mail',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='信箱'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='extension',
            field=models.IntegerField(blank=True, null=True, verbose_name='雲端分機'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='identity',
            field=models.CharField(max_length=10, verbose_name='身份別'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='name',
            field=models.CharField(max_length=12, verbose_name='姓名'),
        ),
        migrations.AlterField(
            model_name='activityuser',
            name='telephone',
            field=models.IntegerField(blank=True, null=True, verbose_name='電話'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='area',
            field=models.CharField(max_length=10, verbose_name='地區'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='av_device',
            field=models.CharField(max_length=40, verbose_name='影音設備'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='capacity',
            field=models.IntegerField(blank=True, null=True, verbose_name='容納人數'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='club_name',
            field=models.CharField(max_length=12, verbose_name='會所名稱'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='site_feature',
            field=models.CharField(max_length=10, verbose_name='場地特性'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='site_name',
            field=models.CharField(max_length=12, verbose_name='場地名稱'),
        ),
        migrations.AlterField(
            model_name='venue',
            name='suitable',
            field=models.CharField(max_length=40, verbose_name='適合活動'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='activity_attr',
            field=models.CharField(max_length=5, verbose_name='活動屬性'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='activity_category',
            field=models.CharField(max_length=5, verbose_name='活動類別'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='activity_end',
            field=models.DateTimeField(blank=True, null=True, verbose_name='活動結束'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='activity_name',
            field=models.TextField(max_length=5, verbose_name='活動名稱'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='activity_people',
            field=models.IntegerField(blank=True, null=True, verbose_name='活動人數'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='activity_start',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True, verbose_name='活動開始'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='編號'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='meals_number',
            field=models.IntegerField(blank=True, default=0, verbose_name='用餐人數'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='message',
            field=models.TextField(help_text=' 請輸入你的意見 ', max_length=100, verbose_name='意見說明'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='report',
            field=models.BooleanField(default=False, verbose_name='是否回報'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='sound_control',
            field=models.BooleanField(default=False, verbose_name='音控志工'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='space_use',
            field=models.CharField(help_text='請給分  1分最低5分最高', max_length=10, verbose_name='空間使用滿意度'),
        ),
        migrations.AlterField(
            model_name='venueinstance',
            name='user_service',
            field=models.CharField(help_text='請給分  1分最低5分最高', max_length=10, verbose_name='人員服務滿意度'),
        ),
        migrations.AlterField(
            model_name='venuemanager',
            name='e_mail',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='信箱'),
        ),
        migrations.AlterField(
            model_name='venuemanager',
            name='extension',
            field=models.IntegerField(blank=True, null=True, verbose_name='雲端分機'),
        ),
        migrations.AlterField(
            model_name='venuemanager',
            name='name',
            field=models.CharField(max_length=200, verbose_name='姓名'),
        ),
    ]
