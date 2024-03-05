# Generated by Django 4.2.7 on 2024-02-08 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_rename_approed_comment_approved'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-created_date']},
        ),
        migrations.AddField(
            model_name='comment',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]