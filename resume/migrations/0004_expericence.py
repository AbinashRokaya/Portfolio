# Generated by Django 5.1.1 on 2024-11-03 06:59

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0003_rename_qualification_education'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expericence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill', models.CharField(max_length=25)),
                ('company', models.CharField(max_length=25)),
                ('year', models.CharField(max_length=15)),
                ('text', tinymce.models.HTMLField()),
            ],
        ),
    ]
