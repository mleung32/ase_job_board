# Generated by Django 3.0.2 on 2020-01-14 00:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ase_site', '0015_auto_20200114_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='percent_time',
            field=models.IntegerField(blank=True, choices=[(15, '15%'), (25, '25%'), (40, '40%'), (50, '50%'), (75, '75%')], null=True, verbose_name='Percent Time'),
        ),
    ]