# Generated by Django 4.1.5 on 2023-05-11 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_alter_user_signup_day_alter_user_signup_month'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=11, max_length=50),
        ),
    ]