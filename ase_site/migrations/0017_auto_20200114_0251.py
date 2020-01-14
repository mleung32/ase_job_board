# Generated by Django 3.0.2 on 2020-01-14 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ase_site', '0016_auto_20200114_0013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posting',
            name='app_due_date',
            field=models.CharField(max_length=50, verbose_name='App Due Date'),
        ),
        migrations.AlterField(
            model_name='posting',
            name='school',
            field=models.CharField(blank=True, choices=[('Information', 'Information'), ('Economics', 'Economics'), ('Cognitive Science', 'Cognitive Science'), ('Sociology', 'Sociology')], max_length=80, verbose_name='School'),
        ),
    ]
