# Generated by Django 4.1.5 on 2023-04-15 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0005_alter_userprofile_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
