# Generated by Django 4.1.5 on 2023-06-04 18:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_alter_user_signup_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_day',
            field=models.CharField(default=4, max_length=50),
        ),
        migrations.AlterField(
            model_name='user',
            name='signup_month',
            field=models.CharField(default=6, max_length=50),
        ),
    ]
