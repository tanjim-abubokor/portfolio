# Generated by Django 5.0 on 2023-12-12 17:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_aboutbanner_skills_about'),
    ]

    operations = [
        migrations.AddField(
            model_name='skills',
            name='date',
            field=models.CharField(default='2016-2023', max_length=1000),
        ),
    ]
