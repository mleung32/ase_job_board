# Generated by Django 3.0.2 on 2020-01-13 00:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ase_site', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='classEndTime',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Class End Time'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='classStartTime',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Class Start Time'),
        ),
    ]