# Generated by Django 3.1.7 on 2021-03-26 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ActivityUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identity', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=12)),
                ('department', models.CharField(max_length=10)),
                ('e_mail', models.EmailField(blank=True, max_length=254, null=True)),
                ('telephone', models.IntegerField(blank=True, null=True)),
                ('extension', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
