# Generated by Django 5.0 on 2023-12-12 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_skills_subtitle'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='about',
            name='banner',
        ),
        migrations.AddField(
            model_name='about',
            name='btn_link',
            field=models.TextField(default='project.html'),
        ),
        migrations.AddField(
            model_name='about',
            name='btn_text',
            field=models.CharField(default='Got a Project', max_length=500),
        ),
        migrations.DeleteModel(
            name='AboutBanner',
        ),
    ]
