# Generated by Django 5.1.1 on 2024-11-03 12:28

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0008_client'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_image', models.ImageField(blank=True, null=True, upload_to='image/')),
                ('blog_date', models.DateTimeField()),
                ('blog_text', tinymce.models.HTMLField()),
            ],
        ),
    ]
