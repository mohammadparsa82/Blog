# Generated by Django 4.2.7 on 2024-02-05 20:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0007_comment_post'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approch',
            new_name='approed',
        ),
    ]