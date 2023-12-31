# Generated by Django 5.0 on 2023-12-12 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sidebar',
            name='menus',
        ),
        migrations.RemoveField(
            model_name='sidebar',
            name='social_links',
        ),
        migrations.AddField(
            model_name='sidebar',
            name='menus',
            field=models.ManyToManyField(to='app.menus'),
        ),
        migrations.AddField(
            model_name='sidebar',
            name='social_links',
            field=models.ManyToManyField(to='app.sociallinks'),
        ),
    ]
