# Generated by Django 4.1.3 on 2022-11-08 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_remove_bloguser_password_confirm'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloguser',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
    ]