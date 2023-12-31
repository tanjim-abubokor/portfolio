# Generated by Django 5.0 on 2023-12-14 17:05

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_testimonial_alter_project_video_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100000)),
                ('image', models.TextField()),
                ('description', ckeditor.fields.RichTextField()),
                ('data', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
