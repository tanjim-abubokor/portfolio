# Generated by Django 5.0 on 2023-12-12 18:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_remove_about_banner_about_btn_link_about_btn_text_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='about',
            old_name='text',
            new_name='description',
        ),
    ]
