# Generated by Django 4.1.5 on 2023-05-17 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_user_signup_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=17, max_length=50),
        ),
    ]
