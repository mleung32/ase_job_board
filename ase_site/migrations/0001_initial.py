# Generated by Django 3.0.2 on 2020-01-16 20:48

import django.contrib.postgres.indexes
import django.contrib.postgres.search
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posting',
            fields=[
                ('posting_id', models.AutoField(primary_key=True, serialize=False)),
                ('class_code', models.CharField(max_length=15, verbose_name='Class Code')),
                ('class_name', models.CharField(max_length=80, verbose_name='Class Name')),
                ('class_desc', models.TextField(verbose_name='Class Description')),
                ('semester', models.CharField(blank=True, choices=[('Fall 2019', 'Fall 2019'), ('Spring 2020', 'Spring 2020')], max_length=50, verbose_name='Semester')),
                ('position', models.CharField(blank=True, choices=[('GSI', 'GSI'), ('Head GSI', 'Head GSI'), ('Tutor', 'Tutor'), ('Reader', 'Reader'), ('Course Asst', 'Course Assistant')], max_length=25, verbose_name='Position')),
                ('school', models.CharField(blank=True, choices=[('Information', 'Information'), ('Economics', 'Economics'), ('Cognitive Science', 'Cognitive Science'), ('Sociology', 'Sociology'), ('Environmental, Science, Policy, and Management', 'Environmental, Science, Policy, and Management')], max_length=80, verbose_name='School')),
                ('percent_time', models.IntegerField(blank=True, choices=[(15, '15%'), (25, '25%'), (40, '40%'), (50, '50%'), (75, '75%')], null=True, verbose_name='Percent Time')),
                ('hours_per_wk', models.IntegerField(verbose_name='Hours Per Week')),
                ('fee_remission', models.BooleanField(default=True, verbose_name='Fee Remission')),
                ('instructor', models.CharField(max_length=200, verbose_name='Instructor')),
                ('mode', models.CharField(max_length=80, verbose_name='Mode')),
                ('instructor_bio', models.URLField(verbose_name='Instructor Bio')),
                ('class_days', models.CharField(blank=True, max_length=20, null=True, verbose_name='Class Days')),
                ('class_start_time', models.CharField(blank=True, max_length=15, null=True, verbose_name='Class Start Time')),
                ('class_end_time', models.CharField(blank=True, max_length=15, null=True, verbose_name='Class End Time')),
                ('num_positions', models.IntegerField(blank=True, null=True, verbose_name='Number of Positions')),
                ('position_notes', models.TextField(blank=True, verbose_name='Notes')),
                ('app_due_date', models.CharField(max_length=50, verbose_name='App Due Date')),
                ('app_url', models.URLField(null=True, verbose_name='App URL')),
                ('content_search', django.contrib.postgres.search.SearchVectorField(blank=True)),
            ],
        ),
        migrations.AddIndex(
            model_name='posting',
            index=django.contrib.postgres.indexes.GinIndex(fields=['content_search'], name='ase_site_po_content_2c0a43_gin'),
        ),
    ]
