# Generated by Django 5.0 on 2023-12-13 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_introvideo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10000)),
                ('description', models.TextField()),
                ('btn', models.CharField(max_length=1000)),
                ('btn_link', models.URLField()),
            ],
        ),
    ]