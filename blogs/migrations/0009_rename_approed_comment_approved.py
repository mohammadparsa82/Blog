# Generated by Django 4.2.7 on 2024-02-05 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0008_rename_approch_comment_approed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='approed',
            new_name='approved',
        ),
    ]
